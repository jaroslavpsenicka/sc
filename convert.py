# import the libraries
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model('skin-lession-class_v1_10_0.673.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)

tflite_model = converter.convert()

with open('skin-lesion-class.tflite', 'wb') as f_out:
    f_out.write(tflite_model)