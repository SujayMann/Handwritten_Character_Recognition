import tensorflow as tf
import numpy as np
from keras.models import load_model
from flask import Flask, request, render_template
import os
import string

app = Flask(__name__)

# Load the Keras model
model = load_model('model.keras')
digits = [str(i) for i in range(10)]
uppercase = [i for i in string.ascii_uppercase]
lowercase = [i for i in string.ascii_lowercase]
class_names = digits + uppercase + lowercase


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('index.html', prediction_text="No file part in the request.")
    
    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', prediction_text="No file selected.")

    if file:
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        img = tf.io.read_file(filepath)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.resize(img, [256, 256])
        img_array = tf.expand_dims(img, axis=0)

        prediction = model.predict(img_array)
        class_index = np.argmax(prediction, axis=1)[0]

        os.remove(filepath)

        return render_template('index.html', prediction_text=f'Prediction: {class_names[class_index]}')
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
