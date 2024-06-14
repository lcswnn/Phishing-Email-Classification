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

import tkinter as tk
from tkinter import ttk


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

message = f"\n \n NOTE: ML Model Accuracy at: {round((SVCscore * 100), 2)} %. \n (Not 100% accurate. For demonstration purposes only.)"

#GUI
root = tk.Tk()
root.geometry("1100x900")
root.title(" Phishing Email Detector ")

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    newPredict = pipeSVC.predict([INPUT])
    if(str(newPredict) == "[0]"):
        Output.insert(tk.END, '\n' + 'Your email is safe.' + message + "\n")
    else:
        Output.insert(tk.END, '\n' + "Your email is a Phishing Email. \n" + message + "\n")
        
def clear():
    Output.delete(1.0 ,tk.END)

l = tk.Label(text = "Copy and Paste your email in the top box...")
inputtxt = tk.Text(root)
Output = tk.Text(root)
Display = tk.Button(root, height = 2,
                width = 20, 
                text = "Check for Phish",
                command = lambda:Take_input())
ClearBtn = tk.Button(root, height = 2,
                width=20,
                text="Clear Output",
                command = lambda:clear())
l.pack()
inputtxt.pack()
Display.pack()
Output.pack()
ClearBtn.pack()

tk.mainloop()