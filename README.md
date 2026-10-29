
# California House Price Prediction

## Project Overview
This project predicts median house values in California using a
Machine Learning model based on Linear Regression.

The model is trained using the California Housing dataset from
Scikit-learn and deployed as a web application using Flask.

## Live Demo

Try the deployed application here: https://california-house-price-prediction-56co.onrender.com

## Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Flask
- HTML and CSS
- Joblib


## Project Structure

```text
California_house_prediction/
├── artifacts/
│   └── linear_regression_model.pkl
├── templates/
│   └── index.html
├── California_Housing.ipynb
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Model
Algorithm: Linear Regression

Evaluation metrics:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

## Run Locally

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
     pip install -r requirements.txt


4. Start the Flask application:
   python app.py


5. Open http://127.0.0.1:5000 in your browser.

## Disclaimer
Predictions are estimates based on a trained model and are not
professional property valuations.
