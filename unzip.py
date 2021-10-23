from stream_unzip import stream_unzip

def unzip(zipped_stream):
    # we are strictly assuming there is only one file
    for fname, size, chunks in stream_unzip(zipped_stream):
        return get_lines(chunks)

def get_lines(chunky_stream):
    buffer = ""
    for chunk in chunky_stream:
        chunk = chunk.decode('utf-8')
        chunk = chunk.replace('\r\n','\n').replace('\r','\n')
        lines = [word+'\n' for word in chunk.split('\n')];
        lines[0] = buffer + lines[0]
        buffer = lines[-1]
        lines.pop(-1)
        for line in lines:
            yield line

f = open("zip/22051.zip", 'rb')
print(list(unzip(f)))
