def processFile(bookFile):
    def processLine(line, arr):
        if line[:4] == '*** ':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    betweenStarsArr = [False] # stores state of betweenStars as a ref
    return filter(lambda line: processLine(line, betweenStarsArr), bookFile)

def punctuation(iterable):
    commaCounter = 0
    sentenceCounter = 0
    for line in iterable:
        for i in range(len(line)):
            char = line[i]
            if char == ",":
                commaCounter +=1
            if (char == "." or char == "?" or char == "!") and (line[i+1] == " " or line[i+1] == "\n") and (line[i-3:i] not in [" Mr"," Ms", " Dr", "Mrs"]):
                sentenceCounter +=1
    return (commaCounter,sentenceCounter)

file = open("TestFile.txt", "r", encoding="utf8")
print(punctuation(processFile(file)))
    

