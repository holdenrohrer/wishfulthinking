import string
import re
from itertools import chain

def read_book(file):
    return chain.from_iterable(map(process_line, file))

def process_line(line):
    return "".join(l for l in line.lower().strip() if l not in string.punctuation + '\u2018\u2019\u201c\u201d').split()
