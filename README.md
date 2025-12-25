🏥 Diabetes Prediction System
An end-to-end machine learning application that predicts the likelihood of diabetes based on clinical parameters. The project features a FastAPI backend for model inference and a Streamlit frontend for a user-friendly interface, all fully containerized using Docker.

ML_PROJECT_/
├── Backend/
│   ├── main.py             # FastAPI Application
├── Frontend/
│   ├── app.py              # Streamlit Web Interface
├── model/
│   ├── gradient_boosting_model.pkl  # Trained Model (v1.6.1)
│   └── scaler.pkl                   # Standard Scaler (v1.6.1)
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Orchestration for Backend + Frontend
├── requirements.txt        # Python dependencies
└── .gitignore              # Files to exclude from Git

# 🚀 Getting Started
Prerequisites
Python 3.10+
Docker & Docker Compose (optional but recommended)


# Virtual Environment (venv)
. Local Setup (Without Docker)
Clone the repository:

 git clone <your-repo-url>
 cd ML_PROJECT_


python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

uvicorn Backend.main:app --reload

# Run the Frontend (Streamlit): Open a new terminal and run:

streamlit run Frontend/app.py

🐳 Docker Deployment
The easiest way to run the entire stack is using Docker Compose.

Build and Run
Bash

docker-compose up --build
Accessing the Services
Web App: http://localhost:8501

API Docs (Swagger): http://localhost:8000/docs


# Versioning Requirement
IMPORTANT: This model was trained using Scikit-learn version 1.6.1. To prevent InconsistentVersionWarning and ensure mathematical accuracy of predictions, the production environment must use the same version.

If you need to check your local version, run:

Bash

python -c "import sklearn; print(sklearn.__version__)"