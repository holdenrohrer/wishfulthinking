#!/usr/bin/python3
import process_frequencies
import process_book
import remove_copyright
import unzip
import sys
import json

out = sys.argv[1]
n = 0
frequency = {}
paths = sys.argv[2:]
for path in paths:
    with open(path, 'rb') as f:
        try:
            frequency = process_frequencies.get_word_frequencies(process_book.read_book(remove_copyright.process_file(unzip.unzip(f))[0]), frequency)
        except Exception as ex:
            print(f"Error found in file {f}", file=sys.stderr)
            raise ex
        n += 1
        if n % 10 == 0:
            print(f"finished {n}/{len(paths)} books for file {out}", file=sys.stderr)
output = open(out, 'w')
print(json.dump(frequency), output)
