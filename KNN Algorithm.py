import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("caesarian.csv")
features=dataset.iloc[:,0:5].values
labels=dataset.iloc[:,-1]
print(dataset.dtypes)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
#feature_scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
features_train=sc.fit_transform(features_train)
features_test=sc.transform(features_test)

from sklearn.neighbors import KNeighborsClassifier
classifier=KNeighborsClassifier(n_neighbors=11,p=1)
classifier.fit(features_train,labels_train)
labels_pred=classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
x=[24,2,2,1,0]

x=np.array(x)
x=x.reshape(1,5)
x=sc.transform(x)

print(classifier.predict(x))