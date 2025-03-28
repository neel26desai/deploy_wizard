import joblib

def run_inference(input_data):
    """
    This function takes input data, uses the trained model to make predictions,
    and returns the class predicted by the model.
    """
    try:
        # Load the trained model
        model = joblib.load('iris_model.pkl')

        # Perform inference on the input data
        prediction = model.predict([input_data])
        
        # Map the numeric prediction to the corresponding class name
        class_names = ['Setosa', 'Versicolor', 'Virginica']
        predicted_class = class_names[prediction[0]]

        return predicted_class

    except Exception as e:
        return f"Error occurred during inference: {str(e)}"
