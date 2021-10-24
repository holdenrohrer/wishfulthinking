#!/usr/bin/python3
import subprocess
from parallel import build_makefile
from process_frequencies import combine_frequencies
import json

splits = 8
outdir = 'output'
build_makefile('test', splits=splits, outputdir=outdir)
subprocess.call(('make'))
corpus = []
for output in range(splits):
    with open(f'{outdir}/{output}', 'r') as file:
        corpus.append(json.load(file))
total = combine_frequencies(corpus)
with open(f'{outdir}/corpus', 'w') as out:
    json.dump(total, out)
