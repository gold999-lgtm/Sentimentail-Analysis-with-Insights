import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Salary_Classification.csv")
labels=dataset.iloc[:,-1].values
features=dataset.iloc[:,0:4].values
dataset["Department"].unique()
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
columnTransformer=ColumnTransformer([("encoder",OneHotEncoder(),[0])],remainder="passthrough")
features=np.array(columnTransformer.fit_transform(features),dtype=np.float32)
features=features[:,1:]
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
#data engineering
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
print(regressor.predict(features_test))
x=["Development",1150,3,4]
x=np.array(x)
x=x.reshape(1,4)
x=np.array(columnTransformer.transform(x),dtype=np.float32)
x=x[:,1:]
regressor.predict(x)