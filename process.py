import string
import re
from itertools import chain


def read_book(lines):
    return chain.from_iterable(map(process_line, lines))

def process_line(line):
    return "".join(l for l in line.lower().strip() if l not in string.punctuation).split()

with open("README.md", "r", encoding ="utf8") as file:
    print(list(read_book(file)))