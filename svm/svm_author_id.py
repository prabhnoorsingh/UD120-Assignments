#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

from sklearn import svm
from sklearn.metrics import accuracy_score

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###

classifier = svm.SVC(C=10000.0, kernel='rbf')

t0=time()
classifier.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"

t1=time()
prediction = classifier.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy = classifier.score(features_test, labels_test)
print accuracy

# count=0
# for i in range(1,1701):
# 	if prediction[i] == 1:
# 		count +=1

# print count

pred_len = len(prediction)
print pred_len

result = []
for i in prediction:
	if i==1:

		result.append(pred_len)

print len(result)
# print prediction[10]
# print prediction[26]
# print prediction[50]
# accuracy = classifier.accuracy_score(prediction, labels_test)
# print accuracy

#########################################################


