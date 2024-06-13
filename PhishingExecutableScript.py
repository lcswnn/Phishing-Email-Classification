#import libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


#import data and print to check form
df = pd.read_csv('phishing_email_scaled.csv', nrows=11000)

#split data into X and y partitions
X = df['text_combined']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

#create Pipeline for model
pipeSVC = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LinearSVC())
])


#fit model and predict
#LinearSVC Pipeline
pipeSVC.fit(X_train, y_train)
#preds
SVCpredict = pipeSVC.predict(X_test)

SVCscore = accuracy_score(y_test, SVCpredict)
print(f"SVC Accuracy: {SVCscore}")

'''

clean_email = userEmail.strip()

passThrough = [clean_email]

newPredict = pipeSVC.predict(passThrough)
if str(newPredict) == '[0]':
  print("Your email is safe.")
else:
  print("This is a Phishing Email.")
'''