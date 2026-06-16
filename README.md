# Salary Prediction API

An end-to-end Machine Learning project that predicts employee salaries based on education, experience, skills, certifications, job role, industry, company size, and location.

## Project Overview

This project demonstrates the complete Machine Learning lifecycle, from data preprocessing and feature engineering to model deployment through a FastAPI REST API.

The system accepts candidate information and returns a predicted salary using a trained Random Forest Regression model.

## Key Highlights

- Performed Exploratory Data Analysis (EDA)
- Created custom engineered features to improve model performance
- Built reusable preprocessing and feature engineering pipelines
- Compared Linear Regression and Random Forest Regression models
- Evaluated models using R² Score, MAE, and Cross Validation
- Selected Random Forest as the final model
- Serialized the complete pipeline using Joblib
- Developed a FastAPI application for real-time predictions
- Generated interactive API documentation using Swagger UI

## Tech Stack

### Machine Learning

- Python
- Pandas
- NumPy
- seaborn
- matplotlib
- Scikit-Learn

### API Development

- FastAPI
- Pydantic
- Uvicorn

### Model Serialization

- Joblib

## Machine Learning Workflow

```text
Raw Data
    ↓
Feature Engineering
    ↓
Encoding & Preprocessing
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Pipeline Serialization
    ↓
FastAPI Deployment
```

## Feature Engineering

Implemented custom feature engineering including:

- Total Experience
- Education Level Mapping
- Company Size Mapping
- Location Mapping
- Company-Location Composite Features

The feature engineering logic is integrated directly into the machine learning pipeline to ensure consistent behavior during both training and inference.

## Model Selection

### Models Evaluated

- Linear Regression
- Random Forest Regression

### Final Model

**Random Forest Regression** was selected as the final model based on superior predictive performance.

## API Endpoint

### Predict Salary

**POST** `/predict`

#### Sample Request

```json
{
  "job_title": "AI Engineer",
  "industry": "Health",
  "location": "India",
  "remote_work": "yes",
  "education_level": "Bachelor",
  "company_size": "Small",
  "experience_years": 5,
  "skills_count": 8,
  "certifications": 3
}
```

#### Sample Response

```json
{
  "predicted_salary": 79620.5
}
```

## Project Structure

```text
salary-prediction-api/
│
├── app.py
├── feature_engineering.py
├── salary_prediction_pipeline.pkl
├── Salary_Prediction.ipynb
├── requirements.txt
└── README.md
```

## Skills Demonstrated

- Data Analysis
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Pipelines
- Model Evaluation
- Random Forest Regression
- API Development with FastAPI
- Model Serialization using Joblib
- Production-Oriented Machine Learning Workflow

## Running the Project

### How to Run This Project Locally

 1. Clone the Repository
    - git clone https://github.com/khushilorish/salary-prediction-api.git
    - cd salary-prediction-api

3. Create a Virtual Environment (Optional)

python -m venv venv

Activate the environment:

# Windows

venv\Scripts\activate

# Mac/Linux

source venv/bin/activate

3. Install Required Dependencies

pip install -r requirements.txt

4. Start the FastAPI Server

uvicorn app:app --reload

You should see output similar to:

INFO: Application startup complete.
INFO: Uvicorn running on http://127.0.0.1:8000

5. Open API Documentation

Open your browser and visit:

http://127.0.0.1:8000/docs

Swagger UI will open automatically, allowing you to test the API directly from your browser.

6. Test Salary Prediction

Expand the POST /predict endpoint.

Click Try it out and provide sample input:

{
  "job_title": "AI Engineer",
  "industry": "Health",
  "location": "India",
  "remote_work": "yes",
  "education_level": "Bachelor",
  "company_size": "Small",
  "experience_years": 5,
  "skills_count": 8,
  "certifications": 3
}

Click Execute to receive a salary prediction.

# Key Learning 

Through this project, I gained hands-on experience with:

- End-to-end Machine Learning workflows

- Custom feature engineering using Scikit-Learn transformers

- Building reusable ML pipelines

- Model evaluation and selection

- Model serialization using Joblib

- REST API development with FastAPI

- Request validation using Pydantic

- API testing with Swagger UI

- Deploying machine learning models for real-world usage

# License
This project is licensed under the MIT License
