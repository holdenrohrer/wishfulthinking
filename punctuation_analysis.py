import string

def processFile(bookFile):
    def processLine(line, arr):
        if line[:4] == '*** ':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    betweenStarsArr = [False] # stores state of betweenStars as a ref
    return filter(lambda line: processLine(line, betweenStarsArr), bookFile)

def punctuation(iterable):
    comma_counter = 0
    sentence_counter = 0
    word_counter = 0
    avg_word_len = 0
    letter_counter = 0
    for line in iterable:
        for i in range(len(line)):
            char = line[i]
            if char == ",":
                comma_counter +=1
            if (char == "." or char == "?" or char == "!") and (line[i+1] == " " or line[i+1] == "\n") and (line[i-3:i] not in [" Mr"," Ms", " Dr", "Mrs"]):
                sentence_counter +=1
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
    

