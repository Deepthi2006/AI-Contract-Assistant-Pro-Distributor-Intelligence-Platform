# 📄 AI Contract Assistant Pro -- Distributor Intelligence Platform

An AI-powered contract intelligence application that uses
Retrieval-Augmented Generation (RAG) to analyze PDF contracts, extract
important information, generate summaries, identify deadlines, and
provide an interactive business intelligence dashboard.

## 1. Overview

****AI Contract Assistant Pro**** is a Streamlit-based
application designed to simplify the analysis of distributor agreements
and legal contracts.

The application combines:
- Large Language Models (LLMs) through Groq.
- Hugging Face sentence embeddings.
- Retrieval-Augmented Generation (RAG).
- A custom NumPy-based vector database.
- Automated contract summarization.
- Contract expiration and renewal alerts.
- Interactive executive dashboard and document comparison.
Users can upload PDF contracts, process them, ask questions about their
documents, and retrieve relevant contractual information.

## 2. Key Features

| Feature | Description |

|---|---|

| 💬 Chat Assistant | Ask questions about processed contracts using
RAG. |

| 📰 Contract Summarizer | Extract margins, service timelines,
expiration dates, unusual clauses, and selling rights. |

| 🚨 Contract Alerts | Identify expiration and renewal dates and
calculate days remaining or overdue status. |

| 📊 Executive Dashboard | View portfolio-level contract analytics and
visualizations. |

| 🆚 Document Comparison | Compare summaries of two selected contracts.
|

| 💰 Profit Optimizer | Explore distributor profitability-related
dashboard insights. |

| 🔄 Document Processing | Extract PDF text, generate embeddings, and
build the vector database. |

| 🔍 Duplicate Detection | Use SHA256 content hashing to identify
duplicate PDF content during processing. |

## 3. Technology Stack

| Component | Technology |

|---|---|

| Frontend | Streamlit |

| Programming Language | Python 3.11 (Streamlit Cloud deployment) |

| LLM Provider | Groq API |

| LLM Model | openai/gpt-oss-20b |

| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |

| AI Orchestration | LangChain |

| Vector Database | Custom NumPy-based VectorDB |

| PDF Extraction | PyMuPDF |

| Similarity Search | Cosine Similarity |

| Data Processing | Pandas, NumPy |

| Visualization | Plotly |

| Environment Configuration | python-dotenv |

## 4. Project Architecture

                 USER

                   |

                   v

          STREAMLIT FRONTEND

                app.py

                   |

          +--------+---------+

          |                  |

          v                  v

     PDF UPLOAD          USER QUERY

          |                  |

          v                  v

    PyMuPDF Extraction   Query Embedding

          |                  |

          v                  v

    Text Chunking       VectorDB Search

          |                  |

          v                  v

    Hugging Face        Relevant Chunks

    Embeddings               |

          |                  |

          v                  |

      CUSTOM VECTOR DATABASE

          |                  |

          +--------+---------+

                   |

                   v

              RAG PIPELINE

                   |

                   v

                GROQ LLM

                   |

          +--------+---------+

          |        |         |

          v        v         v

       Answers  Summaries  Insights

                   |

                   v

             STREAMLIT UI
## 5. Project Structure

AI-Contract-Assistant-Pro/

│

├── app.py                  # Main Streamlit application

├── dashboard.py            # Dashboard and visualization logic

├── requirements.txt        # Python dependencies

├── README.md               # Project documentation

├── .env                    # API credentials (not committed)

├── .env.example            # Environment variable template

├── .gitignore              # Git ignored files

│

├── source_documents/       # Uploaded PDF contracts

│

├── multi_document_db/      # Generated vector database

│

├── summary/                # Generated contract summaries

│

└── venv/                   # Python virtual environment
Generated folders and the virtual environment are created or maintained
locally and should not be committed to GitHub.

## 6. Prerequisites

Before running the application, install:
1. Python 3.11 (used for the Streamlit Community Cloud deployment).
2. Git.
3. Visual Studio Code or another Python IDE.
4. A Groq API key.
Get your API key from:

https://console.groq.com/keys

## 7. Installation and Setup

### Step 1: Clone the repository

git clone https\://github.com/Deepthi2006/AI-Contract-Assistant-Pro-Distributor-Intelligence-Platform.git
Navigate into the project:

