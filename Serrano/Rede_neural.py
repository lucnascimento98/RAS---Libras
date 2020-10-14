import tensorflow as tf
from tensorflow.keras.models import Sequential # Modelo Sequencial
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import numpy as np

pickle_in = open("X.pickle","rb")
X = np.array(pickle.load(pickle_in))

pickle_in = open("y.pickle","rb")
y = np.array(pickle.load(pickle_in))

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

# Layer de saída
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ['accuracy'])
model.fit(X, y, batch_size=32, epochs=3, validation_split=0.1)

model.save('treinando_rede.model') # Salvando Rede Neural