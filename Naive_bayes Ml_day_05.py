import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Match_Making.csv")
features=dataset.iloc[:,0:2].values
labels=dataset.iloc[:,-1]
print(dataset.dtypes)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB()
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
print(classifier.score(features_test,labels_test))
"""[[12 11]
 [ 0 77]]
0.89
[[ 0 23]
 [ 0 77]]
0.77
dtype: object
[[16  7]
 [ 9 68]]
0.84"""
