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
