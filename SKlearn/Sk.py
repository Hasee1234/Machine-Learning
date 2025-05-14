from sklearn.datasets import load_breast_cancer,load_diabetes
from sklearn.feature_selection import SelectKBest,chi2,SelectPercentile,VarianceThreshold,f_classif,f_regression,GenericUnivariateSelect,SelectFdr,SelectFpr,SelectFwe


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
feature_name=bc.feature_names
# print(feature_name)

perchi=SelectPercentile(chi2,percentile=20).fit(X,Y)
trans_per=perchi.transform(X)
# print(feature_name[perchi.get_support()])

k_chi2=SelectKBest(chi2,k=5).fit(X,Y)
trans_kchi2=k_chi2.transform(X)
# print(feature_name[k_chi.get_support()])

#variance threshold
selector=VarianceThreshold(threshold=0.5).fit_transform(X,Y)
# print(selector.shape)

# f_classif anova f-test
anova_selector=SelectKBest(score_func=f_classif,k=10).fit_transform(X,Y)
# print(anova_selector.shape)

# f_regression 
reg_selector=SelectKBest(score_func=f_regression,k=10).fit_transform(x,y)
# print(reg_selector.shape)

# GenericUnivariateSelect can used for any method
gen=GenericUnivariateSelect(chi2,mode="k_best",param=7).fit_transform(X,Y)
# print(gen.shape)

#  SelectFpr / SelectFdr / SelectFwe
fpr=SelectFpr(chi2,alpha=0.05).fit_transform(X,Y)
print(fpr.shape)

fdr=SelectFdr(chi2,alpha=0.05).fit_transform(X,Y)
print(fdr.shape)

fde=SelectFwe(chi2,alpha=0.05).fit_transform(X,Y)
print(fde.shape)