import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

X,y=load_breast_cancer(return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.6)
dt=DecisionTreeClassifier()
dt.fit(X_train,y_train)
acc1=accuracy_score(y_test,dt.predict(X_test))
dt.fit(X_train,y_train)
acc2=accuracy_score(y_test,dt.predict(X_test))
print(acc1)
print(acc2)


X,y=load_breast_cancer(return_X_y=True)
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.6)
sv=SVC()
sv.fit(X_train,y_train)
acc3=accuracy_score(y_test,sv.predict(X_test))
sv.fit(X_train,y_train)
acc4=accuracy_score(y_train,sv.predict(X_train))
print(acc3)
print(acc4)