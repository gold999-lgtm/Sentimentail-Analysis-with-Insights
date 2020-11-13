import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Heart_Disease.csv")
features=dataset.iloc[:,0:9].values
labels=dataset.iloc[:,-1]
print(dataset.dtypes)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
#feature_scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
"""array([2, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1,
       
       1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1,
       1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1,
       1, 1, 1, 1, 2])"""
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
"""array([[53,  8],
       [16, 16]]"""
      