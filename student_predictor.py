import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
data = pd.read_csv("student_data.csv")

print("\nDataset Preview:")
print(data.head())

# Define features and target
X = data[["Hours", "Attendance", "PreviousScore"]]
y = data["FinalScore"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()
model.fit(X_train, y_train)

# Save trained model (AFTER training)
joblib.dump(model, "student_model.pkl")

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
r2 = r2_score(y_test, predictions)

print("\nPredicted Scores:", predictions)
print("Actual Scores:", y_test.values)
print("R2 Score:", round(r2, 4))

# Visualization
plt.scatter(y_test, predictions)

# Perfect prediction reference line
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color='red')

plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores")
plt.show()

# Interactive prediction
print("\n--- Predict New Student Score ---")

while True:
    try:
        hours = float(input("Enter study hours: "))
        attendance = float(input("Enter attendance (%): "))
        previous = float(input("Enter previous score: "))
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

new_data = [[hours, attendance, previous]]
predicted_score = model.predict(new_data)

print("Predicted Final Score:", round(predicted_score[0], 2))