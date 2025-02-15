from flask import Flask, request, jsonify
import pickle
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add a file handler to log to a file
file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Flask application
app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = "iris_model.pkl"
model = None  # Initialize model variable
try:
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
        logger.info("Model loaded successfully.")
except FileNotFoundError:
    logger.error(f"Model file '{MODEL_PATH}' not found. Please ensure it exists.")
except Exception as e:
    logger.error(f"Error loading model: {e}")

@app.route("/")
def home():
    """ Home endpoint to check if the API is running """
    return "Flask API is running! Use /predict to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to make predictions on input data.
    """
    try:
        # Check if model is loaded
        if model is None:
            return jsonify({'error': 'Model is not loaded. Check server logs.'}), 500

        # Get JSON data
        data = request.get_json()
        if not data or 'features' not in data:
            raise ValueError("Invalid input: 'features' key missing.")
        
        features = data['features']

        # Validate input type
        if not isinstance(features, list) or len(features) != 4:
            raise ValueError("Invalid input: Expected a list with 4 features.")

        # Make prediction
        prediction = model.predict([features])
        
        # Log the request and prediction
        logger.info(f"✅ Prediction made for input: {features}, result: {prediction}")
        
        return jsonify({'prediction': prediction.tolist()})

    except ValueError as ve:
        logger.error(f"❌ ValueError: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000)
    except Exception as e:
        logger.exception("❌ Error during startup")
