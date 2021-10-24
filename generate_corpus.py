#!/usr/bin/python3
import process_frequencies
import process_book
import remove_copyright
import unzip
import os
import sys

out = sys.argv[1]
n = 0
frequency = {}
for path in sys.argv[2:]:
    with open(path, 'rb') as f:
        try:
            frequency = process_frequencies.get_word_frequencies(process_book.read_book(remove_copyright.process_file(unzip.unzip(f))[0]), frequency)
        except Exception as ex:
            print(f"Error found in file {f}", file=sys.stderr)
            raise ex
        n += 1
        print(f"finished {n} books", file=sys.stderr)
output = open(out, 'w')
print(frequency, file=output)
