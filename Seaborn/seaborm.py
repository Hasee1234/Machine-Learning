import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#box plot
# data=pd.DataFrame({
#     'Category':['A']*50+['B']*50,
#     'Value':np.random.normal(0,1,100)
# })
# plt.figure(figsize=(10, 6))
# sns.boxplot(data=data,x='Category',y='Value')
# plt.title('Box Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()

#violinplot
# data=pd.DataFrame({
#     'Category':['A']*50+['B']*50,
#     'Value':np.random.normal(0,1,100)
# })
# plt.figure(figsize=(10, 6))
# sns.violinplot(data=data,x='Category',y='Value')
# plt.title('Box Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()

#histogram with seaborn
# data=pd.DataFrame({
#     'Value':np.random.normal(0,1,1000)
# })
# plt.figure(figsize=(10, 6))
# sns.histplot(data=data,bins=30,x='Value',kde=True, color='purple', alpha=0.5)
# plt.title('Histogram with KDE')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()
# plt.show()

#kde plot
# data=({
#     'category':['A']*500 +['B']*500,
#     'Value':np.concatenate([np.random.normal(0,1,500),
#                             np.random.normal(1,1,500)])
# })
# plt.figure(figsize=(10,6))
# sns.kdeplot(data=data,x='Value',hue='category')
# plt.title('Kernel Density Estimation')
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.show()

#bar plot
# data=pd.DataFrame({
#     'categories':['A','B','C','D'],
#     'value':[15,20,5,25]
# })
# plt.figure(figsize=(10,6))
# sns.barplot(data=data,x='categories',y='value',color='purple',alpha=0.8)
# plt.title('bar plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

#count plot
# data=pd.DataFrame({
#     'category':np.random.choice(['A','B','C','D'],100)#100 divided in to 4( A,B,C,D)
# })
# plt.figure(figsize=(10, 6))

# sns.countplot(data=data,x='category')
# plt.title('Count Plot')
# plt.xlabel('Category')
# plt.ylabel('Count')
# plt.show()

#Heat plot
# data=pd.DataFrame(np.random.randn(10,10))
# corr=data.corr()

# plt.figure(figsize=(10, 6))
# sns.heatmap(corr,annot=True)
# plt.title('Correlation Heatmap')
# plt.show()


#pairplot
# iris=sns.load_dataset('iris')
# # plt.figure(figsize=(10,6))
# sns.pairplot(iris,hue='species')
# plt.title('Pairplot of Iris Dataset')

# plt.show()

#jointplot
# iris=sns.load_dataset('iris')
# sns.jointplot(data=iris,x='sepal_length',y='sepal_width',kind='kde')
# plt.title('Jointplot of Sepal Length and Width')
# plt.show()


#regression plot
# data=pd.DataFrame({
#     'x':np.random.rand(100),
#     'y':np.random.rand(100) * 2 + 1,
# })
# plt.figure(figsize=(10, 6))

# sns.regplot(data=data,x='x',y='y')
# plt.title('Regression Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# data=pd.DataFrame({
#     'Category':['A']*50 + ['B']*50,
#     'value':np.random.normal(0,1,100)
# })
# plt.figure(figsize=(10, 6))
# sns.swarmplot(data=data,x='Category',y='value')
# plt.title('Swarm Plot')
# plt.xlabel('Category')
# plt.ylabel('Value')
# plt.show()