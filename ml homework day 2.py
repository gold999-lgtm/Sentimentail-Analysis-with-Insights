import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Bahubali2_vs_Dangal.csv")
features=dataset["Days"].values
labels=dataset.loc[:,["Bahubali_2_Collections_Per_day","Dangal_collections_Per_day"]].values
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
#model
features=features.reshape(9,1)
#training of the model
regressor.fit(features,labels)
m=regressor.coef_
print(m)
c=regressor.intercept_
print(c)
#prediction
#x=10
#y=mx+x
x=[10]
x=np.array(x)
x=x.reshape(1,1)
print(regressor.predict(x))

