import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("affairs.csv")
features=dataset.iloc[:,0:8].values
labels=dataset.iloc[:,-1]
print(dataset.dtypes)


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
columnTransformer=ColumnTransformer([("encoder",OneHotEncoder(),[6,7])],remainder="passthrough")
features=np.array(columnTransformer.fit_transform(features),dtype=np.float32)


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

from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
print(labels_pred)

print(classifier.score(features_test,labels_test))


