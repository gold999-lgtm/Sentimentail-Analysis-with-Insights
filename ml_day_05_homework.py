import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("breast_cancer.csv")

dataset=dataset.fillna(dataset.mean())
features=dataset.iloc[:,1:10].values
labels=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)

from sklearn.svm import SVC
classifier=SVC(kernel="rbf")
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(labels_test,labels_pred)
print(classifier.score(features_test,labels_test))
print(cm)
print(features.shape)
x=[6,2,5,3,2,7,9,2,4]
x=np.array(x)
x=x.reshape(1,9)
val_pred=classifier.predict(x)
print(val_pred)
if val_pred==4:
    print("Women has Maligant Tumor")
else:
    print("Women has Benign Tumor")
