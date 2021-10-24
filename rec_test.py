from book import Book
from vectors import similarity
from process_frequencies import get_word_frequencies


opened_user = open("userFiletxt.txt","r")
user_file = Book(opened_user)
opened_user.close()

text_directory = ["TestFile.txt", "TestFile2.txt", "TestFile3.txt"]
corpus = []
    
greatest_sim_num = 0
for file in text_directory:
    f = open(file,"r",encoding="utf8")
    book = Book(f)
    frequencies = get_word_frequencies(book.text())
    for word in frequencies.keys():
        if word not in corpus:
            corpus.append(word)
user_vector = book.make_vector(corpus)
for file in text_directory:
    data_vector = book.make_vector(corpus)
    similarity_num = similarity(user_vector,data_vector)
    if similarity_num > greatest_sim_num:
        greatest_sim_num = similarity_num
        greatest_author = book.author()
        greatest_title = book.title()

print("You may be interested in " + greatest_title + " by " + greatest_author + "!")
