from fastapi import FastAPI
from pydantic import BaseModel
from iris_inference import run_inference

app = FastAPI()

class InputData(BaseModel):
    data: list

@app.get("/")
def home():
    return {"message": "API is running. Use /predict to get predictions."}

@app.post("/predict")
def predict(input_data: InputData):
    result = run_inference(input_data.data)
    return {"prediction": result}
