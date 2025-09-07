<a id="readme-top"></a>

<div align="center">
  <h1>Customer Churn Predictor</h1>
  <h3>A predictive tool that identifies at-risk telecom customers, enabling proactive retention strategies.</h3>
  
[![Live Demo](https://img.shields.io/badge/Try-Live_Demo-green)]()

</div>
<p align="center">
  <img src="https://github.com/UjuAyoku/churn-predictor/blob/main/churn.PNG" alt="Logo" width="280">
</p>

## Table of Contents
- [Business Impact](#business-impact)
- [Key Features](#key-features)
- [Prediction Interface](#prediction-interface)
- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Feedback System](#feedback-system)

<a id="why-it-matters"></a>
## Why It Matters  

Customer churn costs telecom companies **millions of dollars annually**. This tool helps:
- Identify at-risk customers before they leave to reduce churn rate  
- Improve customer lifetime value
- Enable data-driven retention strategies

> "A 5% increase in retention can increase profits by 95%" - [Bain & Company](https://www.bain.com/insights/retaining-customers-is-the-real-challenge/)

<a id="key-features"></a>
## Features
- Real-time churn probability assessment
- User-friendly interface with dark/light mode toggle
- Feedback system to improve model accuracy
- Single-click predictions

<a id="prediction-interface"></a>
## App Interface  

1. Select from dropdown menus:
   - Contract Term
   - Internet Service Type
   - Tenure Length
2. Enter numerical values:
   - Monthly Charges ($)
   - Total Charges ($)
3. Click "Predict" to get:
   - "Likely to Stay" or 
   - "Likely to Churn"
4. Provide feedback if actual outcome is known


<a id="installation"></a>
## Installation  

```bash
# Clone repository
git clone https://github.com/UjuAyoku/churn-predictor.git
```
#### Install dependencies
```bash
pip install -r requirements.txt
```

#### Launch application
```bash
streamlit run app.py
```

<a id="usage"></a>
## Usage
1. Select customer parameters from dropdowns
2. Enter numerical values (tenure, charges)
3. Click "Predict" for instant analysis
4. (Optional) Provide feedback via toggle
5. View prediction: "Likely to Churn" or "Likely to Stay"

<a id="technology-stack"></a>
## Tech Stack
| Component | Technology |
|-----------|-------------|
| Frontend | HTML5, CSS3, JavaScript  |
| Backend | Flask (Python)  |
| Machine Learning | scikit-learn Random Forest |
| Data Processing | Pandas, NumPy |
| Feedback Storage | OpenPyXL (Excel) |
| Deployment | Gunicorn WSGI Server |

<a id="feedback-system"></a>
## Feedback System
Help improve the model by choosing the actual outcome from the drop down menu and submitting feedback.
User corrections are logged to feedback.xlsx with:
- Original prediction
- User-provided actual outcome
- Timestamp
- All input parameters
