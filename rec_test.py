from book import Book
from vectors import similarity
from process_frequencies import get_word_frequencies
import os

def call_example(user_book):


    directory = './archive'
    corpus = []

    greatest_sim_num = 0
    print(directory)
    print(os.listdir(directory))
    for file in os.listdir(directory):
        encoding = "utf8"
        if file == "foreigndishes.txt":
            encoding = "iso-8859-1"
        with open(directory + "/" + str(file), "r", encoding=encoding) as f:
            book = Book(f)
            frequencies = get_word_frequencies(book.text())
            for word in frequencies.keys():
                if word not in corpus:
                    corpus.append(word)
    user_vector = user_book.make_vector(corpus)



    for file in os.listdir(directory):
        with open(directory + "/" + str(file), "r") as f:

            data_vector = book.make_vector(corpus)
            similarity_num = similarity(user_vector,data_vector)
            if similarity_num > greatest_sim_num:
                greatest_sim_num = similarity_num
                greatest_author = book.author()
                greatest_title = book.title()

    return "You may be interested in " + str(greatest_title) + " by " + str(greatest_author) + "!"
