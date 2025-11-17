"""
Tool for accessing product database through MCP Toolbox.
"""
import os
from toolbox_core import ToolboxSyncClient

def get_database_tool():
    """
    Loads database tools from the MCP Toolbox server.
    Returns the tool for querying product prices.
    
    Note: The toolbox server must be running separately:
    ./toolbox --tools-file "tools.yaml"
    
    The tools.yaml file uses environment variables for MySQL connection,
    which should be set in your .env file.
    """
    # Get toolbox URL from environment, default to localhost
    toolbox_url = os.environ.get("TOOLBOX_URL", "http://127.0.0.1:5000")
    # Ensure no trailing slash
    toolbox_url = toolbox_url.rstrip("/")
    
    try:
        # Create toolbox client
        db_client = ToolboxSyncClient(toolbox_url)
        # Load the tool defined in tools.yaml
        # The tool name should match what's defined in tools.yaml
        db_tool = db_client.load_tool("get-product-price")
        return db_tool
    except Exception as e:
        error_msg = (
            f"Error loading database tool: {e}\n"
            "Make sure:\n"
            "1. MCP Toolbox server is running: ./toolbox --tools-file 'tools.yaml'\n"
            "2. TOOLBOX_URL in .env matches the server URL\n"
            "3. MySQL connection variables (MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD) are set in .env\n"
            "4. The Cloud SQL instance is running and accessible"
        )
        print(error_msg)
        # Return None if tool can't be loaded
        return None