# Fake Job Detector 🔍

## 📌 Project Overview

Fake Job Detector is a Machine Learning-based project designed to identify whether a job posting is potentially **Fake or Real**.

The project uses Machine Learning and Natural Language Processing (NLP) concepts to analyze job-related information and predict the authenticity of job postings.

The main objective is to help users identify potentially fraudulent job advertisements and make safer job application decisions.

## 🎯 Project Objectives

- Identify potentially fake job postings.
- Apply Machine Learning techniques to job-related data.
- Understand and implement NLP concepts.
- Build a user-friendly interface for predictions.
- Deploy the application using Docker.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Data Processing:** Pandas, NumPy
- **Web Framework:** FastAPI
- **Frontend:** HTML
- **Model Storage:** Pickle
- **Containerization:** Docker
- **Development Environment:** VS Code, Jupyter Notebook

## 📂 Project Structure

```text
NLP_ML/
│
├── app.py
├── index.html
├── ML_model.ipynb
├── model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dwivedikanha09-alt/Fake-Job-Post-Detector
```

### 2. Navigate to Project Folder

```bash
cd NLP_ML
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Project Locally

Start the FastAPI application:

```bash
uvicorn app:app --reload
```

Open the following URL in your browser:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## 🐳 Run Using Docker

### Step 1: Build Docker Image

```bash
docker build -t fake-job-detector .
```

### Step 2: Run Docker Container

```bash
docker run -d -p 8000:8000 --name fake-job-container fake-job-detector
```

### Step 3: Access Application

```text
http://localhost:8000
```

## 💡 Key Features

- Machine Learning-based job posting prediction.
- FastAPI backend integration.
- HTML-based user interface.
- Docker support for containerized execution.
- Simple project setup and execution.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning model development.
- Natural Language Processing concepts.
- Python programming.
- FastAPI application development.
- Model integration with a web application.
- Docker image building and container execution.
- Project development and GitHub version control.

## 🚀 Future Improvements

- Improve prediction accuracy through model optimization.
- Enhance the user interface.
- Add more job-related features for analysis.
- Deploy the application on a cloud platform.

