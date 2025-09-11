### Network Security Project For Phising Data 

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green)](https://fastapi.tiangolo.com/)

## Project Overview

This project is a **machine learning pipeline for detecting phishing websites or URLs**. It automates the process from raw data ingestion to model training and prediction, allowing users to determine whether a URL is safe or phishing.

**Key Features:**

* Full ML pipeline: data ingestion → transformation → validation → model training
* Model evaluation using **accuracy, precision, recall, F1 score** (tracked in DagsHub)
* Batch and real-time predictions using **FastAPI**
* Logs and artifacts for reproducibility


**Install dependencies**


pip install -r requirements.txt


## Usage

### 1. Run Training Pipeline

python main.py
* Ingests, validates, transforms data, and trains the ML model
* Saves artifacts like `model.pkl`, `preprocessor.pkl`, and reports in `Artifacts/`



### 2. Real-time Prediction (FastAPI)


uvicorn app:app --reload
* Open `http://127.0.0.1:8000/docs` in your browser
* Input a file to see the prediction:

  * `1` → Phishing
  * `0` → Legitimate
* Results displayed in a table using `templates/table.html`

## Model Evaluation

* Metrics: **accuracy, precision, recall, F1 score**
* Logged and visualized in **DagsHub** for experiment tracking


## Project Flow

1. **Data Ingestion** → Load CSV and split data
2. **Data Transformation** → Preprocess features for ML
3. **Data Validation** → Ensure schema and data quality
4. **Model Training** → Train ML model and save artifacts
5. **Prediction** → Batch or real-time predictions
6. **Evaluation & Logging** → Metrics tracked via DagsHub

---

## Dependencies

* Python 3.10+
* pandas, numpy, scikit-learn
* FastAPI, uvicorn
* Jinja2 (for HTML templates)
