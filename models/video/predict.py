from cv2 import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model
import tensorflow as tf

# model = load_model('model.h5')

def predictVideo(frame):
    preprocessedFrame = preprocessing(frame);

    print('predic' + str(len(preprocessedFrame)))
    frame = preprocessedFrame[None,:]
    # result = model.predict(frame)
    # result = 3
    return result

def preprocessing(frame):
    resized = cv2.resize(frame, (320,240))
    # print('resized : ' + str(resized.shape))
    grayscaled = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    # print('grayscaled : ' + str(grayscaled.shape))
    retval,thresholded = cv2.threshold(grayscaled, 128, 1, cv2.THRESH_BINARY)
    # print('thresholded : ' + str(thresholded.shape))
    thresholded = np.expand_dims(thresholded, axis=-1)
    # print('expand : ' + str(thresholded.shape))
    return thresholded  


