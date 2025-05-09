from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

app = Flask(__name__)

# ---------------------------- #
# Step 1: Train the Iris Model
# ---------------------------- #
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, 'iris_model.pkl')

print("Model trained and saved as 'iris_model.pkl'")

# ---------------------------- #
# Step 2: Load the Model
# ---------------------------- #
model = joblib.load('iris_model.pkl')

# ---------------------------- #
# Step 3: Define the Flask API
# ---------------------------- #
@app.route('/')
def home():
    return "Iris Classification Model API - Ready for Predictions!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse the incoming JSON request
        data = request.json['input']

        # Ensure the input is in the correct format (array of 4 values)
        if len(data) != 4:
            return jsonify({"error": "Invalid input format. Expected 4 features."}), 400

        # Convert input to a NumPy array and predict
        prediction = model.predict([data]).tolist()
        class_name = iris.target_names[prediction[0]]

        return jsonify({"prediction": prediction[0], "class": class_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ---------------------------- #
# Step 4: Run the API
# ---------------------------- #
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
