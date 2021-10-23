from stream_unzip import stream_unzip

def unzip(zipped_stream):
    # we are strictly assuming there is only one file
    for fname, size, chunks in stream_unzip(zipped_stream):
        return get_lines(chunks)

header = b"Character set encoding: "
def get_lines(chunky_stream):
    buffer = b""
    encoding = 'utf-8'
    encoding_known = False # assumed to be utf-8 until proven otherwise
    for chunk in chunky_stream:
        chunk = chunk.replace(b'\r\n',b'\n').replace(b'\r',b'\n')
        lines = [word+b'\n' for word in chunk.split(b'\n')];
        lines[0] = buffer + lines[0]
        buffer = lines[-1]
        lines.pop(-1)
        for line in lines:
            if not encoding_known:
                if line.startswith(header):
                    given = line[len(header):].upper()
                    if given.startswith(b'UTF-8'):
                        encoding = 'utf-8'
                    elif given.startswith(b'ISO-8859-1') or given.startswith(b'ISO LATIN-1'):
                        encoding = 'iso-8859-1'
                    elif given.startswith(b'ASCII') or given.startswith(b'ISO-646-US') or given.startswith(b'US-ASCII'):
                        encoding = 'ascii'
                    else:
                        raise Exception(f"Unknown encoding {given}")
                    encoding_known = True
            yield line.decode(encoding, 'ignore')
