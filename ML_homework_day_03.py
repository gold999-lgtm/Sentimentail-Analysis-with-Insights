import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("Female_Stats.csv")
labels=dataset.iloc[:,0].values
features=dataset.iloc[:,1:].values        
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.05,random_state=0)
#data engineering
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
pred=regressor.predict(features_test)
print(pd.DataFrame(zip(pred,labels_test)))
x=[75,75]
x=np.array(x)
x=x.reshape(1,2)
pred1=regressor.predict(x)
print(pred1)
#when fathers height is kept constant 
x=[76,75]
x=np.array(x)
x=x.reshape(1,2)
pred2=regressor.predict(x)
print(pred2)
difference=pred2-pred1
print(difference)

#when mothers height is kept constant
x=[75,76]
x=np.array(x)
x=x.reshape(1,2)
pred3=regressor.predict(x)
print(pred3)
diff=pred3-pred1
print(diff)