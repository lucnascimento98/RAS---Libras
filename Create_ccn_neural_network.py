import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential # Modelo Sequencial
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard # Para visualização do Modelo da Rede Neural

import time

DATADIR = "dataset\\training" #Onde estão sendo armazenados os arquivos
CATEGORIES = ["A","B","C","D","E","F","G","I","L","M","N","O","P","Q","R","T","U","V","W","Y"] #Possibilidades de estudo

training_data = []
IMG_SIZE = 64

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR,category) # Caminho com os diretórios das letras
        class_num = CATEGORIES.index(category) # Dando um número para a categoria
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE) #Cada imagem também é convertida na escala de cinza
                new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE)) #Redimensionando a imagem
                training_data.append([new_array,class_num]) #Inserindo a imagem e sua classificação
            except Exception as e: #Erro que pode ocorrer ao importar imagens
                pass

create_training_data()

import random
random.shuffle(training_data) #Embaralhando os dados que a rede vai usar para treinar

X = [] # Features
y = [] # Labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) # -1: Quantas features tem, IMG_SIZE x IMG_SIZE: tamanho da imagem, 1: indica que o canal de cores é só o cinza (3 se RGB)

#####################################################################################################################

NAME = 'Verificação_de_letras-cnn-64x2-{}'.format(int(time.time()))

tensorboard = TensorBoard(log_dir = 'logs/{}'.format(NAME)) # Para ter uma visualização do treinamento da rede neural

X = np.array(X/255.0) #Simplificando coloração de Pixels para valores entre 0 e 1

# Primeira Layer
model = Sequential()
model.add(Conv2D(64,(3,3), input_shape = X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# Segunda Layer
model = Sequential()
model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

# Terceira Layer
model.add(Flatten()) #Deixa a rede neural em 2D
model.add(Dense(64))
model.add(Activation('relu'))

# Layer de saída
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ['accuracy'])
model.fit(X, y, batch_size=32, epochs=10, validation_split=0.1, callbacks = [tensorboard])

model.save('treinando_rede.model') # Salvando Rede Neural