cd AI-Contract-Assistant-Pro-Distributor-Intelligence-Platform
### Step 2: Create a virtual environment

python -m venv venv
### Step 3: Activate the environment

****Windows PowerShell:****

.\venv\Scripts\Activate.ps1
****Windows Command Prompt:****

venv\Scripts\activate
### Step 4: Install dependencies

Upgrade pip:

python -m pip install --upgrade pip
Install all project dependencies:

pip install -r requirements.txt
### Step 5: Configure the Groq API key

Create a `.env` file in the project root.

You can copy the example file:

Copy-Item .env.example .env
Add your Groq API key:

GROQ_API_KEY=your_actual_groq_api_key
****Important:**** Never upload your `.env` file or expose
your API key in GitHub.

### Step 6: Run the application

streamlit run app.py
Open your browser and navigate to:

http://localhost:8501

## 8. How to Use the Application

### Step 1: Upload PDF Documents
1. Open the application.
2. Locate the Controls section in the sidebar.
3. Upload one or more PDF contracts.
4. Uploaded files are stored in the `source_documents` directory.
### Step 2: Process Documents

Click:

****🔄 Process New Documents (Rebuild)****

The application will:
1. Extract text from PDF documents using PyMuPDF.
2. Split extracted text into smaller chunks.
3. Generate embeddings using Hugging Face.
4. Store document vectors and metadata in the custom VectorDB.
5. Generate structured summaries using Groq.
6. Save summaries in the `summary` directory.
### Step 3: Explore the Modules

****💬 Chat Assistant****

Ask questions about your processed contracts. The application retrieves
relevant document chunks and passes them to the Groq LLM to generate
contextual answers.

****📰 Summarizer****

View extracted information about:
- Distributor margins.
- Service timelines and SLAs.
- Expiration and renewal dates.
- Unusual contractual clauses.
- Selling rights and territories.
****🚨 Alerts****

Review contract expiration and renewal dates, including:
- Upcoming deadlines.
- Days remaining.
- Past-due contracts.
- Due-today notifications.
****📊 Executive Dashboard****

Explore contract portfolio analytics and visualizations.

****🆚 Compare Documents****

Select two processed contracts to view their summaries side by side.

****💰 Profit Optimizer****

Explore profitability-related dashboard insights.

## 9. Important Notes

### Running the application again

Once the initial setup and dependency installation are complete, you do
not need to install the packages every time.

On your existing Windows laptop:

cd path\to\AI-Contract-Assistant-Pro

.\venv\Scripts\Activate.ps1

streamlit run app.py
Open:

http://localhost:8501

### Hugging Face Model Download

The first execution may download the embedding model. Subsequent
executions can reuse the locally cached model.

### Groq API Rate Limits

Groq applies token-per-minute and other usage limits depending on the
account and model.

If a `429 RateLimitError` occurs:
- Wait for the retry interval indicated in the error.
- Avoid repeatedly clicking the rebuild button.
- Process fewer documents at a time.
- Reduce unnecessary LLM requests.
### Important: Rebuild Behavior

The current Rebuild implementation deletes the existing
`multi_document_db` and `summary` directories before rebuilding the
database.

Therefore:
- Back up important generated data before rebuilding.
- Do not click Rebuild simply to restart the application.
- Normal application restarts can load the saved database if it
  exists.
## 10. Troubleshooting

| Error | Possible Solution |

|---|---|

| `ModuleNotFoundError` | Activate the virtual environment and
install `requirements.txt`. |

| `GROQ_API_KEY missing` | Check the `.env` file and its location.
|

| `RateLimitError: 429` | Wait for the specified interval and reduce
requests. |

| `404 model_not_found` | Verify that the configured Groq model is
available to your account. |

| `Connection error` | Check internet connectivity and API
configuration. |

| `No documents found` | Upload PDF files and process them. |

| `Port 8501 already in use` | Stop the existing Streamlit process or
use another port. |

## 11. Updating the Project

To get the latest code from GitHub:

git pull origin main
If dependencies have changed:

pip install -r requirements.txt
Then restart:

streamlit run app.py
**## 12. Deployment Status

Live application:
https://ai-contract-assistant-pro-distributor-intelligence-platform-new.streamlit.app/

