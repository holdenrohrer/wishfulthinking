import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

def naive_bayes_implement(document_frequencies, genres):
    le = preprocessing.LabelEncoder()
    encoded_words = []
    encoded_frequencies = []
    encoded_genres = []


    for frequencies in document_frequencies:
        for word in frequencies.keys():
            encoded_words.append(word)
            encoded_frequencies.append(frequencies[word])
            encoded_genres.append(document_frequencies.index(frequencies))

    encoded_words = le.fit_transform(encoded_words)
    encoded_frequencies = le.fit_transform(encoded_frequencies)
    targets = le.fit_transform(encoded_genres)

    data = list(tuple(zip(encoded_words, encoded_frequencies)))

    gnb = GaussianNB()
    gnb.fit(data, encoded_genres)


    predicted = gnb.predict([[0, 2]])

    X_train, X_test, y_train, y_test = train_test_split(data, targets, test_size=0.3,random_state=109)
    gnb.fit(X_train, y_train)

    y_pred = gnb.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    
    print(predicted)

