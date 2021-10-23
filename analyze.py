import process_frequencies
import process_book
import naive_bayes
import process_data
import os

genres = ["science fiction", "mystery", "romance", "fantasy", "nonfiction"]
texts = []
document_frequencies = []
files = []
directory = './archive'
for file in os.listdir(directory):
    encoding = "utf8"
    if file == "foreigndishes.txt":
        encoding = "iso-8859-1"
    with open(directory + "/" + str(file), "r", encoding =encoding) as file:
        files.append(file)
        try:
            text = list(process_book.read_book(file))
        except Exception as ex:
            print(file)
            raise ex
        texts.append(text)
        document_frequencies.append([process_frequencies.get_word_frequencies(text)])

document_frequencies[0].append("humour")
document_frequencies[1].append("horror")
document_frequencies[2].append("gothic")
document_frequencies[3].append("epic poetry")
document_frequencies[4].append("fiction")
document_frequencies[5].append("romance")
document_frequencies[6].append("")
document_frequencies[7].append("")
document_frequencies[8].append("")
document_frequencies[9].append("")
document_frequencies[10].append("")
document_frequencies[11].append("")
document_frequencies[12].append("")
document_frequencies[13].append("")
document_frequencies[14].append("")
document_frequencies[15].append("")
document_frequencies[16].append("")
document_frequencies[17].append("")


genres = []
for document_data in document_frequencies:
    for genre in document_data[1:]:
        if genre not in genres:
            genres.append(genre)



frequencies_by_genre = process_data.get_frequencies_by_genre(document_frequencies, genres)
#print(frequencies_by_genre)
naive_bayes.naive_bayes_implement(frequencies_by_genre, genres)
