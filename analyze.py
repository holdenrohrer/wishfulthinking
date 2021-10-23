import process_frequencies
import process_book

file_path = "test.txt"
with open(file_path, "r", encoding ="utf8") as file:
    text = list(process_book.read_book(file))

print(process_frequencies.get_word_frequencies(text))