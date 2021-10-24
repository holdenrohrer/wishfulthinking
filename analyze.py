#!/usr/bin/python3
import process_frequencies
import process_book
import naive_bayes
import process_data
import remove_copyright
import unzip
import os
import itertools
import test_bayes

genres = ["science fiction", "mystery", "romance", "fantasy", "nonfiction"]
texts = []
document_frequencies = []
files = []
directory = './archive'

for file in os.listdir(directory):
    encoding = "utf8"
    if file == "foreigndishes.txt":
        encoding = "iso-8859-1"
    with open(directory + "/" + str(file), "r", encoding =encoding) as file:

        files.append(file)
        try:
            text = list(process_book.read_book(file))
        except Exception as ex:
            print(file)
            raise ex
        texts.append(text)
        document_frequencies.append(process_frequencies.get_word_frequencies(text))

def get_frequencies():
    n = 0
    direntries = os.listdir('zip')
    frequency = {}
    for path in direntries:
        with open('zip/'+path, 'rb') as f:
            frequency = process_frequencies.get_word_frequencies(process_book.read_book(remove_copyright.process_file(unzip.unzip(f))), frequency)
            f.close()
            n += 1
            print(f"finished {n} books")
    return frequency
genres_of_books = [[] for doc_freq in document_frequencies]

genres_of_books[0].append("romance")
genres_of_books[1].append("horror")
genres_of_books[2].append("horror")
genres_of_books[3].append("horror")
genres_of_books[4].append("horror")
genres_of_books[5].append("romance")
genres_of_books[6].append("nonfiction")
genres_of_books[7].append("horror")
genres_of_books[8].append("romance")
genres_of_books[9].append("romance")
genres_of_books[10].append("nonfiction")
genres_of_books[11].append("science fiction")
genres_of_books[12].append("romance")
genres_of_books[13].append("romance")
genres_of_books[13].append("horror")
genres_of_books[14].append("horror")
genres_of_books[15].append("science fiction")
genres_of_books[16].append("science fiction")




genres = []
for genres in genres_of_books:
    for genre in genres:
        if genre not in genres:
            genres.append(genre)


frequencies_by_genre = process_data.get_frequencies_by_genre(document_frequencies, genres, genres_of_books)


#naive_bayes.naive_bayes_implement(frequencies_by_genre, genres)
#process_data.create_standard_vector(frequencies_by_genre, genres)
#print(frequencies_by_genre)
test_bayes.test_bayes_implementation(frequencies_by_genre, document_frequencies, genres_of_books)