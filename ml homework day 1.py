import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Salaries.csv")
data_gender=df["sex"].value_counts().reset_index()
data_gender_ref=pd.DataFrame()
data_gender_ref["Male"]=[data_gender["sex"][0]]
data_gender_ref["Female"]=[data_gender["sex"][1]]
plt.pie([data_gender_ref["Male"],data_gender_ref["Female"]],explode=[0,0],labels=["male","female"],autopct="%1.1f%%")
plt.axis("equal")
