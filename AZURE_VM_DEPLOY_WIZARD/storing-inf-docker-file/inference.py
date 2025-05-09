from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_iris

# Load the trained model
model = joblib.load('iris_model.pkl')

# Load the Iris dataset to get target names
iris = load_iris()

# Define the input data model
class InputData(BaseModel):
    input: list

# Initialize the FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Iris Classification Model API - Ready for Predictions!"}

@app.post("/predict")
def predict(data: InputData):
    try:
        # Extract the input data
        input_data = data.input

        # Ensure the input is in the correct format (array of 4 values)
        if len(input_data) != 4:
            raise HTTPException(status_code=400, detail="Invalid input format. Expected 4 features.")

        # Convert input to a NumPy array and predict
        prediction = model.predict([input_data]).tolist()
        class_name = iris.target_names[prediction[0]]

        return {"prediction": prediction[0], "class": class_name}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the FastAPI app, use the command:
# uvicorn script_name:app --host 0.0.0.0 --port 8000