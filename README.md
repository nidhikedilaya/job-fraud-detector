# Job Fraud Detection System

An AI-powered tool to detect fraudulent job postings.

## How to Run

1. Train the model:

```bash
cd model_training
jupyter notebook train_model.ipynb
```

2. Start the backend:

```bash
cd ../backend
pip install -r requirements.txt
python app.py
```

3. Open `frontend/index.html` in your browser

## Input Fields

- title, description, requirements, company_profile, location
- salary_range, employment_type, industry, benefits
