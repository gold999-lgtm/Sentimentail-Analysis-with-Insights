import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("Iris (1).csv")
data=data.drop("Id",axis=1)
features=data.iloc[:,0:4].values
labels=data.iloc[:,-1].values
from sklearn import preprocessing
label=preprocessing.LabelEncoder()
labels=label.fit_transform(data.Species)
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,random_state=0,test_size=0.20)
from sklearn.linear_model import LogisticRegression
regressor=LogisticRegression()

regressor.fit(features_train,labels_train)
labels_pred=regressor.predict(features_test)
print(labels_pred)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
print(regressor.score(features_test,labels_test))
