import string
import re
from itertools import chain

def read_book(file):
    return chain.from_iterable(map(process_line, file))

def process_line(line):
    return "".join(l for l in line.lower().strip() if l not in string.punctuation+"\u201c\u201d\u2019\u2014").split()
