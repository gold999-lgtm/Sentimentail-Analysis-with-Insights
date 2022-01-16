from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
import pickle
from keras.applications.imagenet_utils import decode_predictions
from keras.preprocessing import image
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from keras.models import model_from_json
import webbrowser
app = Flask(__name__)
json_file=open("C:/Users/Swati Lohiya/Downloads/models/model_json","r")
loaded_model_json=json_file.read()
json_file.close()
loaded_model=model_from_json(loaded_model_json)
loaded_model.load_weights("C:/Users/Swati Lohiya/Downloads/models/model.h5")
loaded_model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
def model_predict(img_path, loaded_model):
    img = image.load_img(img_path, target_size=(64,64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = loaded_model.predict(x)
    temp=0
    classes=["Balbasaur","Charmander","Pikachu"]
    for clss in classes:
      for pred in (preds>0.5).astype("int32"):
        while temp<len(pred):
          if pred[temp]==1:
            actual_pred=clss
            temp+=1
            break
          temp+=1
          break
    return actual_pred
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")
@app.route("/predict",methods=["GET","POST"])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        preds = model_predict(file_path, loaded_model)
        return preds
    return None
def main():
    open_browser()
    global app
    app.run()
    app=None
if __name__ == '__main__':
    main()
    print("This code will be executed when you break the connection")