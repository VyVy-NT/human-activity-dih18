import os

from keras.optimizers import SGD

from config3d import *
from dataset import categories

opt = SGD(lr=0.71, decay=1e-4)
MyModel = getattr(getattr(__import__('models.' + MODEL), MODEL), MODEL + '_model')
model = MyModel(input_shape=SIZE3D + (DEPTH, CHANNELS), num_classes=len(categories))
model.compile(loss="categorical_crossentropy", optimizer='adam', metrics=['accuracy'])


def load_model():
    if not os.path.isdir(RESULT_PATH):
        os.mkdir(RESULT_PATH)
    model.load_weights(os.path.join(RESULT_PATH, MODEL_NAME))
    print('Loaded model successfully')


def save_model():
    with open(os.path.join(RESULT_PATH, MODEL_NAME) + '.json', 'w')as model_file:
        model_file.write(model.to_json())
    model.save_weights(os.path.join(RESULT_PATH, MODEL_NAME) + '.h5')
    print('Saved model successfully')


try:
    load_model()
except:
    pass
