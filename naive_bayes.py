import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics

def naive_bayes_implement(document_frequencies, genres):
    uncoded_words = []
    uncoded_frequencies = []
    targets = []

    for idx, frequencies in enumerate(document_frequencies):
        for word in frequencies.keys():
            uncoded_words.append(word)
            uncoded_frequencies.append(frequencies[word])
            targets.append(idx) # Also genre idx
    print(targets)
    wordsle = preprocessing.LabelEncoder()
    encoded_words = wordsle.fit_transform(uncoded_words)
    freqle = preprocessing.LabelEncoder()
    encoded_frequencies = freqle.fit_transform(uncoded_frequencies)


    data = list(zip(encoded_words, encoded_frequencies))

    gnb = GaussianNB()
    gnb.fit(data, targets)


    predicted = gnb.predict([[0, 2]])

    X_train, X_test, y_train, y_test = train_test_split(data, targets, test_size=0.3,random_state=109)
    gnb.fit(X_train, y_train)

    y_pred = gnb.predict(X_test)
    print(encoded_words)
    print(encoded_frequencies)
    print(targets)
    print(wordsle.inverse_transform(encoded_words))
    print(freqle.inverse_transform(encoded_frequencies))

    print(tuple(zip(genres, targets)))
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    
    print(predicted)