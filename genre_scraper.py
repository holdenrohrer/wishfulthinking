from types import TracebackType
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from book_class import book
from process_book import read_book
import re

from process_frequencies import get_word_frequencies
from remove_copyright import process_file

def get_genres_from_web(book_title):
    genre_text = []
    try:
        # requires chromedriver.exe in the same directory
        with webdriver.Chrome(executable_path = 'chromedriver.exe') as driver:
            # gets HTML
            driver.get("https://en.wikipedia.org/wiki/Special:Search?search="+book_title)
            html = driver.page_source
            
            # sets up BeutifulSoup
            soup = BeautifulSoup(html, 'html.parser')
            
            # navigates to info boxes on right hand side
            info_boxes_elem = soup.find("th", class_="infobox-label").parent
            
            # navigates to "Genre" info box
            while "Genre" not in str(info_boxes_elem):
                info_boxes_elem = info_boxes_elem.next_sibling
            # extracts Genres listed
            for g in re.split(',|\|', info_boxes_elem.contents[1].getText()):
                g = g.strip()
                if '[' in g:
                    open_bracket = g.index('[')
                    close_bracket = g.index(']')
                    g = (g[0:open_bracket] + (g[close_bracket+1] if close_bracket < len(g) - 1 else ""))
                genre_text.append(g.lower())
    except Exception as e:
        # return blank array if book not found
        return []
    return genre_text

def get_frequency_table(book_list):
    table = []

    for book in book_list:
        data = []
        title = book.title()
        #print(title)
        
        genres = get_genres_from_web(title)
        #print(genres)
        if len(genres) != 0:
            data.append(get_word_frequencies(read_book(book.text())))
            #data.append(1)
            #print(get_word_frequencies(read_book(book.text())))
            for g in genres:
                data.append(g)
            table.append(data)
    return table
        

books = [Book(process_file(open("TestFile.txt","r",encoding="utf-8"))), Book(process_file(open("TestFile2.txt","r",encoding="utf-8")))]
freq = get_frequency_table(books)
print(freq)
#print(get_word_frequencies(read_book(books[0].text())))
#print(get_genres_from_web("Ulysses (novel)"))
#print(get_frequency_table(["TestFile.txt"]))
#book_list = [read_book(process_file(open("TestFile.txt","r",encoding="utf-8")))]
#print(list(get_frequency_table(book_list)))
#print(get_word_frequencies(read_book(process_file(open("TestFile.txt","r",encoding="utf-8"))[0])))

