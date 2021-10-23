def processFile(fileName):
    bookFile = open(fileName,"r", encoding = "utf8")
    def processLine(line, arr):
        if line[:3] == '***':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    betweenStarsArr = [False] # stores state of betweenStars as a ref
    return filter(lambda line: processLine(line, betweenStarsArr), bookFile)


print(list(processFile("TestFile.txt")))