#!/usr/bin/python3
from process_frequencies import combine_frequencies
from multiprocessing import Pool, Queue
from generate_corpus import process_paths
import os
import json

splits = 8
outdir = 'output'
inputdir = 'zip'

def worker(chunk, queue):
    queue.put(process_paths(chunk))
    print("done")

files = [f'./{inputdir}/{file}' for file in list(os.listdir(inputdir))]
processes = []
chunklen = int(len(files)/splits) + 1
chunks = []
for y in range(splits):
    chunks.append(files[min(y*chunklen, len(files)):min((y+1)*chunklen, len(files))])

pool = Pool(processes = 8)
corpus = pool.map(process_paths, chunks) # list of frequencies by chunks

total = combine_frequencies(corpus)
with open("corpus", 'w') as file:
    json.dump(total, file)

vecs = []
for file in files:
    with open(file, "r") as f:
        vecs.append(Book(f).archive())
with open("vecs", "w") as f:
    json.dump(vecs, f)
