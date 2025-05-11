import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
X,y=load_iris(return_X_y=True)
X_train,X_test,Y_train,Y_test=train_test_split(X,y,train_size=0.6)
nb=GaussianNB()
nb.fit(X_train,Y_train)
# acc=nb.score(X_test,Y_test)
acc=accuracy_score(Y_train,nb.predict(X_train))
print(acc)
nb.fit(X_train,Y_train)
# acc2=nb.score(X_train,Y_train)
acc2=accuracy_score(Y_test,nb.predict(X_test))
print(acc2)
