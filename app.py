from flask import Flask, render_template, request, redirect, url_for
import joblib
import numpy as np
import csv
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load('rf_churn_model.pkl')
# scaler = joblib.load('scaler.pkl')  # not required for Random Forest

# Dropdown options
contract_options = ['Month-to-month', 'One year', 'Two year']
internet_options = ['DSL', 'Fiber optic', 'No']

@app.route('/')
def home():
    return render_template('index.html', contracts=contract_options, internets=internet_options)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    contract = request.form['contract']
    internet = request.form['internet']
    tenure = float(request.form['tenure'])
    monthly = float(request.form['monthly'])
    total = float(request.form['total'])

    # One-hot encode categorical inputs
    contract_one = 1 if contract == 'One year' else 0
    contract_two = 1 if contract == 'Two year' else 0
    internet_fiber = 1 if internet == 'Fiber optic' else 0
    internet_none = 1 if internet == 'No' else 0

    # Scale numeric features only (last 3 columns),  *scaling not needed for Random Forest
    # input_data[:, 4:] = scaler.transform(input_data[:, 4:])
   
    # Order must match training
    input_data = np.array([[contract_one, contract_two, internet_fiber, internet_none,
                        tenure, monthly, total]])

    pred = model.predict(input_data)[0]
    result = "Likely to Churn" if pred == 1 else "Likely to Stay"

    #return render_template('result.html', prediction=result)
    return render_template('result.html', prediction=result, contract=contract,
                           internet=internet, tenure=tenure, monthly=monthly,
                           total=total, pred_value=pred)

@app.route('/feedback', methods=['POST'])
def feedback():
    # Collect feedback from form
    actual = request.form['actual']
    pred_value = request.form['pred_value']
    contract = request.form['contract']
    internet = request.form['internet']
    tenure = request.form['tenure']
    monthly = request.form['monthly']
    total = request.form['total']

    row = [contract, internet, tenure, monthly, total, pred_value, actual]

    # Append to CSV
    file_exists = os.path.isfile('feedback.csv')
    with open('feedback.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Contract', 'Internet', 'Tenure', 'Monthly', 'Total', 'Prediction', 'Actual'])
        writer.writerow(row)

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
