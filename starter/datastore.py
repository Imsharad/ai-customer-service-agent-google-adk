from google.api_core.client_options import ClientOptions
from google.cloud import discoveryengine_v1 as discoveryengine
from google.adk.tools import FunctionTool
import os

# Definition of a tool that accesses a Vertex AI Search Datastore

#
# This is based on code provided by Google at
# https://cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-search
#
# The object definitions aren't available to all IDEs because of Google's ProtoBuf
# implementation, so the IDE may generate a warning, but work fine. I've used
# dicts here instead, but indicated the Class that could be used instead.
# You can see the definitions at
# https://cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types

def search(
    project_id: str,
    location: str,
    engine_id: str,
    search_query: str,
) -> list[str]:
    """
    Search the Vertex AI Search datastore for information.
    
    Args:
        project_id: GCP project ID
        location: Location of the datastore (e.g., 'global' or 'us-central1')
        engine_id: The engine ID of the Vertex AI Search datastore
        search_query: The search query string
        
    Returns:
        List of search result strings containing relevant document excerpts
    """
    #  For more information, refer to:
    # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    client_options = (
        ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
        if location != "global"
        else None
    )

    # Create a client
    client = discoveryengine.SearchServiceClient(client_options=client_options)

    # The full resource name of the search app serving config
    serving_config = f"projects/{project_id}/locations/{location}/collections/default_collection/engines/{engine_id}/servingConfigs/default_config"

    # Create search request using discoveryengine.SearchRequest
    # Using SearchRequest class for proper type safety
    request = discoveryengine.SearchRequest(
        serving_config=serving_config,
        query=search_query,
        page_size=5,  # Limit results to top 5 for relevance
        content_search_spec=discoveryengine.SearchRequest.ContentSearchSpec(
            snippet_spec=discoveryengine.SearchRequest.ContentSearchSpec.SnippetSpec(
                max_snippet_count=3,  # Get up to 3 snippets per result
                reference_only=False,  # Include full content, not just references
            ),
            summary_spec=discoveryengine.SearchRequest.ContentSearchSpec.SummarySpec(
                summary_result_count=5,  # Summarize top 5 results
                include_citations=True,  # Include citations for attribution
            ),
        ),
    )

    page_result = client.search(request=request)

    # Format and return the results
    results = []
    for result in page_result.results:
        # Extract document information
        document = result.document
        # Get snippets from the result
        if hasattr(result, 'document_snippets') and result.document_snippets:
            for snippet in result.document_snippets:
                if snippet.snippet:
                    results.append(snippet.snippet)
        # Also include document struct data if available
        if document.struct_data:
            # Extract relevant fields from struct data
            content_parts = []
            for key, value in document.struct_data.items():
                if key.lower() in ['title', 'content', 'text', 'body']:
                    content_parts.append(str(value))
            if content_parts:
                results.append(" ".join(content_parts))

    return results if results else ["No relevant information found in the store documents."]


def get_datastore_search_tool() -> FunctionTool:
    """
    Creates and returns a tool for searching the Vertex AI Search datastore.
    
    This tool allows the agent to answer questions about store hours, location,
    history, staff, and other store-specific information from uploaded documents.
    
    Returns:
        Tool instance configured for datastore search
    """
    # Get configuration from environment variables
    project_id = os.environ.get("DATASTORE_PROJECT_ID", os.environ.get("GOOGLE_CLOUD_PROJECT", ""))
    location = os.environ.get("DATASTORE_LOCATION", os.environ.get("GOOGLE_CLOUD_LOCATION", "global"))
    engine_id = os.environ.get("DATASTORE_ENGINE_ID", "")
    
    def search_datastore(search_query: str) -> str:
        """
        Search the Vertex AI Search datastore for store-related information.

        Args:
            search_query: The query to search for in store documents

        Returns:
            Formatted string containing search results from store documents

        Note: This function uses Application Default Credentials (ADC) which works
        with Udacity's federated account setup. Ensure you've run:
        gcloud auth application-default login
        """
        # Function implementation remains the same
        if not project_id or not engine_id:
            error_msg = (
                "Error: Datastore configuration is missing. Please check environment variables.\n"
                f"Current values - PROJECT_ID: {project_id or 'NOT SET'}, ENGINE_ID: {engine_id or 'NOT SET'}\n"
                "For Udacity setup, ensure you've set DATASTORE_PROJECT_ID and DATASTORE_ENGINE_ID in .env"
            )
            return error_msg
        
        try:
            results = search(project_id, location, engine_id, search_query)
            # Format results as a single string
            if results:
                formatted_results = "\n\n".join(results)
                return formatted_results
            else:
                return "No relevant information found in the store documents."
        except Exception as e:
            error_msg = f"Error searching datastore: {str(e)}\n"
            if "authentication" in str(e).lower() or "credential" in str(e).lower():
                error_msg += (
                    "Authentication error detected. For Udacity setup, ensure you've run:\n"
                    "gcloud auth application-default login\n"
                    "And that your project ID is correct: a4617265-u4192188-1762158583"
                )
            return error_msg
    
    # Create tool with proper description
    return FunctionTool(search_datastore)
