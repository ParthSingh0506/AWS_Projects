import numpy as np
import pandas as pd
import joblib

#Importing Dataset

dataset = pd.read_csv(r"breast_cancer.csv")
print(dataset.columns)

X = dataset.iloc[: , 1:-1].values
y = dataset.iloc[: , -1].values

#Splitting Data into training data and test set

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)

#Training Model on the Training Set

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state =0)
classifier.fit(X_train,y_train)

joblib.dump(classifier,'cancer.pkl')

#Predicting value on the test set

mod = joblib.load('cancer.pkl')
y_pred = classifier.predict(X_test)
print(y_pred)

#Making of Confusion Matrix 
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred,y_test)
print(cm)
s = (104+59)/(103+59+4+5)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
