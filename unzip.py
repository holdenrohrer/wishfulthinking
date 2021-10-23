from stream_unzip import stream_unzip

def unzip(zippedStream):
    # we are strictly assuming there is only one file
    for fname, size, chunks in stream_unzip(zippedStream):
        return chunks

f = open("zip/22051.zip", 'rb')
print(list(unzip(f)))
