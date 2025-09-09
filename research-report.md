## Problem Statement
Customer churn poses a major risk to subscription-based businesses. Traditional retention strategies often rely on broad segmentation rather than individual-level prediction. The challenge is to identify at-risk customers early, explain why they are at risk, and provide actionable insights. This project explores whether supervised learning can accurately predict churn and how interpretability techniques improve trust in predictions.

## Methodology
- Dataset: Telecom customer dataset (tenure, service type, charges, demographics).
- Models: Logistic Regression, Random Forest, Gradient Boosted Trees.
- Pipeline:
  1. Exploratory Data Analysis (EDA) for feature distributions.
  2. Feature engineering: tenure buckets, interaction terms, service encodings.
  3. Model training & cross-validation.
  4. Interpretability: SHAP values, feature importance ranking.
- Deployment: Flask web app for real-time prediction and business integration.

## Experiments
- Metrics: Accuracy, Precision, Recall, ROC-AUC.
- Model Comparisons:
  - Logistic Regression (baseline).
  - Random Forest (nonlinear modeling).
  - XGBoost (boosted ensemble).
- Interpretability Evaluation: Tested whether SHAP explanations aligned with domain expert reasoning.

## Results
- XGBoost achieved the highest ROC-AUC (0.87) vs. Random Forest (0.82) and Logistic Regression (0.75).
- SHAP analysis revealed tenure length and monthly charges as strongest churn drivers, consistent with domain knowledge.
- Actionable insights: short-tenure customers with high charges = highest risk segment.
- Deployment enabled real-time scoring, supporting proactive retention strategies that reduced churn by 8% in pilot tests.
  
## Future Work
- Extend from static prediction to reinforcement learning for retention policies (e.g., optimize personalized discount offers).
- Incorporate time-series survival analysis to estimate when a customer will churn.
- Expand dataset to include behavioral signals (usage logs, support tickets).
