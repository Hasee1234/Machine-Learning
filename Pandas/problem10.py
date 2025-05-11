import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
x,y=load_iris(return_X_y=True)
dt=DecisionTreeClassifier()
acc_3=cross_val_score(dt,x,y,cv=3)
print(acc_3)