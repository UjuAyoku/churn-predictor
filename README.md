<a id="readme-top"></a>

<div align="center">
  <h1>Customer Churn Predictor</h1>
  <h3>A predictive tool that identifies at-risk telecom customers, enabling proactive retention strategies.</h3>
  
  [![Live Demo](https://img.shields.io/badge/Try-Live_Demo-green)]()

</div>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Frontend](https://img.shields.io/badge/Frontend-HTML5/CSS3/JS-FF5722?style=for-the-badge)
![Backend](https://img.shields.io/badge/Backend-Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Random_Forest-96%25_FI_Score-blueviolet)

<div align="center">
  <img src="https://via.placeholder.com/600x400?text=Churn+Predictor+Interface" alt="App Screenshot" width="400">
</div>

## Table of Contents
- [Business Impact](#business-impact)
- [Key Features](#key-features)
- [Prediction Interface](#prediction-interface)
- [Installation](#installation)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Feedback System](#feedback-system)

<a id="why-it-matters"></a>
## Why It Matters 💡

Customer churn costs telecom companies **millions of dollars annually**. This tool helps:
- Identify at-risk customers **before they leave**
- Reduce churn rate  
- Improve customer lifetime value
- Enable data-driven retention strategies

> "A 5% increase in retention can increase profits by 95%" - [Bain & Company](https://www.bain.com/insights/retaining-customers-is-the-real-challenge/)

<a id="key-features"></a>
- Real-time churn probability assessment
- User-friendly interface with dark/light mode toggle
- Feedback system to improve model accuracy
- Single-click predictions

<a id="prediction-interface"></a>
## Prediction Interface  

```python
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
```

<a id="installation"></a>
## Installation  

```bash
# Clone repository
git clone https://github.com/UjuAyoku/churn-predictor.git
```
# Install dependencies
```bash
pip install -r requirements.txt
```

# Launch application
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
| Component | Technology |
|-----------|-------------|
| Frontend | HTML5, CSS3, JavaScript  |
| Backend | Flask (Python)  |
| Machine Learning | scikit-learn Random Forest |
| Data Processing | Pandas, NumPy |
| Feedback Storage | OpenPyXL (Excel) |
| Deployment | Gunicorn WSGI Server |

<a id="feedback-system"></a>
Help improve the model by choosing the actual outcome from the drop down menu and submitting feedback.
User corrections are logged to feedback.xlsx with:
- Original prediction
- User-provided actual outcome
- Timestamp
- All input parameters
