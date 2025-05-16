from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import mutual_info_classif,chi2,SelectKBest
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
#question 1
bc=load_breast_cancer()
X,Y=bc.data,bc.target
selector=SelectKBest(mutual_info_classif,k=8).fit_transform(X,Y)
# print(selector.shape)

#question 2
iris=sns.load_dataset('iris')
plt.figure(figsize=(10,6))
sns.boxplot(iris,color='green')
plt.show()

# question 3 )
# x,y=load_breast_cancer(train_test_split(return_X_y=True))
