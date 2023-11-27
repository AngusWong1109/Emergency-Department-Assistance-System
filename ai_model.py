from calendar import c
from cgi import test
from tabnanny import verbose
from matplotlib import axis
from numpy import genfromtxt, shape, sort
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

listOfNumpyPatients = []
listOfPatientObjects = []
# Load data from csv file
data = genfromtxt('patient_priority.csv', delimiter=',',
                  skip_header=1, dtype=None, autostrip=True, encoding=None, missing_values="", filling_values=0)
data = np.asarray(data.tolist())

# Sizes
train_size = 4000
test_size = 900

# Parse data
train_x = data[0:train_size]
train_x = train_x[:, 1:-1]
train_y = data[0:train_size]
train_y = train_y[:, -1]

# test_x = data[train_size:train_size+test_size]
# test_x = test_x[:, 1:-1]
# test_y = data[train_size:train_size+test_size]
# test_y = test_y[:, -1]

# Create model
def createModel():
    model = Sequential()
    dropoutConstant = 0.1
    initializer = initializers.RandomNormal(mean=0., stddev=0.01)
    model.add(Dense(512, input_shape=shape(train_x[0]), activation='relu',
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

# Predict on data, use this once all the patients have been inserted
def predict_on_data(model, data):
    prediction = model.predict(data)
    prediction = np.argmax(prediction, axis=1)
    for x in range(len(listOfPatientObjects)):
        listOfPatientObjects[x].triage = prediction[x]
    sortList()
    return prediction

# Sort list of patients
def sortList():
    listOfPatientObjects.sort(key=lambda x: x.triage, reverse=True)

# Insert patient into list
def insertPatient(patient):
    listOfPatientObjects.append(patient)
    listOfNumpyPatients.append(patient.to_np_arr())

# Machine learning model
finalModel = createModel()
# patient = data_class.data_class(67, 1, 3, 160, 286, 108, 1, 0, 23, 0, 30.4, 0.319, 1, 0, 0, 0, 0)
# patient2 = data_class.data_class(68, 1, 3, 160, 186, 108, 1, 0, 23, 0, 30.4, 0.32, 1, 0, 0, 0, 0)
# insertPatient(patient)
# insertPatient(patient2)
predict_on_data(finalModel, np.asarray(listOfNumpyPatients))