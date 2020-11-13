import matplotlib
import numpy as np
import pandas as pd
print(matplotlib.__version__)
#pyplot- matlab
import matplotlib.pyplot as plt
"""x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]
plt.scatter(x,y)
x=[1,2,3,4,5,6]
y=[1,4,9,16,25,36]
plt.scatter(x,y)
plt.plot(x,y)"""
plt.title("Forsk Coding School")
"""branchnames=["CSE","ECE","IT","EE"]
studentcount=[15,30,25,10]
plt.pie(studentcount,labels=branchnames)"""
print(np.__version__)
list1=[1,2,3,4,5,6]
print(type(list1))
list2=[]
for item in list1:
    list2.append(item*item)
print(list2)
a=[0,1,2,3,4,5,6,7,8]
print(type(a))
x=np.array(a)
print(type(x))
print(x)
print(x.dtype)
print(x[0])
print(x[:-1])
print(x[0:5])
print(x[-1])
print(x.ndim)
print(x.shape)
a=[0,1,2,3,4,5,6,7,8]
x=x.reshape(3,3)
print(x)
print(x.ndim)
print(x.shape)
x=np.arange(10,dtype=np.uint8)
print(x.ndim)
print(x.dtype)
a=np.arange(5)
print(a)
b=np.arange(5)
print(b)
print(a+b)
print(a-b)
print(a>=3)
print(np.sign(a))
print(np.cos(a))
print(a>=b)
print(pd.__version__)
df=pd.read_csv("Salaries.csv")
print(type(df))
print(df.ndim)
print(df.shape)
print(df)
#want to know the column names
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.head(2))
print(df.tail)
print(df.sample(2))
print(df.sample())
print(df["rank"])
print(df["salary"])
print(df[["rank","salary"]])
print(df.iloc[10])
print(df.iloc[5:10,5])
print(df.iloc[10:15,0:3])
print(df.iloc[[5,10],[0,5]])
print(df.loc[0:5,"rank"])
print(df.loc[0:4,["rank","salary"]])
print(df.loc[:,["rank","salary"]])
df["rank"]
print(df["rank"].unique())
print(df["rank"].value_counts())
filter1=df["salary"].isnull()
print(df[filter1])
print(df[df["salary"].isnull()])

df2=df.fillna(100)
df3=df.fillna(df.mean())
df4=df.dropna()
x=df["rank"].value_counts()
x=["Male","Female"]
plt.pie(df["sex"].value_counts(),labels=x,autopct="%1.1f%%")
plt.axis('equal')
"""y=["Prof","AsstProf","AssocProf"]
plt.pie(x,labels=y,autopct="%1.1f%%")
plt.axis('equal')"""

 







    
    