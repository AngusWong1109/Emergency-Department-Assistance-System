from tabnanny import verbose
from numpy import genfromtxt
import numpy as np
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import initializers
from tensorflow.python.keras.optimizers import adam_v2
from tensorflow.keras.layers import Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau

# Load data from csv file
data = genfromtxt('patient_priority.csv', delimiter=',', skip_header=1, dtype=None, autostrip=True, encoding=None)
data = np.asarray(data.tolist())

# Sizes
train_size = 4900
test_size = 3000

# Parse data
train_x = data[0:train_size]
train_x = train_x[:,1:-1]
train_y = data[0:train_size]
train_y = train_y[:,-1]

test_x = data[0:test_size]
test_x = test_x[:,1:-1]
test_y = data[0:test_size]
test_y = test_y[:,-1]

# Printing accuracy
def predict(model):
    prediction = model.predict(test_x)
    predicted_values = prediction > 0.5
    total = len(test_y)
    avg = 0
    for i in range(total):
        if predicted_values[i] == test_y[i]:
            avg += 1
    print("Testing accuracy: ", avg/total)
    return avg/total

# Machine learning model
finalModel = Sequential()
dropoutConstant = 0.05
initializer = initializers.RandomNormal(mean=0., stddev=0.01)
finalModel.add(Dense(100, input_shape=(16,), activation='relu', kernel_regularizer='l2', kernel_initializer=initializer))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(95, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(90, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(80, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(70, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(60, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(50, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(40, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(30, activation='relu', kernel_regularizer='l2'))
finalModel.add(BatchNormalization())
finalModel.add(Dropout(dropoutConstant))
finalModel.add(Dense(1, activation='linear', kernel_regularizer='l2'))
adamOpti = adam_v2.Adam(learning_rate=0.0002)
reduce_lr = ReduceLROnPlateau(monitor='loss', patience=200, min_lr=0.00002, verbose=1, mode='auto')
finalModel.compile(loss='mean_squared_error', optimizer=adamOpti, metrics=['accuracy'])
finalModel.fit(train_x, train_y, epochs=500, batch_size=256, callbacks=[reduce_lr])
_, accuracy = finalModel.evaluate(train_x, train_y)
print("Training accuracy: ", accuracy)
predict(finalModel)