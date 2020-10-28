import tensorflow as tf
import cv2
import keras
import matplotlib.pyplot as plt
import numpy as np
import os

CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"] #Possibilidades de estudo


def prepare(filepath):
    IMG_SIZE = 64  # 50 in txt-based
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = tf.keras.models.load_model("RAS---Libras\\output\\treinando_rede_all.model")

prediction = model.predict([prepare('Letra.jpg')]) # Quando usar Predict -> Deve ser uma lista
print(prediction)  # will be a list in a list.
valor = np.where(prediction==1)
print(CATEGORIES[int(valor[1])])