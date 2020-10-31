#!/usr/bin/python3
import time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras import utils
from tensorflow.keras.datasets import mnist
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard

def Run(n_epochs, early_stop):
    (train_dataset, train_classes),(test_dataset, test_classes) = mnist.load_data()
    train_dataset = train_dataset.reshape(train_dataset.shape[0], 28, 28, 1)
    test_dataset = test_dataset.reshape(test_dataset.shape[0], 28, 28, 1)

    train_dataset = train_dataset.astype('float32')
    test_dataset = test_dataset.astype('float32')

    train_dataset = train_dataset / 255
    test_dataset = test_dataset / 255

    train_classes = utils.to_categorical(train_classes, 10)
    test_classes = utils.to_categorical(test_classes, 10)


    cnn = Sequential()
    cnn.add(Conv2D(32, (3,3), input_shape = (28, 28, 1), activation = 'relu'))
    cnn.add(MaxPooling2D())
    cnn.add(Dropout(0.25))
    cnn.add(Flatten())
    cnn.add(Dense(units = 128, activation = 'relu'))
    cnn.add(Dropout(0.5))
    cnn.add(Dense(units = 10, activation = 'softmax'))

    adam = Adam(lr=0.001)
    cnn.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
    top_layers_file_path="MNIST_Model.iv3.hdf5"

    checkpoint = ModelCheckpoint(top_layers_file_path, monitor='loss', verbose=1, save_best_only=True, mode='min')

    early = EarlyStopping(monitor="loss", mode="min", patience=int(early_stop))

    tb = TensorBoard(log_dir='./logs', batch_size=128, write_graph=True, update_freq='batch')

    reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=10, min_lr=0.0001)

    cnn.fit(train_dataset, train_classes, batch_size = 128, epochs = int(n_epochs),
            validation_data = (test_dataset, test_classes),
            callbacks=[checkpoint, early, reduce_lr, tb])

    result = cnn.evaluate(test_dataset, test_classes)
    #print ('Accuracy = ' + str(result[1] * 100) + "%")
    return ('Accuracy = ' + "{:.2f}".format(result[1] * 100) + " %")
