from numpy import genfromtxt, shape, sort
import numpy as np
import tensorflow
import data_class
from data_class import data_class
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import initializers
from tensorflow.python.keras.optimizers import adam_v2
from tensorflow.keras.layers import Dropout

class ai_model:
    def __init__(self):
        data = genfromtxt('patient_priority.csv', delimiter=',',
                    skip_header=1, dtype=None, autostrip=True, encoding=None, missing_values="", filling_values=0)
        data = np.asarray(data.tolist())

        # Parse data
        self.train_size = 4000
        self.train_x = data[0:self.train_size]
        self.train_x = self.train_x[:, 1:-1]
        self.train_y = data[0:self.train_size]
        self.train_y = self.train_y[:, -1]
        self.model = self.createModel()
        self.listOfNumpyPatients = []
        self.listOfPatientObjects = []

    # Create model
    def createModel(self):
        model = Sequential()
        dropoutConstant = 0.1
        initializer = initializers.RandomNormal(mean=0., stddev=0.01)
        model.add(Dense(512, input_shape=shape(self.train_x[0]), activation='relu',
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
        model.fit(self.train_x, self.train_y, epochs=300,
                    batch_size=256)
        _, accuracy = model.evaluate(self.train_x, self.train_y)
        return model

    # Sort list of patients
    def sortList(self):
        self.listOfPatientObjects.sort(key=lambda x: x.triage, reverse=True)

    # Insert patient into list
    def insertPatient(self, patient):
        self.listOfPatientObjects.append(patient)
        self.listOfNumpyPatients.append(patient.to_np_arr())
    
    # Predict on data, use this once all the patients have been inserted
    def predict_on_data(self):
        prediction = self.model.predict(np.asarray(self.listOfNumpyPatients))
        prediction = np.argmax(prediction, axis=1)
        for x in range(len(self.listOfPatientObjects)):
            self.listOfPatientObjects[x].triage = prediction[x]
        self.sortList()
        return prediction

# Machine learning model example
# ai = ai_model()
# patient = data_class(67, 1, 0, 160, 286, 108, 1, 0, 0, 0, 26.2, 0.313, 0, 0, 0, 0, 0)
# ai.insertPatient(patient)
# patient = data_class(67, 1, 0, 120, 229, 129, 1, 0, 0, 0, 38.5, 0.591, 0, 0, 0, 0, 0)
# ai.insertPatient(patient)
# patient = data_class(37, 1, 0, 130, 250, 187, 0, 0, 0, 0, 25.9, 0.209, 0, 0, 0, 0, 0)
# ai.insertPatient(patient)
# patient = data_class(41, 0, 0, 130, 204, 172, 0, 0, 0, 0, 32.8, 0.334, 0, 0, 0, 0, 0)
# ai.insertPatient(patient)
# print(ai.predict_on_data())