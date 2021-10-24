import process_frequencies
from typing import NewType
from itertools import islice

def get_frequencies_by_genre(frequencies_of_books, genres, genres_of_books):
    bookdata = zip(frequencies_of_books, genres_of_books)
    frequencies_by_genre = {
        genre: process_frequencies.combine_frequencies([
            book[0]
            for book in bookdata
            if genre in book[1]
        ])
        for genre in genres
    }
    return frequencies_by_genre

Word = NewType("Word", str)
Frequencies = NewType("Frequencies", dict[Word, int])
def create_standard_words(frequencies_of_genres: list[Frequencies]) -> tuple[Word]:
    standard_words = set()
    for frequencies in frequencies_of_genres:
        standard_words.update(top_one_hundred(frequencies).keys())
    return tuple(standard_words)

def create_standard_vector(frequencies: Frequencies, standard_words: tuple[Word]) -> Frequencies:
    return [frequencies[word] if word in frequencies else 0 for word in standard_words]

def top_one_hundred(frequencies: dict[Word, int]) -> dict[Word, int]:
    return dict(islice(sorted(frequencies.items(), key=lambda item: item[1], reverse=True), 0, 100))