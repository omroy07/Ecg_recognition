from flask import Flask, request, jsonify, send_from_directory
import tensorflow as tf
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained model (replace with your actual model path)
model = tf.keras.models.load_model('your_ecg_model.h5')

# Serve static HTML, CSS, and JS files from a folder
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Route to handle ECG image upload
@app.route('/upload_ecg', methods=['POST'])
def upload_ecg():
    try:
        # Ensure the file is provided
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Preprocess the image and make a prediction
        img = preprocess_image(file)
        prediction = model.predict(img)

        # ECG components and their cures
        components = ['N', 'P', 'Q', 'R', 'S']
        cures = {
            'N': "No cure necessary unless accompanied by other symptoms.",
            'P': "P-wave abnormalities may require lifestyle changes or medication.",
            'Q': "Q-wave anomalies can indicate previous heart attack, consult a doctor.",
            'R': "R-wave abnormalities need professional consultation.",
            'S': "S-wave abnormalities can signal ischemia, requires medical review."
        }

        # Find detected components based on model prediction
        detected_components = [
            components[i] for i in range(len(components)) if prediction[0][i] > 0.5
        ]

        # Prepare the response data
        result = [
            {
                'component': comp,
                'full_form': comp,
                'cure': cures.get(comp, "No specific cure needed.")
            }
            for comp in detected_components
        ]

        return jsonify({'predictions': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


# Helper function to preprocess image for prediction
def preprocess_image(image):
    # Open the image file using PIL
    img = Image.open(image)
    img = img.resize((224, 224))  # Adjust size based on model input
    img = np.array(img)
    img = img / 255.0  # Normalize the image
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Serve static files (CSS, JS, etc.)
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
