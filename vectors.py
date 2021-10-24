import math
import numpy as np

def similarity(user_vector,database_vector):
    dict_weight = 100000
    comma_weight = 1
    num_sentence_weight = 1
    num_word_weight = 1
    avg_word_len_weight = 1
    avg_sentence_weight = 1
    comma_dot = comma_weight * user_vector[-5] * database_vector[-5]
    num_sentence_dot = num_sentence_weight * user_vector[-4] * database_vector[-4]
    num_word_dot = num_word_weight * user_vector[-3] * database_vector[-3]
    avg_word_dot = avg_word_len_weight * user_vector[-2] * database_vector[-2]
    avg_sen_dot = avg_sentence_weight * user_vector[-1] * database_vector[-1]

    user_vector_dicts = user_vector[:-6]
    database_vector_dicts = database_vector[:-6]
    dot_product = dict_weight * np.dot(user_vector_dicts, database_vector_dicts) + comma_dot + num_sentence_dot + num_word_dot + avg_word_dot + avg_sen_dot

    magnitude_user = np.sqrt(dict_weight**2 * np.dot(user_vector_dicts, user_vector_dicts) + (comma_weight * user_vector[-5])**2 + (num_sentence_weight * user_vector[-4])**2 + (num_word_weight * user_vector[-3])**2 + (avg_word_len_weight* user_vector[-2])**2 + (avg_sentence_weight * user_vector[-1])**2)
    magnitude_database = np.sqrt(dict_weight * np.dot(database_vector_dicts, database_vector_dicts) + (comma_weight * database_vector[-5])**2 + (num_sentence_weight * database_vector[-4])**2 + (num_word_weight * database_vector[-3])**2 + (avg_word_len_weight* database_vector[-2])**2 + (avg_sentence_weight * database_vector[-1])**2)
    
    similarity = dot_product/(magnitude_user*magnitude_database)
    return similarity





