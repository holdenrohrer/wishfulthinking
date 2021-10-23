import process_frequencies
import process_book
import naive_bayes
import process_data
import os

genres = ["Science Fiction", "Mystery", "Romance", "Fantasy", "Nonfiction"]file_paths = ["prideandprejudice.txt", "janeeyre.txt", "frankenstein.txt"]
texts = []
document_frequencies = []
for file in os.listdir("archive"):
    with open(file, "r", encoding ="utf8") as file:
        text = list(process_book.read_book(file))
        texts.append(text)
        document_frequencies.append([process_frequencies.get_word_frequencies(text)])




frequencies_by_genre = process_data.get_frequencies_by_genre(document_frequencies, genres)
#print(frequencies_by_genre)
naive_bayes.naive_bayes_implement(frequencies_by_genre, genres)
