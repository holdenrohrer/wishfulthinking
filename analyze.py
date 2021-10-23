import process

file_path = "test.txt"
with open(file_path, "r", encoding ="utf8") as file:
    text = list(process.read_book(file))

print(process.get_word_frequencies(text))