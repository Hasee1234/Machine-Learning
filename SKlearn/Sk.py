from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectKBest,chi2,SelectPercentile


x,y=load_breast_cancer(return_X_y=True)
# print(x.shape)
# print(y.shape)

#kbest
k_chi=SelectKBest(score_func=chi2,k=5).fit_transform(x,y)
k_chi=SelectKBest(chi2,k=5).fit_transform(x,y)#any method
# print(k_chi.shape)

#percentile method
per_chi=SelectPercentile(score_func=chi2,percentile=15).fit_transform(x,y)
# print(per_chi.shape)

#feature names
bc=load_breast_cancer()
X,Y=bc.data,bc.target
feature_name,g=bc.feature_names
print(feature_name)

