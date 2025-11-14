# Email to Udacity Support

**Subject:** Urgent: Organizational Policy Exception Request for Vertex AI Search (Betty's Bird Boutique Project)

**To:** support@udacity.com or [Your Course Support Portal]

---

Dear Udacity Support Team,

I am working on the Betty's Bird Boutique project and have encountered an organizational policy restriction that is preventing me from completing the assignment.

**Issue:**
I am unable to create a Vertex AI Search (Discovery Engine) datastore because the organizational policy `constraints/gcp.resourceLocations` is blocking the `global` location, which is required by Vertex AI Search.

**Error Details:**
- **Error Message:** "Location 'locations/global' violates constraint 'constraints/gcp.resourceLocations'"
- **Service:** Vertex AI Search (Discovery Engine API)
- **Location Required:** `global` (this is mandatory - no regional alternatives available)
- **Console Error:** Multi-region dropdown shows "No items to display"
- **API Error:** HTTP 400 with LOCATION_ORG_POLICY_VIOLATED

**Project Information:**
- **GCP Project ID:** `a4617265-u4192188-1762158583`
- **Udacity Account:** `user16609364987875b5@vocareumlabs.com`
- **Course:** [Your Course Name]
- **Project:** Betty's Bird Boutique Agent

**Project Context:**
This project involves building an AI customer service agent for Betty's Bird Boutique, a pet store specializing in birds and bird-related products. The agent uses Google's Agent Development Kit (ADK) and must integrate three tools: a product database tool (Cloud SQL MySQL), a document search tool (Vertex AI Search for PDF documents), and a web search tool (Google Search grounding). The agent needs to answer questions about store hours, store history, staff information, product prices, and general bird care knowledge. Vertex AI Search is specifically required to search through unstructured PDF documents (store hours, history, and staff information) that have been uploaded to Cloud Storage.

**What I've Already Completed:**
✅ Cloud SQL MySQL database setup and configuration
✅ All PDF documents uploaded to Cloud Storage bucket (`gs://betty-bird-boutique-docs`)
✅ Code implementation for all three tools (database, datastore search, web search)
✅ All other project requirements

**What I Need:**
An exception to the organizational policy `constraints/gcp.resourceLocations` to allow creation of Vertex AI Search datastores in the `global` location for project `a4617265-u4192188-1762158583`.

**Why This Is Critical:**
Vertex AI Search requires the `global` location - there is no regional alternative. This is a hard requirement of the service. Without this exception, I cannot complete the project as the datastore tool is one of the three required components.

**Requested Action:**
Please grant a temporary exception for this specific project to allow Vertex AI Search datastore creation in the `global` location. This exception can be scoped to:
- Project: `a4617265-u4192188-1762158583`
- Service: `discoveryengine.googleapis.com`
- Location: `global`
- Duration: Until project completion (or permanent if preferred)

**Timeline:**
I need to complete this project soon and would appreciate a quick resolution. If there's an alternative approach or workaround you can suggest, I'm happy to explore that as well.

Thank you for your assistance.

Best regards,
[Your Name]
[Your Udacity Email/Username]

---

## Additional Information (if needed)

**Technical Details:**
- Discovery Engine API is enabled: ✅
- Storage API is enabled: ✅
- All PDFs uploaded successfully: ✅
- Authentication working: ✅
- Only blocker is the org policy restriction

**Policy Details:**
```
Constraint: constraints/gcp.resourceLocations
Project: a4617265-u4192188-1762158583
Effect: Blocks 'global' location for Discovery Engine API
```

**Console URL:**
https://console.cloud.google.com/gen-app-builder/data-stores?project=a4617265-u4192188-1762158583

**GCS Bucket with PDFs:**
`gs://betty-bird-boutique-docs`
