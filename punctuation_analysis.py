<<<<<<< HEAD
import string

def processFile(bookFile):
    def processLine(line, arr):
=======
def process_file(book_file):
    def process_line(line, arr):
>>>>>>> 30772435224c39c5767fa4e835ed0e05c46a32fe
        if line[:4] == '*** ':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    between_stars_arr = [False] # stores state of betweenStars as a ref
    return filter(lambda line: process_line(line, between_stars_arr), book_file)

def punctuation(iterable):
    comma_counter = 0
    sentence_counter = 0
<<<<<<< HEAD
    word_counter = 0
    avg_word_len = 0
    letter_counter = 0
=======
>>>>>>> 30772435224c39c5767fa4e835ed0e05c46a32fe
    for line in iterable:
        for i in range(len(line)):
            char = line[i]
            if char == ",":
                comma_counter +=1
            if (char == "." or char == "?" or char == "!") and (line[i+1] == " " or line[i+1] == "\n") and (line[i-3:i] not in [" Mr"," Ms", " Dr", "Mrs"]):
                sentence_counter +=1
<<<<<<< HEAD
        if line != "\n":
            line_list = line.split()
            for word in line_list:
                letters = False
                for char in word:
                    if char in string.ascii_letters:
                        letter_counter+=1
                        letters = True
            if letters == True:
                word_counter += len(line_list)
    avg_word_len = letter_counter/word_counter
    avg_sentence_len = word_counter/sentence_counter
    return (comma_counter,sentence_counter,word_counter,avg_word_len, avg_sentence_len)

file = open("TestFile2.txt", "r", encoding="utf8")
print(punctuation(processFile(file)))
=======
    return (comma_counter,sentence_counter)

file = open("TestFile.txt", "r", encoding="utf8")
print(punctuation(process_file(file)))
>>>>>>> 30772435224c39c5767fa4e835ed0e05c46a32fe
    

