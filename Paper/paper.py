#create a 5 array
import numpy as np
arr=np.array([[[[[5]]]]])
# arr=np.zeros([[[[[5,5]]]]])
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.ndim)
# print(arr[0,0,0,0,0])
from sklearn.datasets import load_breast_cancer,load_wine,load_iris
from sklearn.feature_selection import SelectKBest,chi2,SelectPercentile,SelectFpr,f_classif
# x,y=load_breast_cancer(return_X_y=True)
# feature=SelectKBest(chi2,k=8).fit_transform(x,y)
# print(feature.shape)

bc=load_breast_cancer()
# X,Y=bc.data,bc.target
# f=SelectKBest(chi2,k=8).fit(X,Y)
# z=f.transform(X)
# print(z.shape)


#paper 2
ones=np.ones((24,24))
# print(ones.shape)
# print(ones.ndim)

wine=load_wine()
X,Y=wine.data,wine.target
percent=SelectPercentile(chi2,percentile=15).fit(X,Y)
wine2=percent.transform(X)
print(wine2.shape)

x,y=load_iris(return_X_y=True)
fpr=SelectFpr(f_classif,alpha=0.01).fit_transform(x,y)
print(fpr.shape)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset('iris')
# sns.boxplot(data=tips)
# plt.show()

# sns.histplot(data=tips,bins=20)
# plt.show()

x=1
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,color='blue',marker='^')
plt.plot(x,z,color='blue',marker='^')
plt.show()