The application is deployed using Streamlit Community Cloud and the
source code is hosted on GitHub:
- Repository:
  https://github.com/Deepthi2006/AI-Contract-Assistant-Pro-Distributor-Intelligence-Platform
- Branch: main
- Entry point: app.py
- Python version selected in Streamlit app settings: 3.11
Free deployment setup (repeatable checklist)
1. Push the latest project files to the main branch on GitHub.
2. Open Streamlit Community Cloud and choose Create app.
3. Select the GitHub repository
   Deepthi2006/AI-Contract-Assistant-Pro-Distributor-Intelligence-Platform.
4. Select branch main and main file path app.py.
5. In App settings → General, select Python 3.11.
6. In App settings → Secrets, enter the Groq key in valid TOML
   format. Use one line, with the value inside double quotes:
   GROQ_API_KEY = "your_groq_api_key_here"
7. Save the secrets and wait for Streamlit to restart the app.
8. Open the app URL and test the dashboard, PDF upload, document
   processing, and chat.
Important: Do not paste the example placeholder as a real key. Do
not add a real API key to README.md, GitHub, screenshots, or source
code. If a key has been exposed, revoke it in the Groq console and
create a replacement.
Deployment troubleshooting notes
  Problem                                     What to check
  No solution found for torch==2.2.2 with The deployment was using Python 3.14, for
cp314                                     which this pinned Torch version has no
compatible wheel. Set the app's Python
version to 3.11 and reboot/redeploy.

  Invalid format: please enter valid TOML   Use
GROQ_API_KEY = "your_groq_api_key_here"
on one line. TOML requires the key name,
equals sign, and quoted string value.

  App shows an error after deployment         Open Manage app → Logs and inspect the
first Python traceback/error above the
repeated health-check messages.

  503 GET /script-health-check              This indicates the app process is not
responding to the health check. Check the
app's startup/runtime logs; repeated 503s
are symptoms, not the underlying Python
exception.
Groq 429 RateLimitError                   Wait for the retry interval, avoid repeated
rebuild clicks, and process fewer documents
or reduce LLM calls.
Important cloud-hosting limitations
- Streamlit Community Cloud and Groq offer free usage options subject
  to their current quotas, limits, and availability; this is not a
  guarantee of unlimited usage or permanent uptime.
- This application currently writes uploaded PDFs, summaries, and its
  custom vector database to local folders (source_documents/,
  summary/, and multi_document_db/). Cloud runtime storage may be
  temporary and may be lost after a restart, redeploy, or app rebuild.
  Do not rely on it as permanent storage.
- The app does not currently provide authentication or per-user
  document isolation. For a public demo, use sample or
  non-confidential contracts only. Do not upload private customer
  contracts or sensitive legal documents.
- The first startup can take longer because the Hugging Face embedding
  model may need to download and initialize.
13. Future Improvements**
- Incremental document processing.
- Improved API rate-limit handling and retry mechanisms.
- More advanced contract risk detection.
- Persistent and scalable vector database storage.
- Multi-user authentication and access control.
- Cloud deployment and Docker containerization.
- Advanced contract analytics and reporting.
## 14. Author

****Deepthi V****

AI & Data Science

Karpagam College of Engineering

GitHub: https://github.com/Deepthi2006
****AI Contract Assistant Pro -- Transforming Contract Documents
into Actionable Intelligence.****
15. Quick Reference: Run Locally Next Time
Open PowerShell in the project folder and run:
cd D:\projects\AI-Contract-Assistant-Pro-Distributor-Intelligence-Platform-main
.\venv\Scripts\Activate.ps1
streamlit run app.py
You do not need to reinstall dependencies every time. Install them again
only if requirements.txt changes or the virtual environment is
recreated:
pip install -r requirements.txt
16. Quick Reference: Push Updates to GitHub
After editing files, check what changed:
git status
Stage and commit the files you intend to publish (never stage .env):
git add README.md app.py dashboard.py requirements.txt .gitignore .env.example
git commit -m "Describe your update"
git push origin main
Streamlit Community Cloud will detect the GitHub update and rebuild the
deployed app. If it does not, open the app's management menu and reboot
the app.
AI Contract Assistant Pro -- Transforming Contract Documents into
Actionable Intelligence.