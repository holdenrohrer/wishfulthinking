from types import TracebackType
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from book import Book
import re
import json

from process_frequencies import get_word_frequencies
from remove_copyright import process_file

def get_genres_from_web(book_title):
    genre_text = []
    try:
        # requires chromedriver.exe in the same directory
        with webdriver.Chrome(executable_path = 'chromedriver.exe') as driver:
            # gets HTML
            driver.get("https://en.wikipedia.org/wiki/Special:Search?search="+book_title)
            url = driver.current_url
            html = driver.page_source

            # sets up BeutifulSoup
            soup = BeautifulSoup(html, 'html.parser')

            # navigates to info boxes on right hand side
            info_boxes_elem = soup.find("th", class_="infobox-label").parent

            # navigates to "Genre" info box
            while "Genre" not in str(info_boxes_elem):
                info_boxes_elem = info_boxes_elem.next_sibling
            # extracts Genres from the Wikipedia pages, delimited by ',' or '|'
            for g in re.split(',|\|', info_boxes_elem.contents[1].getText()):
                g = g.strip()
                # removes the citation marker if listed
                if '[' in g:
                    open_bracket = g.index('[')
                    close_bracket = g.index(']')
                    g = (g[0:open_bracket] + (g[close_bracket+1] if close_bracket < len(g) - 1 else ""))
                genre_text.append(g.lower())
    except Exception as e:
        # return blank array if book not found
        return []
    return genre_text, url

def get_frequency_table(book_list):
    # array that will contain the entire dataset
    table = []

    for book in book_list:
        # temporary array storying data for single book
        data = []
        title = book.title()

        # gets genre array
        (genres, url) = get_genres_from_web(title)


        # empty arrays signify the book was not found, so is skipped
        if len(genres) != 0:
            # gets word frequencies for book, and adds that
            dict = get_word_frequencies(book.text())
            data.append(dict)

            # then appends each genre
            for g in genres:
                data.append(g)
            table.append(data)

            ### json dump ###
            json_list = json.load(open("test.json","r"))
            json_list.append([{"title":title},{"url":url},dict])
            json_object = (json.dumps(json_list, indent = 4))
            with open("test.json", "w") as outfile:
                outfile.write(json_object)
    return table

books = [Book(open("TestFile.txt","r",encoding="utf-8")), Book(open("TestFile2.txt","r",encoding="utf-8"))]
freq = get_frequency_table(books)
print(freq)
