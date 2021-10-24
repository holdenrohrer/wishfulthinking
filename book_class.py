import string
#ACCEPTS PROCESSED TUPLES
class book:
    def __init__(self,bookIterator):
        self.iterator = bookIterator

# Returns an iterator of the book's text
    def text(self):
        text = self.iterator[0]
        return text

    def title(self):
        title = self.iterator[1]
        return title
    
    def author(self):
        author = self.iterator[2]
        return author
    
    def punctuation(self):
        iterable = self.iterator[0]
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

    def comma_count(self):
        wordTup = self.punctuation()
        return wordTup[0]
    
    def sentence_count(self):
        wordTup = self.punctuation()
        return wordTup[1]
    
    def word_count(self):
        wordTup = self.punctuation()
        return wordTup[2]

    def avg_word_len(self):
        wordTup = self.punctuation()
        return wordTup[3]

    def avg_sen_len(self):
        wordTup = self.punctuation()
        return wordTup[4]
    

