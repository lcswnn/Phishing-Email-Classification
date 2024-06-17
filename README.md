# Phishing-Email-Classification
### Description
This project utilizes using text as training data for various machine learning models. Through this process, we are able to find the best performing model and from there create an executable that users can use in order to find out if their emails are phishing emails or not. The training data used is sourced from Kaggle and has around 11000 different rows of data. This allows us to get more training/testing data to better understand our models.

**Libraries Used:** SKLearn(Random Forest, Decision Tree, MLP Classifier, Pipeline, TfidfVectorizer, Multinomail Naive Bayes, Complement Naive Bayes, LinearSVC), Pandas, MatPlotLib, Numpy

The executable python file in the repository utilizes the LinearSVC model and Tkinter for GUI programming. In the future, I will look to make a web application instead implementing database connections for model training and possibly Django for web frameworks.

### Findings
We found that the LinearSVC and MLP Classifier models are the best when it comes to training on text and text identification. All the models tested were good canidates, but LinearSVC and MLP stood out amongst the rest with a 97-99% accuracy for both every run. Although the MLp Classifier gives LinearSVC a run for its money, the time that it takes for the model to run is too long for the executable script that the user would use. Therefore, LinearSVC was used in the executable script for time purposes.

### Visualization of Model Performances
Below I have attatched the graph of model performances based on train/test data. I find it nice to see all the performances side by side to compare easier:

![output](https://github.com/lcswnn/Phishing-Email-Classification/assets/118494460/402da32e-6502-4bd4-aef9-839cacdf6a55)

