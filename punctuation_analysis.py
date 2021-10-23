def process_file(book_file):
    def process_line(line, arr):
        if line[:4] == '*** ':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    between_stars_arr = [False] # stores state of betweenStars as a ref
    return filter(lambda line: process_line(line, between_stars_arr), book_file)

def punctuation(iterable):
    comma_counter = 0
    sentence_counter = 0
    for line in iterable:
        for i in range(len(line)):
            char = line[i]
            if char == ",":
                comma_counter +=1
            if (char == "." or char == "?" or char == "!") and (line[i+1] == " " or line[i+1] == "\n") and (line[i-3:i] not in [" Mr"," Ms", " Dr", "Mrs"]):
                sentence_counter +=1
    return (comma_counter,sentence_counter)

file = open("TestFile.txt", "r", encoding="utf8")
print(punctuation(process_file(file)))
    

