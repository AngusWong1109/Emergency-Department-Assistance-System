from calendar import c
from tabnanny import verbose
from matplotlib import axis
from numpy import genfromtxt
import numpy as np
import tensorflow
import data_class
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import initializers
from tensorflow.python.keras.optimizers import adam_v2
from tensorflow.keras.layers import Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau

# Load data from csv file
data = genfromtxt('patient_priority.csv', delimiter=',',
                  skip_header=1, dtype=None, autostrip=True, encoding=None, missing_values="?", filling_values="0")
data = np.asarray(data.tolist())

# Sizes
train_size = 4000
test_size = 900

# Parse data
train_x = data[0:train_size]
train_x = train_x[:, 1:-1]
train_y = data[0:train_size]
train_y = train_y[:, -1]

test_x = data[train_size:train_size+test_size]
test_x = test_x[:, 1:-1]
test_y = data[train_size:train_size+test_size]
test_y = test_y[:, -1]

# Create model
def createModel():
    model = Sequential()
    dropoutConstant = 0.1
    initializer = initializers.RandomNormal(mean=0., stddev=0.01)
    model.add(Dense(512, input_shape=(16,), activation='relu',
                kernel_regularizer='l2', kernel_initializer=initializer))
    model.add(BatchNormalization())
    model.add(Dropout(dropoutConstant))
    model.add(Dense(256, activation='relu', kernel_regularizer='l2'))
    model.add(BatchNormalization())
    model.add(Dropout(dropoutConstant))
    model.add(Dense(128, activation='relu', kernel_regularizer='l2'))
    model.add(BatchNormalization())
    model.add(Dropout(dropoutConstant))
    model.add(Dense(64, activation='relu', kernel_regularizer='l2'))
    model.add(BatchNormalization())
    model.add(Dropout(dropoutConstant))
    model.add(Dense(4, activation='softmax', kernel_regularizer='l2'))
    adamOpti = adam_v2.Adam(learning_rate=0.0002)
    model.compile(loss='sparse_categorical_crossentropy',
                    optimizer=adamOpti, metrics=['accuracy'])
    model.fit(train_x, train_y, epochs=300,
                batch_size=256)
    _, accuracy = model.evaluate(train_x, train_y)
    return model

# Predict on test data
def predict(model):
    preds = model.predict(test_x)
    preds = np.argmax(preds, axis=1)
    for i in range(len(preds)):
        print(preds[i], test_y[i])

# Predict on data, use this with new data
def predict_on_data(model, data):
    prediction = model.predict(data)
    prediction = np.argmax(prediction, axis=1)
    return prediction

# Machine learning model
finalModel = createModel()
predict(finalModel)