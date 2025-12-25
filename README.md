# 🏥 Diabetes Prediction System

An end-to-end machine learning application that predicts the likelihood of diabetes based on clinical parameters. This project features a **FastAPI** backend for model inference and a **Streamlit** frontend for a user-friendly interface, fully containerized using **Docker**.

---

## 📂 Project Structure

```text
ML_PROJECT_/
├── Backend/
│   ├── main.py             # FastAPI Application logic
├── Frontend/
│   ├── app.py              # Streamlit Web Interface
├── model/
│   ├── gradient_boosting_model.pkl  # Trained Model (v1.6.1)
│   └── scaler.pkl                   # Standard Scaler (v1.6.1)
├── Dockerfile              # Docker configuration for the API
├── docker-compose.yml      # Orchestration for Backend + Frontend
├── requirements.txt        # Python dependencies
└── .gitignore              # Files to exclude from Git
