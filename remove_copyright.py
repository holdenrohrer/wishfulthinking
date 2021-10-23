def process_file(book_file):
    def process_line(line, arr):
        if line[:4] == '*** ':
            arr[0] = not arr[0]
            return False # if cur line's stars, don't return
        return arr[0]
    between_stars_arr = [False] # stores state of betweenStars as a ref
    return filter(lambda line: process_line(line, between_stars_arr), book_file)