import pickle

# Load model
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make prediction
features = [5.1, 3.5, 1.4, 0.2]
print(model.predict([features]))
