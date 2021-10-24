import pandas as pd
import numpy as np
from process_data import create_standard_vector, create_standard_words
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

def test_bayes_implementation(frequencies_by_genre, book_frequencies, genres_of_books):
    data = [
        (bdata[0], g)
        for bdata in zip(book_frequencies, genres_of_books)
        for g in bdata[1]
    ]
    book_frequencies, genres_of_books = [i for i, j in data], [j for i, j in data]

    genre_encoder = LabelEncoder()
    genres_of_books = genre_encoder.fit(genres_of_books).transform(genres_of_books)

    standard_words = create_standard_words(frequencies_by_genre.values())
    corpus_frequency = np.sum([create_standard_vector(f, standard_words) for f in frequencies_by_genre.values()], axis=0)
    #standard_genre_frequencies = [create_standard_vector(genre_frequency, standard_words) for genre_frequency in frequencies_by_genre.values()]
    standard_book_frequencies = [create_standard_vector(book_frequency, standard_words) for book_frequency in book_frequencies] # from where ????
    # downweight double books if you get to it

    relative_book_frequencies = [
        [
            x[0]/x[1]
            for x in zip(frequency, corpus_frequency)
        ]
        for frequency in standard_book_frequencies
    ]
    
    #Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(relative_book_frequencies, genres_of_books, test_size = 0.3, random_state=31)

    clfrNB = MultinomialNB(alpha = 0.1)
    clfrNB.fit(X_train, y_train)
    preds = clfrNB.predict(X_test)
    print(y_test, preds)
    print(genre_encoder.inverse_transform(preds))