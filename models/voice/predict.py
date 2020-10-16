import librosa
import speech_recognition
import scipy.io.wavfile
import wavio
import base64
import os
import glob
import io
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import pywt
import os
import time
import tensorflow as tf
import sklearn

@app.route("/predict", methods=['GET','POST'])
def predictVoice(data):
    #load model
    # load json and create model
    adam = "model/opsadammodelspeechrobotnofold_100.json"
    adamWeight = "model/opsadammodelspeechrobotnofold_100.h5"
    json_file = open(adam, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights(adamWeight)
    print("Loaded model from disk")
    #Predict
    data2 = np.array(data)
    data2 = data2.reshape((1,data2.shape[0], data2.shape[1]))
    prediction = model.predict(data2)
    hasil = np.argmax(prediction[0],axis=-1)

    switcher={
        1: "Maju",
        2: "Mundur",
        3: "Kiri",
        4: "Kanan"    
    }

    hasil = switcher.get(hasil,"Nothing")
    print(hasil)

    return render_template("resultvideo.html", hasil=hasil)
    # hasilakhir = (result, extracted)
    # return redirect(url_for('.predict_result', result=result, filename=f.filename))


    
