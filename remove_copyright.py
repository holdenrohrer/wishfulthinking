def process_file(book_file):
    title = "Title Not Found"
    author = "Author Not Found"
    for line in book_file:
        if line[:7] == "Title: ":
            title = line[7:-1]
            break
    for line in book_file:
        if line[:8] == "Author: ":
            author = line[8:-1]
            break
    def process_line(line, arr):
        if line[:4] == '*** ':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    between_stars_arr = [False] # stores state of betweenStars as a ref
    return (filter(lambda line: process_line(line, between_stars_arr), book_file), title, author)
