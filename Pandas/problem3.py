import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

X,y=load_diabetes(return_X_y=True)
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.5)
print(X_train.shape)
print(X_test.shape)