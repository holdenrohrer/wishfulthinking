import process_frequencies



def get_frequencies_by_genre(frequencies_of_documents, genres):
    frequencies_by_genre = []
    for genre in genres:
        frequencies_by_genre.append({})
    for document_data in frequencies_of_documents:
        process_frequencies.combine_frequencies([frequencies_by_genre[genres.index(document_data[1])], document_data[0]])
        
    
    return frequencies_by_genre