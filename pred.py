import numpy as np
import pandas as pd
from config import Brands
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

def to_categorical(brand):
    return np.array([b==brand for b in Brands],dtype="int")

df = pd.read_csv("survey.processed.csv")
dlen = len(df)
x_train = np.zeros((dlen,10),dtype="int")
y_train = np.zeros((dlen,8))

x_train[:] = df.iloc[:,9:19]
y_train[:] = [to_categorical(brand) for brand in df["brand"]]

model = Sequential()
model.add(keras.Input(shape=(10,)))
model.add(layers.Dense(16,activation="relu"))
model.add(layers.Dense(8))

model.compile(optimizer='Adam')
model.fit(x_train, y_train, epochs=5, batch_size=20)
model.summary()
model.save("model.h5")
