from keras.layers import Activation, Conv3D, Dense, Dropout, Flatten, MaxPooling3D
from keras.models import Sequential


def cnn3d_model(input_shape, num_classes):
    model = Sequential()
    model.add(Conv3D(32, kernel_size=(3, 3, 3), input_shape=input_shape, padding='same'))
    model.add(Activation('relu'))
    model.add(Conv3D(32, kernel_size=(3, 3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2), padding='same'))

    model.add(Conv3D(64, kernel_size=(5, 5, 5), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv3D(64, kernel_size=(5, 5, 5), padding='same'))
    model.add(Activation('relu'))
    model.add(MaxPooling3D(pool_size=(2, 2, 2), padding='same'))

    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dropout(0.7))
    model.add(Dense(num_classes, activation='softmax'))
    return model
