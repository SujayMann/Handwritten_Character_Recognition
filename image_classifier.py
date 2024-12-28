import numpy as np
import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
import string

st.title('Image Classifier')

model = load_model('model.keras')
digits = [str(i) for i in range(10)]
uppercase = [i for i in string.ascii_uppercase]
lowercase = [i for i in string.ascii_lowercase]
class_names = digits + uppercase + lowercase

def predict_image(img_file):
    image = tf.keras.utils.load_img(img_file, target_size=(224, 224))
    input_arr = keras.utils.img_to_array(image)
    input_arr = tf.expand_dims(input_arr, axis=0)
    input_arr = input_arr / 255.0
    pred = model.predict(input_arr)
    class_index = np.argmax(pred, axis=1)[0]
    result = class_names[class_index]
    return result

def main():
    img_file = st.file_uploader(label='Character image', type=['png', 'jpg', 'jpeg'])
    if img_file is not None:
        st.image(img_file, width=256, caption=img_file.name)
        if st.button('Predict'):
            result = predict_image(img_file)
            st.write(f"Prediction: {result}")

if __name__ == '__main__':
    main()