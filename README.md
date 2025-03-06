# Customer Churn Prediction - Streamlit App

This Streamlit-based web application predicts customer churn using a trained Artificial Neural Network (ANN) model.

## Features
- User-friendly interface for entering customer details.
- Uses a pre-trained deep learning model to predict churn.
- Standardizes inputs using a pre-fitted scaler before making predictions.

## Preview
![image](https://github.com/user-attachments/assets/f3442bd1-d39e-4693-adf2-f8dbba167f35)
![image](https://github.com/user-attachments/assets/b774e980-6786-44d3-8e3f-69bede05d8e1)



## Requirements
Ensure you have the following installed:

- Python 3.7+
- Streamlit
- TensorFlow
- NumPy
- Pandas
- Scikit-learn
- Joblib

## Installation
1. Clone this repository or download the files.
2. Install dependencies using:
   ```bash
   pip install streamlit tensorflow numpy pandas scikit-learn joblib
   ```
3. Ensure you have the trained model file (`churn_model.h5`) and scaler (`scaler.pkl`) in the same directory.

## Running the App
Start the Streamlit app by running:
```bash
streamlit run streamlit_churn_app.py
```

## Usage
1. Enter customer details into the provided input fields.
2. Click on the "Predict Churn" button.
3. The app will display whether the customer is likely to churn or not.

## Notes
- The model was trained on the `Churn_Modelling.csv` dataset.
- The input data is standardized using `StandardScaler` before making predictions.
- Ensure `churn_model.h5` and `scaler.pkl` are available before running the app.

## Author
This application was built for churn prediction using deep learning with Streamlit.

