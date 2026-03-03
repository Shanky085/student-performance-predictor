from flask import Flask, request, render_template_string
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
import csv
import os

app = Flask(__name__)

# Load model
model = joblib.load("student_model.pkl")

# Load dataset to calculate performance
data = pd.read_csv("student_data.csv")
X = data[["Hours", "Attendance", "PreviousScore"]]
y = data["FinalScore"]

predictions_full = model.predict(X)
r2 = round(r2_score(y, predictions_full), 4)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Score Predictor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container mt-5">
    <div class="card shadow p-4">

        <h2 class="text-center mb-3">📊 Student Performance Predictor</h2>

        <div class="alert alert-info text-center">
            <strong>Model R² Score:</strong> {{ r2 }}
        </div>

        <form method="post">
            <div class="mb-3">
                <label class="form-label">Study Hours</label>
                <input type="number" step="any" class="form-control" name="hours" required>
            </div>

            <div class="mb-3">
                <label class="form-label">Attendance (%)</label>
                <input type="number" step="any" class="form-control" name="attendance" required>
            </div>

            <div class="mb-3">
                <label class="form-label">Previous Score</label>
                <input type="number" step="any" class="form-control" name="previous" required>
            </div>

            <button type="submit" class="btn btn-primary w-100">Predict</button>
        </form>

        {% if prediction %}
        <div class="alert alert-success mt-4 text-center">
            <h4>Predicted Final Score: {{ prediction }}</h4>
        </div>
        {% endif %}

    </div>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        hours = float(request.form["hours"])
        attendance = float(request.form["attendance"])
        previous = float(request.form["previous"])

        input_data = np.array([[hours, attendance, previous]])
        prediction = round(model.predict(input_data)[0], 2)

        # Save history
        file_exists = os.path.isfile("prediction_history.csv")

        with open("prediction_history.csv", "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Hours", "Attendance", "PreviousScore", "PredictedScore"])
            writer.writerow([hours, attendance, previous, prediction])

    return render_template_string(HTML, prediction=prediction, r2=r2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)