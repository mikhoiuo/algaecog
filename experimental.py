from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io
from classify import predict_algae
from keras.models import load_model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    
    # Get the image data from the request
    image_data = request.get_data()

    # Load the image data into a Pillow Image object
    image = Image.open(io.BytesIO(image_data))

    # Check if the image is in a supported format (JPG or PNG)
    if image.format not in ['JPEG', 'PNG']:
        return jsonify({'success': False, 'error': 'Unsupported image format'})

    # Convert the image to PNG if it's in JPG format
    if image.format == 'JPEG':
        image = image.convert('RGB')
        image.save('image.png', 'PNG')
        image = Image.open('image.png')

    # Preprocess the image
    image_array = np.array(image)
    image_array = np.expand_dims(image_array, axis=0)

    prediction = predict_algae(image_array)

    return jsonify({'success': True, 'prediction': prediction.tolist()})

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=8000)
#    app.run(host='<host>', port=<port>, debug=True)
