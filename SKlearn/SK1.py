from sklearn.datasets import load_iris #here load-iris is predifined datasets of sk learn
from sklearn.model_selection import train_test_split #train-test split to separate the data into training and testing
from sklearn.ensemble import RandomForestClassifier#to build a model we use randomforestclassifier from ensemble method which can be used for classifiers and regressors,here we use for classifiers

#down X is array for data and y is array for data labels
X,y=load_iris(return_X_y=True)#return_X_y is taken from parameters of load_iris you can see allby hovering o load_iris

print(X.shape)#to see shape of data i.e.,rows and columns
print(y.shape)#to see shape of labels/targets i.e.,rows and columns

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=0)
#0.3 test_size means 30% of data for testing
# random_state shuffles the data when it value is 0,you use it when you want to shuffle data before splitting 

print("Training data:"+str(X_train.shape))
print("Testing data:"+str(X_test.shape))

# initialize randomforest 
clf_rf=RandomForestClassifier(n_estimators=200,max_depth=3)#number of paarmeters are by default 100 but ou can define yourself in n-estimators(it means number of decision trees ever made)
#can also define max_depth

#for fitting
clf_rf.fit(X_train,y_train)#in fit()you will give the training arrays of test and labels

#prediction or accuracy
#for testing data
rf_acc=clf_rf.score(X_test,y_test)#score is amethod that give you accuracy,inputs are testing arrays,now classifier is ready you can print it

#for training data
rf_acc_tr=clf_rf.score(X_train,y_train)#score is amethod that give you accuracy,inputs are training arrays,now classifier is ready you can print it

print(rf_acc)
print(rf_acc_tr)
print("test set accuracy for random forest :"+str(rf_acc*100))#in %age
print("training set accuracy for random forest :"+str(rf_acc_tr*100))#in %age
#the more you train the data the more its accurate and will move towards overfitting like we did 0.3