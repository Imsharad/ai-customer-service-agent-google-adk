# Udacity Cloud Lab Setup Guide

## Overview
This project uses Udacity's federated Google Cloud Platform account (Cloud Lab) with temporary credentials. The setup uses Application Default Credentials (ADC) which works seamlessly with ADK.

## Authentication Setup

### Step 1: Log Out of Personal GCP Accounts
Before starting, ensure you're logged out of any personal GCP accounts:
```bash
gcloud auth list  # Check current accounts
gcloud auth revoke <your-personal-account>  # If needed
```

### Step 2: Authenticate with Udacity Cloud Lab
1. Open the Udacity workspace
2. Click on "Cloud Resources" tab
3. Click "Open Cloud Console" to access GCP
4. Copy the project ID from the console (found in .env.local: `a4617265-u4192188-1762158583`)

### Step 3: Set Up Application Default Credentials
Run this command to authenticate locally:
```bash
gcloud auth application-default login
```

When prompted, use your Udacity federated account credentials from `.env.local`:
- Email: `user16609364987875b5@vocareumlabs.com`
- Password: `j^jvzIkk*dWQ3aj%9uBJh}fC`

### Step 4: Set Project Context
```bash
gcloud config set project a4617265-u4192188-1762158583
```

### Step 5: Verify Authentication
```bash
gcloud auth application-default print-access-token
# Should return a token if authenticated correctly
```

## Environment Variables

### Required Variables
Copy `.env.example` to `.env` in the `starter/` directory and fill in:

```bash
# Already set from Udacity project
GOOGLE_CLOUD_PROJECT=a4617265-u4192188-1762158583
GOOGLE_CLOUD_LOCATION=global
DATASTORE_PROJECT_ID=a4617265-u4192188-1762158583
DATASTORE_LOCATION=global

# You need to set these after creating resources:
DATASTORE_ENGINE_ID=<from Vertex AI Search console>
MYSQL_HOST=<Cloud SQL instance IP>
MYSQL_USER=<your MySQL username>
MYSQL_PASSWORD=<your MySQL password>
TOOLBOX_URL=http://127.0.0.1:5000
```

### Important Notes
- **DO NOT set GOOGLE_APPLICATION_CREDENTIALS** for Udacity setup - use ADC instead
- ADK automatically detects and uses ADC when `GOOGLE_APPLICATION_CREDENTIALS` is not set
- The code is already configured to work with ADC (no service account needed)

## Resource Setup Checklist

### 1. Cloud SQL for MySQL
- [ ] Create MySQL instance in GCP Console
- [ ] Note the public IP address (MYSQL_HOST)
- [ ] Create database user (MYSQL_USER, MYSQL_PASSWORD)
- [ ] Run `betty_db.sql` to populate database
- [ ] Ensure instance is running and accessible

### 2. Vertex AI Search
- [ ] Create Vertex AI Search app in GCP Console
- [ ] Create data store connected to GCS bucket
- [ ] Upload PDF documents (bettys-history.pdf, bettys-hours.pdf, bettys-staff.pdf)
- [ ] Wait for indexing to complete
- [ ] Note the ENGINE_ID (DATASTORE_ENGINE_ID)
- [ ] Note the location (DATASTORE_LOCATION)

### 3. MCP Toolbox Server
- [ ] Install MCP Toolbox if not already installed
- [ ] Ensure `tools.yaml` is configured correctly
- [ ] Start toolbox server: `./toolbox --tools-file "tools.yaml"`
- [ ] Verify it's running on `http://127.0.0.1:5000`

## Budget Considerations

⚠️ **Important**: Udacity provides $25 budget for the entire course (~$10 typically sufficient)

- **Shut down resources immediately after use**:
  - Cloud SQL instances
  - Vertex AI Search apps
  - Any other running services

- **Check costs regularly**:
  ```bash
  gcloud billing accounts list
  ```

- **Set up billing alerts** (if possible in Udacity console)

## Troubleshooting

### Authentication Issues
```bash
# Clear existing credentials
rm ~/.config/gcloud/application_default_credentials.json

# Re-authenticate
gcloud auth application-default login
```

### Project Access Issues
```bash
# Verify project access
gcloud projects describe a4617265-u4192188-1762158583

# Check permissions
gcloud projects get-iam-policy a4617265-u4192188-1762158583
```

### ADK Not Finding Credentials
- Ensure ADC is set up: `gcloud auth application-default print-access-token`
- Check that `GOOGLE_APPLICATION_CREDENTIALS` is NOT set in `.env`
- ADK will automatically use ADC if service account path is not provided

## Code Compatibility

The implementation is already compatible with Udacity's federated account setup:

✅ **agent.py**: Uses ADC automatically (no service account required)
✅ **datastore.py**: Uses discoveryengine which works with ADC
✅ **search_agent.py**: Uses ADK's google_search which works with ADC
✅ **toolbox_tools.py**: Uses ToolboxSyncClient (independent of GCP auth)

All tools will automatically use Application Default Credentials when properly configured.