from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
model_filename = 'water_quality_combined_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get feature inputs from the form
        features = [float(request.form.get(feature)) for feature in [
            'ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 
            'Organic_carbon', 'Trihalomethanes', 'Turbidity'
        ]]
        final_features = np.array(features).reshape(1, -1)

        # Make prediction using the loaded model
        prediction = model.predict(final_features)
        output = prediction[0]
        
        # Determine if the water is safe to drink based on prediction
        if output == 1:  # Assuming '1' means safe to drink
            result = "The water is safe to drink."
        else:
            result = "The water is not safe to drink."
    
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
