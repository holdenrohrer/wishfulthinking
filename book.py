from collections.abc import Iterable
from typing import NewType
import string
import remove_copyright
from process_frequencies import get_word_frequencies
Punctuation = NewType('Punctuation', tuple[int, int, int, int, int])
class Book:
    __text: Iterable[str]
    __author: str = "Author Not Found"
    __title: str = "Title Not Found"
    __punctuation: Punctuation

    def make_vector(self,corpus_vector):
        vector = []
        wordTup= self.punctuation()
        iterable = self.text()
        frequencies = get_word_frequencies(iterable)
        for word in corpus_vector:
            if word in frequencies.keys():
                vector.append(frequencies[word])
            else:
                vector.append(0)
        for num in wordTup:
            vector.append(num)
        return tuple(vector)

    # typically, Iterable[str] is an unprocessed file
    def __init__(self, book: Iterable[str], basic_text = False):
        if basic_text:
            self.__text = list(book)
        else:
            preprocessedText = remove_copyright.process_file(book)
            self.__text = list(preprocessedText[0])
            self.__title = preprocessedText[1]
            self.__author = preprocessedText[2]
        self.__punctuation = None

    # Returns an iterator of the book's text
    def text(self) -> Iterable[str]:
        return self.__text

    def title(self) -> str:
        return self.__title

    def author(self) -> str:
        return self.__author

    def __build_punctuation(self) -> None:
        # Really quite ugly please fix up later
        iterable = self.text()
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

    def punctuation(self) -> Punctuation:
        if self.__punctuation == None:
            self.__punctuation = self.__build_punctuation()
        return self.__punctuation

    def comma_count(self):
        return self.punctuation()[0]

    def sentence_count(self):
        return self.punctuation()[1]

    def word_count(self):
        return self.punctuation()[2]

    def avg_word_len(self):
        return self.punctuation()[3]

    def avg_sen_len(self):
        return self.punctuation()[4]
