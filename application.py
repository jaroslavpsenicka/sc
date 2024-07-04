from flask import Flask, request, jsonify
import tflite_runtime.interpreter as tflite
from PIL import Image
from io import BytesIO
import numpy as np

app = Flask(__name__)

# Actinic keratoses and intraepithelial carcinomae
# Basal cell carcinoma
# Benign keratosis-like lesions
# Dermatofibroma
# Melanoma
# Melanocytic nevi
# Pyogenic granulomas and hemorrhage
classes = np.array(['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc'])

interpreter = tflite.Interpreter(model_path='skin-lesion-class.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

# # Function to load and preprocess the image
def load_and_preprocess_image(image_data):
    image = Image.open(BytesIO(image_data))
    image = image.resize((150, 150))  # Resize image to match model input size
    image = np.array(image) / 255.0   # Normalize pixel values to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image


@app.route('/', methods=['GET'])
def main():
    return jsonify({"status": "OK"}), 200


@app.route('/', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image_file = request.files['image']
    image_data = image_file.read()

    try:
        preprocessed_image = load_and_preprocess_image(image_data)
        interpreter.set_tensor(input_index, np.float32(preprocessed_image))
        interpreter.invoke()
        preds = interpreter.get_tensor(output_index)
        return jsonify({
            'akiec': float(preds[0][0]), 
            'bcc': float(preds[0][1]), 
            'bkl': float(preds[0][2]), 
            'df': float(preds[0][3]), 
            'mel': float(preds[0][4]), 
            'nv': float(preds[0][5]), 
            'vasc': float(preds[0][6])
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
