from numpy import genfromtxt, shape, sort
import numpy as np
import tensorflow
import data_class
import os.path
from data_class import data_class
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import initializers
from tensorflow.keras import optimizers
from tensorflow.keras.layers import Dropout

class ai_model:
    # Initialize model
    def __init__(self):
        data = genfromtxt('patient_priority.csv', delimiter=',',
                    skip_header=1, dtype=None, autostrip=True, encoding=None, missing_values="", filling_values=0)
        data = np.asarray(data.tolist())

        # Parse data and separate into x and y
        self.train_size = 4000
        self.train_x = data[0:self.train_size]
        self.train_x = self.train_x[:, 1:-1]
        self.train_y = data[0:self.train_size]
        self.train_y = self.train_y[:, -1]
        # Check if model exists, if not create it
        if os.path.isfile('model.h5'):
            self.model = tensorflow.keras.models.load_model('model.h5')
        else:
            self.model = self.createModel()
        # Create list of patients
        self.listOfNumpyPatients = []
        self.listOfPatientObjects = []

    # Create model
    def createModel(self):
        model = Sequential()
        dropoutConstant = 0.1
        initializer = initializers.RandomNormal(mean=0., stddev=0.01)
        # Add layers
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
        # Output layer, 4 classes so use softmax
        model.add(Dense(4, activation='softmax', kernel_regularizer='l2'))
        # Compile model
        model.compile(loss='sparse_categorical_crossentropy',
                        optimizer=tensorflow.optimizers.Adam(learning_rate=0.0002), metrics=['accuracy'])
        # Fit model
        model.fit(self.train_x, self.train_y, epochs=300,
                    batch_size=256)
        _, accuracy = model.evaluate(self.train_x, self.train_y)
        # Save model
        model.save('model.h5')
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
        # Get the highest probability
        prediction = np.argmax(prediction, axis=1)
        # Update the triage value of the patient
        for x in range(len(self.listOfPatientObjects)):
            self.listOfPatientObjects[x].triage = prediction[x]
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