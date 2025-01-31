Here is an improved version of the Python script with logging, try-except blocks, and production-ready enhancements:

```python
import pickle
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_model(model_file):
    try:
        with open(model_file, 'rb') as f:
            model = pickle.load(f)
            logging.info("Model loaded successfully")
            return model
    except FileNotFoundError:
        logging.error("Model file not found")
    except Exception as e:
        logging.error(f"Error loading model: {e}")

def make_prediction(model, features):
    try:
        prediction = model.predict([features])
        logging.info("Prediction made successfully")
        return prediction
    except Exception as e:
        logging.error(f"Error making prediction: {e}")

if __name__ == "__main__":
    model_file = 'iris_model.pkl'
    model = load_model(model_file)

    if model:
        features = [5.1, 3.5, 1.4, 0.2]
        prediction = make_prediction(model, features)
        if prediction:
            print(prediction)
```

In this improved version:
- Logging is added to track the execution flow and any errors that occur.
- Try-except blocks are added for robust error handling during model loading and prediction making.
- The script is structured with functions for better organization and readability.
- The script is made production-ready by encapsulating the main logic in a `if __name__ == "__main__":` block.

You can further enhance the logging configuration based on your specific requirements and environment.