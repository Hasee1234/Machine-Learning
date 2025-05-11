from sklearn.feature_selection import SelectKBest, chi2,mutual_info_classif,SelectPercentile ,GenericUnivariateSelect   #to select the best features from the datset
from sklearn.datasets import load_breast_cancer

bc=load_breast_cancer()
X1,y1=bc.data,bc.target
feature_names=bc.feature_names
print(feature_names)

#kbest method
X,y=load_breast_cancer(return_X_y=True)
k_chi=SelectKBest(chi2, k=5).fit_transform(X,y)   #to select the best features
print(k_chi.shape)

#percentile method
per_chi = SelectPercentile(chi2, percentile=5).fit_transform(X,y)   #to select the best features ,,,percentile is %age of 30 as dataset has 30 features
print(per_chi.shape)

per_mu=SelectPercentile(mutual_info_classif, percentile=5).fit(X1,y1)   
trans_mu=per_mu.transform(X1)
print(feature_names[per_mu.get_support()])

gen=GenericUnivariateSelect(chi2,mode="k_best",param=7).fit_transform(X,y)#if you dont want to write different functions use genericunivariateselect method
print(gen)