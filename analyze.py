#!/usr/bin/python3
import process_frequencies
import process_book
import remove_copyright
import unzip
import os
import sys

def get_frequencies():
    n = 0
    direntries = os.listdir('zip')
    frequency = {}
    for path in direntries:
        with open('zip/'+path, 'rb') as f:
            try:
                frequency = process_frequencies.get_word_frequencies(process_book.read_book(remove_copyright.process_file(unzip.unzip(f))[0]), frequency)
            except Exception as ex:
                print(f"Error found in file {f}")
                raise ex
            f.close()
            n += 1
            print(f"finished {n} books", file=sys.stderr)
    return frequency

print(get_frequencies())
