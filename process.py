from binascii import a2b_base64
import numpy as np
import tensorflow as tf
from tensorflow import keras
import json

def pinger(data):
    binary = a2b_base64(data)

    with open("img.png", "wb") as f:
        f.write(binary)

def resize(img):
    image = tf.keras.preprocessing.image.load_img(img, color_mode="grayscale", target_size=(28, 28), interpolation="bilinear")
    return image

def to_json(img):
    package = json.dumps({
        "signature_name": "serving_default",
        "instances": img.tolist(),
    })
    return package

def predict(img):
    image = np.array(img)
    image = image.reshape([1, 28, 28])
    model = keras.models.load_model("digits/0002")
    return model.predict(image).argmax()