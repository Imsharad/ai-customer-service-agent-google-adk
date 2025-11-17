# Betty's Bird Boutique - AI Customer Service Agent

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4)](https://cloud.google.com/agent-development-kit)
[![Gemini](https://img.shields.io/badge/Model-Gemini_2.5_Flash-FF6F00)](https://ai.google.dev/models/gemini)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

An intelligent AI customer service agent for Betty's Bird Boutique - a pet store specializing in birds, bird food, and accessories. Built with Google's Agent Development Kit (ADK) and powered by Gemini 2.5 Flash.

## 🐦 Project Overview

Betty's Bird Boutique is upgrading its basic website with an AI-powered customer service agent that can help customers with:

- **Product Information & Pricing** - Database-driven product lookup and pricing
- **Store Information** - Hours, location, history, and staff details from PDF documents
- **General Bird Knowledge** - Web-sourced information about bird care, breeds, and behaviors
- **Intelligent Guardrails** - Focused conversations about birds and store operations only

**Key Requirement**: The agent encourages in-store visits rather than taking online orders, building customer relationships.

## 🏗️ Architecture

### Core Components

```
betty-bird-boutique/
├── starter/
│   ├── agent.py              # Main agent configuration
│   ├── agent-prompt.txt      # Agent personality & instructions
│   ├── datastore.py          # Vertex AI Search integration
│   ├── search_agent.py       # Google Search tool
│   ├── toolbox_tools.py      # Database connectivity
│   ├── tools.yaml           # MCP Toolbox configuration
│   └── docs/                # Store information PDFs
├── docs/                    # Project documentation
└── scripts/                 # Setup and utility scripts
```

### AI Agent Tools

The agent uses three specialized tools:

1. **🗃️ Database Tool** - MySQL integration via MCP Toolbox
   - Product pricing lookup
   - Inventory information
   - Secure parameterized queries

2. **📄 Datastore Search Tool** - Vertex AI Search
   - Store hours and location
   - Company history and staff information
   - PDF document knowledge base

3. **🌐 Web Search Tool** - Google Search integration
   - Current bird care trends
   - General bird information
   - Real-time information retrieval

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Cloud Project with enabled APIs:
  - Vertex AI API
  - Discovery Engine API
  - Cloud SQL (if using managed database)
- MCP Toolbox server

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Imsharad/betty-bird-boutique.git
   cd betty-bird-boutique/starter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. **Configure environment variables**
   ```bash
   # Google Cloud Configuration
   export GOOGLE_CLOUD_PROJECT="your-project-id"
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account.json"

   # Vertex AI Search Configuration
   export SEARCH_ENGINE_ID="your-search-engine-id"
   export SEARCH_LOCATION="global"

   # Database Configuration
   export DB_HOST="localhost"
   export DB_PORT="3306"
   export DB_USER="your-username"
   export DB_PASSWORD="your-password"
   export DB_NAME="bird_store"

   # MCP Toolbox Configuration
   export TOOLBOX_URL="http://127.0.0.1:5000"
   ```

5. **Start the MCP Toolbox server**
   ```bash
   # Follow MCP Toolbox documentation to start server
   # Ensure tools.yaml is properly configured
   ```

6. **Run the agent**
   ```bash
   python agent.py
   ```

## 🛠️ Configuration

### Agent Configuration

The agent uses **Gemini 2.5 Flash** for optimal balance of:
- **Performance** - Advanced reasoning capabilities
- **Speed** - Fast response times for customer service
- **Cost-effectiveness** - Efficient token usage

### Database Setup

Configure your MySQL database with the products table:

```sql
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(100),
    in_stock BOOLEAN DEFAULT TRUE
);
```

### Vertex AI Search Setup

1. Create a search engine in Google Cloud Console
2. Upload store documents (PDFs) to your datastore
3. Configure search specifications in `datastore.py`

## 💬 Usage Examples

### Product Pricing Inquiry
```
Customer: "How much do canary seeds cost?"
Agent: "Let me check our current pricing for canary seeds..."
[Database tool retrieval]
Agent: "Our premium canary seed mix is $12.99 for a 5lb bag..."
```

### Store Information
```
Customer: "What are your store hours?"
Agent: "Let me look up our current hours..."
[Datastore search tool]
Agent: "We're open Monday-Friday 9am-7pm, Saturday 9am-6pm..."
```

### General Bird Care
```
Customer: "How often should I clean my parakeet's cage?"
Agent: "Let me find the latest guidance on parakeet care..."
[Web search tool]
Agent: "Experts recommend cleaning your parakeet's cage weekly..."
```

## 🔒 Security & Guardrails

### Prompt Engineering Guardrails
- **Topic Boundaries** - Conversations limited to birds and store operations
- **No Order Taking** - Agent redirects to in-store visits
- **Professional Tone** - Friendly, helpful customer service approach

### Technical Security
- **Parameterized Queries** - SQL injection protection
- **Environment Variables** - Secure credential management
- **Input Validation** - Query sanitization and filtering

## 🧪 Testing

### Development Environment Testing

Use the ADK web testing environment:

```bash
# Start the development server
adk web

# Access the testing interface at:
# http://localhost:8080
```

### Conversation Testing Checklist

- [ ] Database tool responds to product inquiries
- [ ] Datastore tool retrieves store information
- [ ] Web search tool answers general bird questions
- [ ] Agent maintains conversation context
- [ ] Guardrails prevent off-topic discussions
- [ ] Session management works across multi-turn conversations

## 📁 Project Structure

```
betty-bird-boutique/
├── README.md                 # This file
├── .env.example             # Environment template
├── .gitignore              # Git ignore patterns
├── starter/                # Main application code
│   ├── agent.py            # Agent configuration & setup
│   ├── agent-prompt.txt    # Agent instructions & personality
│   ├── datastore.py        # Vertex AI Search tool
│   ├── search_agent.py     # Google Search integration
│   ├── toolbox_tools.py    # Database tool via MCP Toolbox
│   ├── tools.yaml         # MCP Toolbox configuration
│   ├── requirements.txt   # Python dependencies
│   ├── docs/              # Store information PDFs
│   │   ├── bettys-history.pdf
│   │   ├── bettys-hours.pdf
│   │   └── bettys-staff.pdf
│   └── scripts/           # Setup and utility scripts
│       ├── cloud-sql/     # Cloud SQL management
│       ├── personal-account/ # Account setup scripts
│       └── utils/         # Database setup utilities
├── docs/                  # Project documentation
│   ├── project_overview.md
│   ├── rubric.md
│   ├── instructions.md
│   └── Udacity_SETUP.md
└── memory/               # Development notes
    ├── progress.md
    └── tasks.md
```

## 🚀 Deployment

### Google Cloud Platform

1. **Set up Cloud Run service**
   ```bash
   gcloud run deploy betty-bird-agent \
     --source . \
     --region us-central1 \
     --allow-unauthenticated
   ```

2. **Configure environment variables in Cloud Run**
   - Set all required environment variables
   - Enable required APIs and services

3. **Set up monitoring and logging**
   - Enable Cloud Logging for debugging
   - Set up monitoring alerts for errors

### Local Development

```bash
# Start development server
python agent.py

# Or use ADK web interface
adk web
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints where appropriate
- Test all three tools in integration tests
- Update documentation for new features

## 📋 Requirements

### Core Dependencies
```
google-adk>=1.13.0
google-cloud-discoveryengine>=0.13.11
toolbox-core>=0.5.0
```

### System Requirements
- Python 3.8+
- Google Cloud Project with billing enabled
- Vertex AI API access
- MySQL database (local or Cloud SQL)

## 🔧 Troubleshooting

### Common Issues

**Agent not responding to database queries**
- Verify MCP Toolbox server is running
- Check database connection parameters in `.env`
- Validate `tools.yaml` configuration

**Vertex AI Search returning empty results**
- Confirm search engine ID and location
- Verify documents are uploaded and indexed
- Check service account permissions

**Web search tool failing**
- Validate Google Cloud credentials
- Ensure required APIs are enabled
- Check network connectivity

### Debug Mode

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Agent Development Kit** - Core agent framework
- **Gemini 2.5 Flash** - Language model powering the agent
- **MCP Toolbox** - Database integration tools
- **Vertex AI Search** - Document search capabilities
- **Udacity** - Project specification and guidance

## 📧 Contact

**Project Maintainer**: [Your Name](mailto:your.email@example.com)

**Project Repository**: [https://github.com/Imsharad/betty-bird-boutique](https://github.com/Imsharad/betty-bird-boutique)

---

> 🐦 **Betty's Bird Boutique** - *Where every bird finds their perfect home!*