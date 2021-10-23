#!/usr/bin/python3
import process_frequencies
import process_book
import remove_copyright
import unzip
import os

def get_frequencies():
    n = 0
    direntries = os.listdir('zip')
    frequency = {}
    for path in direntries:
        with open('zip/'+path, 'rb') as f:
            frequency = process_frequencies.get_word_frequencies(process_book.read_book(remove_copyright.process_file(unzip.unzip(f))), frequency)
            f.close()
            n += 1
            print(f"finished {n} books")
    return frequency

print(get_frequencies())
