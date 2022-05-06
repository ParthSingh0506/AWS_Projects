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
