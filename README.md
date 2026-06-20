# Salary Prediction API

A Machine Learning API that predicts employee salaries based on professional, educational, and company-related information.

The project is built using FastAPI and Scikit-Learn and deployed on Hugging Face Spaces using Docker.

---

## Project Objective

Salary estimation is an important problem for both job seekers and employers.

This project uses Machine Learning to estimate a person's salary based on factors such as:

- Job Title
- Industry
- Location
- Remote Work Status
- Education Level
- Company Size
- Years of Experience
- Number of Skills
- Certifications

The trained model is exposed through a REST API so predictions can be accessed from any application.

---

## Technologies Used

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Joblib

### API Development

- FastAPI
- Pydantic
- Uvicorn

### Deployment

- Docker
- Hugging Face Spaces

---

## Project Structure

```text
salary-prediction-api/
│
├── app.py
├── feature_engineering.py
├── salary_prediction_pipeline.pkl
├── requirements.txt
├── Dockerfile
├── code.ipynb
├── README.md
└── LICENSE
```

### File Description

| File | Purpose |
|--------|---------|
| app.py | Main FastAPI application |
| feature_engineering.py | Custom feature engineering logic |
| salary_prediction_pipeline.pkl | Trained machine learning pipeline |
| requirements.txt | Python dependencies |
| Dockerfile | Docker deployment configuration |
| code.ipynb | Model development notebook |

---

## How the System Works

```text
User Input
     ↓
FastAPI Endpoint
     ↓
Feature Engineering
     ↓
Machine Learning Pipeline
     ↓
Salary Prediction
     ↓
JSON Response
```

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
    "message": "Salary Prediction API is running"
}
```

---

### Prediction Endpoint

```http
POST /predict
```

Request Example:

```json
{
  "job_title": "AI Engineer",
  "industry": "Technology",
  "location": "USA",
  "remote_work": "Yes",
  "education_level": "Master",
  "company_size": "Large",
  "experience_years": 5,
  "skills_count": 10,
  "certifications": 3
}
```

Response Example:

```json
{
  "predicted_salary": 125000.45
}
```

---

# Using the Deployed API

You can use the deployed version directly without downloading the repository.

Open:

https://khushilorish-salary-prediction-api.hf.space/docs

Steps:

1. Open the Swagger documentation.
2. Expand the `/predict` endpoint.
3. Click **Try it out**.
4. Enter sample JSON data.
5. Click **Execute**.
6. View the predicted salary in the response.

---

# Run the Project Locally

## Step 1: Clone the Repository

```bash
git clone https://github.com/khushilorish/salary-prediction-api.git
```

Move into the project directory:

```bash
cd salary-prediction-api
```

---

## Step 2: Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Start FastAPI Server

```bash
uvicorn app:app --reload
```

You should see output similar to:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

## Step 5: Open API Documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

You can now test the API locally.

---

# Run with Docker

Build Docker Image:

```bash
docker build -t salary-prediction-api .
```

Run Container:

```bash
docker run -p 7860:7860 salary-prediction-api
```

Open:

```text
http://localhost:7860/docs
```

---

# Example Use Cases

- HR Analytics
- Salary Benchmarking
- Recruitment Platforms
- Career Guidance Systems
- Compensation Analysis
- Educational Projects
- Machine Learning API Learning

---

# Repository

GitHub Repository:

https://github.com/khushilorish/salary-prediction-api

---

# Live Demo

https://khushilorish-salary-prediction-api.hf.space/docs

---

GitHub:
https://github.com/khushilorish
