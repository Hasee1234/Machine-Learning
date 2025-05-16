import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import load_breast_cancer,load_wine
from sklearn.feature_selection import SelectKBest,chi2,SelectPercentile
# zeros=np.zeros((2,3,4,5,6))
# print(zeros.shape)
# print(zeros.ndim)

# random=np.random.rand(1,2,3,4,5)
# print(random.shape)
# print(random.ndim)
# print(random)
# arr = np.ones((24, 24), dtype=int)

# # Calculate the center start and end indices for a 4x4 block
# start = 10  # 10
# end = 14      # 14

# # Set the center 4x4 block to zeros
# arr[start:end, start:end] = 0

# # Print the array or display as an image for clarity
# print(arr)

# plt.figure(figsize=(10,6))
# plt.plot(2,4,label='London',color='green',marker='^')
# plt.plot(5,7,label='Paris',color='red',marker='^')
# plt.legend()
# plt.show()


# tips=sns.load_dataset('tips')
# plt.figure(figsize=(10,6))
# sns.boxplot(data=tips,x='total_bill',y='day')
# plt.show()

# iris=sns.load_dataset('iris')
# sns.histplot(data=iris,x='petal_length')
# plt.show()

# bc=load_breast_cancer()
# X,Y=bc.data,bc.target
# feature_name=bc.feature_names
# kbest_selector=SelectKBest(chi2,k=8).fit(X,Y)
# selector=kbest_selector.transform(X)
# print(feature_name[kbest_selector.get_support()])

# wine=load_wine()
# x,y=wine.data,wine.target
# feature_name=np.array(wine.feature_names)
# percent=SelectPercentile(chi2,percentile=15).fit(x,y)
# trans=percent.transform(x)
# print(feature_name[percent.get_support()])

# x=pd.DataFrame(np.random.rand(12,12),columns=['a','b','c','d','a','b','c','d','a','b','c','d'])
# corr=x.corr()
# sns.heatmap(corr,annot=True)
# plt.title('heat map')
# plt.show()
iris=sns.load_dataset('iris')
plt.scatter(iris['petal_length'],iris['petal_width'],cmap='viridis')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.legend()
plt.show()