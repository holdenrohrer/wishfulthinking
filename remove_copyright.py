titlekey = "Title: "
authorkey = "Author: "

# this is only for books from a specific source that appear in the
# corpus
def is_shakespeare_start(line):
    return line.startswith("SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>")
def is_shakespeare_end(line):
    return line.startswith("<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM")

def process_file(book_file):
    title = "Title Not Found"
    author = "Author Not Found"
    between_stars = False
    iterator = iter(book_file)
    while True:
        line = next(iterator)
        if line.strip().startswith('***') and 'START' in line or is_shakespeare_start(line):
            break
        if line.strip().startswith(titlekey):
            title = line[len(titlekey):-1]
        elif line.strip().startswith(authorkey):
            author = line[len(authorkey):-1]
    return (process_after_metadata(iterator), title, author)

def process_after_metadata(iterator):
    done = False
    while True:
        try:
            line = next(iterator)
            if line.strip().startswith('***') and 'END' in line or is_shakespeare_end(line):
                done = True
            if not done:
                yield line
        except StopIteration as ex:
            break
