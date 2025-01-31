from flask import Flask, request, jsonify
import pickle
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Flask application
app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = "iris_model.pkl"
try:
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
        logger.info("Model loaded successfully.")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    raise

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to make predictions on input data.
    """
    try:
        # Get JSON data
        data = request.get_json()
        if not data or 'features' not in data:
            raise ValueError("Invalid input: 'features' key missing.")
        
        # Extract features and make predictions
        features = data['features']
        prediction = model.predict([features])
        
        # Log the request and prediction
        logger.info(f"Prediction made for input: {features}, result: {prediction}")
        
        # Return the prediction
        return jsonify({'prediction': prediction.tolist()})
    
    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == "__main__":
    app.run(debug=True)
