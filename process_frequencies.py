import string
import re
from itertools import chain
from collections.abc import Iterable
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
    'you', "you're", "you've", "you'll", "you'd", 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
    "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
    'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am',
    'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
    'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a',
    'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as',
    'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against', 'between', 'into', 'through', 'during', 'before',
    'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in',
    'out', 'on', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why',
    'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
    'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
    'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will',
    'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll',
    'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
    "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't",
    'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
    "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
    'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won',
    "won't", 'wouldn', "wouldn't"]

def get_word_frequencies(text: Iterable[str], frequencies=None) -> dict[str, int]:
    wordlist = __read_book(text)
    if frequencies == None:
        frequencies = {}
    for word in wordlist:
        if (word in frequencies):
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    return __remove_stop_words(frequencies)

def __read_book(file):
    return chain.from_iterable(map(__process_line, file))

def __process_line(line):
    return "".join(l for l in line.lower().strip() if l not in string.punctuation+"\u201c\u201d\u2019\u2014").split()

def __remove_stop_words(word_freqs):
    for word in stop_words:
        if word in word_freqs.keys():
            word_freqs.pop(word)
    return word_freqs

def combine_frequencies(list_of_frequencies):
    final_frequencies = list_of_frequencies.pop(0)
    for frequencies in list_of_frequencies:
        for word in frequencies.keys():
            if word in final_frequencies.keys():
                final_frequencies[word] += frequencies[word]
            else:
                final_frequencies[word] = frequencies[word]
    return final_frequencies
