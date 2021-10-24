from stream_unzip import stream_unzip

def unzip(zipped_stream):
    # we are strictly assuming there is only one file
    for fname, size, chunks in stream_unzip(zipped_stream):
        if fname.endswith(b'.txt'):
            return get_lines(chunks)
        else:
            for chunk in chunks:
                pass

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
                    given = line[len(header):].upper().replace(b'\n', b'')
                    if given.startswith(b'UTF-8') or given.startswith(b'UTF\xe2\x80\x908') or given.startswith(b'UNICODE UTF-8'):
                        encoding = 'utf-8'
                    elif given.startswith(b'ISO-8859-1') or given.startswith(b'ISO 8859-1') or given.startswith(b'ISO LATIN-1') or given.startswith(b'ISO-LATIN-1') or given.startswith(b'LATIN1') or given.startswith(b'LATIN-1') or given.startswith(b'ACII, WITH SOME ISO-8859-1 CHARACTERS') or given.startswith(b'ISO8859_1'):
                        encoding = 'iso-8859-1'
                    elif given.startswith(b'ASCII') or given.startswith(b'ISO-646-US') or given.startswith(b'US-ASCII') or given.startswith(b'ASCI'):
                        encoding = 'ascii'
                    elif given.startswith(b'WINDOWS CODE PAGE 1252') or given.startswith(b'WINDOWS-1252') or given.startswith(b'CP-1252'):
                        encoding = 'windows-1252'
                    else:
                        raise Exception(f"Unknown encoding {given}")
                    encoding_known = True
            yield line.decode(encoding, 'ignore')
