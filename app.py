
from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load("artifacts/linear_regression_model.pkl")


@app.route("/")
def home():
    return render_template("index.html", prediction=None, error=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from the HTML form
        features = {
            "MedInc": float(request.form["MedInc"]),
            "HouseAge": float(request.form["HouseAge"]),
            "AveRooms": float(request.form["AveRooms"]),
            "AveBedrms": float(request.form["AveBedrms"]),
            "Population": float(request.form["Population"]),
            "AveOccup": float(request.form["AveOccup"]),
            "Latitude": float(request.form["Latitude"]),
            "Longitude": float(request.form["Longitude"])
        }

        # Keep features in the same order as the training data
        input_data = pd.DataFrame([features])

        # Predict house value
        prediction = float(model.predict(input_data)[0])
        predicted_dollars = prediction * 100000

        return render_template(
            "index.html",
            prediction=predicted_dollars,
            error=None
        )

    except (ValueError, KeyError) as e:
        return render_template(
            "index.html",
            prediction=None,
            error="Please enter valid numeric values for all fields."
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)


