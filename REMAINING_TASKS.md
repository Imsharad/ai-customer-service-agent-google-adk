# Project Completion Checklist

## ✅ COMPLETED

1. **Code Implementation** ✅
   - Root agent (`agent.py`) with InMemorySessionService ✅
   - Agent prompts (`agent-prompt.txt`, `search-prompt.txt`) ✅
   - Database tool (`toolbox_tools.py`, `tools.yaml`) ✅
   - Datastore tool (`datastore.py`) ✅
   - Web search tool (`search_agent.py`) ✅
   - Error handling and integration ✅

2. **Infrastructure Setup** ✅
   - Cloud SQL MySQL database created and populated ✅
   - Database connection configured in `.env` ✅
   - Scripts organized and ready ✅

3. **Scripts Created** ✅
   - Personal account workflow scripts ✅
   - Cloud SQL management scripts ✅
   - Utility scripts ✅
   - Master workflow script (`run_project.sh`) ✅

## 🔄 REMAINING TASKS (In Order)

### Step 1: Set Up Vertex AI Search in Personal Account
**Status:** Scripts ready, needs execution

```bash
cd starter
./scripts/personal-account/switch_to_personal_account.sh
# Enter your personal GCP project ID when prompted

./scripts/personal-account/setup_personal_account.sh <your-project-id>
```

**What this does:**
- Enables Discovery Engine API
- Creates GCS bucket
- Uploads PDFs (bettys-history.pdf, bettys-hours.pdf, bettys-staff.pdf)
- Creates Vertex AI Search datastore
- Updates `.env` with personal account details

**Estimated time:** 5-10 minutes (including indexing wait)

---

### Step 2: Install Dependencies (if not already done)
**Status:** Check and install if needed

```bash
cd starter
uv pip install -r requirements.txt

# Verify MCP Toolbox is installed
which toolbox
# If not installed, follow Udacity course instructions
```

**Required packages:**
- `google-adk`
- `google-cloud-discoveryengine`
- `toolbox_core`
- `mysql-connector-python`

---

### Step 3: Start Cloud SQL Database
**Status:** Script ready, needs execution

```bash
cd starter
./scripts/cloud-sql/start.sh
```

**Verifies:**
- Cloud SQL instance is running
- Connection details are correct
- Database is accessible

---

### Step 4: Start MCP Toolbox Server
**Status:** Needs execution

```bash
cd starter
./toolbox --tools-file "tools.yaml"
```

**Keep this terminal running!** The toolbox server must stay active.

**Verify:** Should see "Listening on http://127.0.0.1:5000"

---

### Step 5: Test the Agent
**Status:** Needs execution and screenshots

**In a NEW terminal:**

```bash
cd starter
adk web
```

**Test queries (in order):**

1. **Datastore Tool Test:**
   - "When are you open on Thursday?"
   - "Who is Betty?"

2. **Web Search Tool Test:**
   - "What kind of bird did she own?"
   - "What do they eat?"

3. **Database Tool Test:**
   - "Can I buy that from you?"
   - "What's the price of a bird cage?"

4. **Guardrail Test:**
   - "Tell me about politics"
   - "What's the weather today?"

---

### Step 6: Capture Screenshots
**Status:** CRITICAL - Required for submission

**Required screenshots:**

1. **Root Agent Interface**
   - Shows session ID visible
   - Shows agent name/description

2. **Datastore Tool Usage**
   - User question: "When are you open on Thursday?"
   - Shows tool call details (request/response)
   - Shows document excerpts from PDFs

3. **Web Search Tool Usage**
   - User question: "What kind of bird did she own?"
   - Shows tool call details
   - Shows citations/attribution

4. **Database Tool Usage**
   - User question: "Can I buy that from you?" or "What's the price of a bird cage?"
   - Shows tool call details
   - Shows SQL query and results

5. **Guardrail Enforcement**
   - Off-topic question
   - Shows agent declining appropriately

**Save screenshots to:** `screenshots/` directory (create if needed)

---

### Step 7: Verify Rubric Criteria

**Check against `docs/rubric.md`:**

#### Root Agent ✅
- [x] Agent object created ✅
- [x] InMemorySessionService ✅
- [x] Model selection with justification ✅
- [x] Agent prompt with persona ✅
- [ ] Screenshots showing session IDs ⏳
- [ ] Screenshots showing all three tools ⏳

#### Database Tool ✅
- [x] tools.yaml configured ✅
- [x] ToolboxSyncClient implemented ✅
- [ ] Screenshots showing tool usage ⏳

#### Datastore Tool ✅
- [x] search() function implemented ✅
- [x] Tool function created ✅
- [x] Integrated in agent.py ✅
- [ ] Screenshots showing tool usage ⏳

#### Web Search Tool ✅
- [x] AgentTool created ✅
- [x] Google Search grounding ✅
- [x] Model selection justified ✅
- [ ] Screenshots showing tool usage ⏳

#### Coding Best Practices ✅
- [x] Proper file organization ✅
- [x] Comments and docstrings ✅
- [x] Descriptive naming ✅

---

### Step 8: Clean Up Resources
**Status:** After testing and screenshots

```bash
# Stop Cloud SQL
./scripts/cloud-sql/stop.sh

# Clean up personal account resources
./scripts/personal-account/cleanup_personal_account.sh <your-project-id>

# Switch back to Udacity account (optional)
./scripts/personal-account/switch_back_to_udacity.sh
```

---

## 🎯 Quick Start Command

**Run everything automatically:**

```bash
cd starter
./run_project.sh
```

This will guide you through all steps interactively!

---

## 📋 Final Submission Checklist

Before submitting:

- [ ] All three tools working correctly
- [ ] Screenshots captured showing:
  - [ ] Session ID visible
  - [ ] All three tools used successfully
  - [ ] Tool call details visible
  - [ ] Guardrail enforcement shown
- [ ] Code reviewed for comments/docstrings
- [ ] `.env` file configured correctly
- [ ] Resources cleaned up (if desired)
- [ ] Project ready for submission

---

## ⏱️ Estimated Time to Complete

- **Setup:** 10-15 minutes
- **Testing:** 15-20 minutes
- **Screenshots:** 10 minutes
- **Total:** ~45 minutes

---

## 🚨 Critical Notes

1. **Screenshots are REQUIRED** - Without them, the project cannot be evaluated
2. **All three tools must work** - Database, Datastore, Web Search
3. **Session ID must be visible** - Important for rubric compliance
4. **Tool call details must be shown** - Request/response information visible
5. **Clean up after testing** - To avoid costs in personal account
