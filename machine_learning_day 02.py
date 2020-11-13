import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset=pd.read_csv("student_scores.csv")
dataset.plot(x="Hours",y="Scores",style="o")
features=dataset["Hours"].values
labels=dataset["Scores"].values
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
#model
features=features.reshape(25,1)
#training of the model
regressor.fit(features,labels)
m=regressor.coef_
c=regressor.intercept_
#prediction
#x=10
#y=mx+x
x=[10]
x=np.array(x)
x=x.reshape(1,1)
regressor.predict(x)
plt.scatter(features,labels,color='red')
plt.plot(features,regressor.predict(features))
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(features_train,labels_train)
print(regressor.predict(features_test))
regressor.score(features_test,labels_test)
