import math
import os

import numpy as np
import pandas as pd
from natsort import natsorted
from nltk import word_tokenize
from nltk.corpus import stopwords

# Folder Path
path = "C:\\Projects\\IR\\DocumentCollection"  # Replace it with your folder path

# Change the directory
os.chdir(path)

file_list = natsorted(os.listdir(path))

tokens_list = []

all_words = []

# Initialize the dictionary.
pos_index = {}

# Initialize the file no.
file_no = 1

# Initialize the file mapping (file_no -> file name).
file_map = {}

# Query For Test
user_query = "antony brutus"


# user input query
# user_query = input("Enter Your Query:")


# Part one
# Remove stop words in files
def preprocessing(file_path):
    with open(file_path, 'r') as f:
        word = f.read()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('to')
        all_stopwords.remove('in')
        all_stopwords.remove('where')
        text_tokens = word_tokenize(word)
        tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
        return tokens_without_sw


for file in file_list:
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
        data = preprocessing(file_path)
        tokens_list.append(data)

for token in tokens_list:
    for word in token:
        all_words.append(word)

print("'Display all tokens after preprocessing':\n")
print(tokens_list)

# 2- Create Positional index

for doc in tokens_list:
    # For index and word in the tokens.
    for idx, word in enumerate(doc):
        idx = 1
        # If term already exists in the positional index dictionary.
        if word in pos_index:
            # Increment total freq by 1.
            pos_index[word][0] = pos_index[word][0] + 1
            # Check if the term has existed in that DocID before.
            if file_no in pos_index[word][1]:
                pos_index[word][1][file_no].append(idx)

            else:
                pos_index[word][1][file_no] = [idx]
        else:
            # Initialize the list.
            pos_index[word] = []
            # The total frequency is 1.
            pos_index[word].append(1)
            # The postings list is initially empty.
            pos_index[word].append({})
            # Add doc ID to postings list.
            pos_index[word][1][file_no] = [idx]

    # Map the file no. to the file name.
    file_map[file_no] = file_list
    # Increment the file no. counter for document ID mapping
    file_no += 1

# Positional index for all tokens
print("\n'Display all Positional index for all tokens':\n")
print(pos_index)
print("\n")

# DO NOT REMOVE THIS
# Show all columns  and rows in one line
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.options.mode.chained_assignment = None

##################################################################################################
# Before insert query:

print("'Before insert query':\n")


# TF
def get_term_frequency(doc):
    words = dict.fromkeys(all_words, 0)
    for j in doc:
        words[j] += 1
    return words


term_frequency = pd.DataFrame(get_term_frequency(tokens_list[0]).values(),
                              index=get_term_frequency(tokens_list[0]).keys())
# tf dataframe
for i in range(1, len(tokens_list)):
    term_frequency[i] = get_term_frequency(tokens_list[i]).values()

term_frequency.columns = ['d' + str(i) for i in range(1, 11)]

# tf ---> results
print("\n'TF results':\n")
print(term_frequency)


# w-tf
def get_w_term_frequency(doc):
    if doc > 0:
        return math.log(doc) + 1
    return 0


for i in range(1, len(tokens_list) + 1):
    term_frequency['d' + str(i)] = term_frequency['d' + str(i)].apply(get_w_term_frequency)
# w_tf ---> results
print("\n'W-TF results':\n")
print(term_frequency)

# df and idf
df_idf = pd.DataFrame(columns=['df', 'idf'])
for i in range(len(term_frequency)):
    freq = term_frequency.iloc[i].values.sum()
    df_idf.loc[i, 'df'] = freq
    df_idf.loc[i, 'idf'] = math.log10(len(tokens_list) / float(freq))
df_idf.index = term_frequency.index
# df and idf ---> results
print("\n'DF-IDF results':\n")
print(df_idf)

# tf.idf
tf_idf = term_frequency.multiply(df_idf['idf'], axis=0)
# tf.idf ---> results
print("\n'TF-IDF results':\n")
print(tf_idf)

# docs length
doc_length = pd.DataFrame()


def get_length(doc):
    return np.sqrt(tf_idf[doc].apply(lambda x: x ** 2).sum())


for doc in tf_idf.columns:
    doc_length.loc[0, doc + ' length'] = get_length(doc)

# doc length ---> results
print("\n'Doc length results':\n")
print(doc_length)

# Normalized tf.idf
norm_tf_idf = pd.DataFrame()


def get_Normalized_tf_idf(doc, l):
    try:
        return l / doc_length[doc + ' length'].values[0]
    except:
        return 0


for doc in tf_idf.columns:
    norm_tf_idf[doc] = tf_idf[doc].apply(lambda l: get_Normalized_tf_idf(doc, l))

# Normalized tf.idf ---> results
print("\n'Normalized tf.idf results':\n")
print(norm_tf_idf)

##################################################################################################
# After insert query:

print("\nAfter insert query\n")
print("1-'Positional Index Result':\n")


# remove stop words in query
def query_preprocessing(user_query):
    for word in user_query.split():
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('to')
        all_stopwords.remove('in')
        all_stopwords.remove('where')
        tokens_without_sw = [word for word in user_query.split() if not word in all_stopwords]
        return tokens_without_sw


# function to convert list to string
def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)


final_query = query_preprocessing(user_query)
final_query = listToString(final_query)


def display_pos_index_query_result():
    for term in final_query.split():
        try:
            sample_pos_idx2 = [term, pos_index[term]]
            print(sample_pos_idx2)
        except:
            print("Not Found")


print("\n'Positional Index Result for the query':\n")
display_pos_index_query_result()


# # phrase Query
# def phrase_query(q):
#     lis = [[] for i in range(10)]
#     for term in final_query.split():
#
#         if term in pos_index.keys():
#             for key in pos_index[term][1].keys():
#
#                 if lis[key - 1]:
#
#                     if lis[key - 1][-1] == pos_index[term][1][key][0] - 1:
#                         lis[key - 1].append(pos_index[term][1][key][0])
#                 else:
#                     lis[key - 1].append(pos_index[term][1][key][0])
#     position_list = []
#     for pos, list in enumerate(lis, start=1):
#         if len(list) == len(final_query.split()):
#             position_list.append('doc' + str(pos))
#     return position_list
#
#
# print("\n'phrase Query Result for the query':\n")
#
# print(phrase_query(final_query))


def after_insert():
    query = pd.DataFrame(index=norm_tf_idf.index)

    query['tf-raw'] = [1 if i in final_query.split() else 0 for i in list(norm_tf_idf.index)]
    query['w_tf'] = query['tf-raw'].apply(lambda l: get_w_term_frequency(l))
    product = norm_tf_idf.multiply(query['w_tf'], axis=0)
    query['idf'] = df_idf['idf'] * query['w_tf']
    query['tf_idf'] = query['w_tf'] * query['idf']

    query['normalized'] = 0
    for i in range(len(query)):
        query['normalized'].iloc[i] = float(query['idf'].iloc[i]) / math.sqrt(sum(query['idf'].values ** 2))

    product2 = product.multiply(query['normalized'], axis=0)

    query = query[(query.T != 0).any()]  # To Drop rows with all zeros
    print("\n'Vector space models calculations table for the query':\n")
    print(query)

    # calculate query length
    query_length = math.sqrt(sum([i ** 2 for i in query['idf'].loc[final_query.split()]]))
    print("\n'Query length':")
    print(query_length)

    # for calculate cosine similarity scores
    cosine_scores = {}
    for doc in product2.columns:
        if 0 in product2[doc].loc[final_query.split()].values:
            pass
        else:
            cosine_scores[doc] = product2[doc].sum()
    print("\n'cosine similarity scores for matched docs':")
    print(cosine_scores)

    product_result = product2[list(cosine_scores.keys())].loc[final_query.split()]
    product_result_sum = product_result.sum()
    print("\n'product (query * matched docs):'")
    print(product_result)

    print("\n'Sum Product'")
    print(product_result_sum)

    # for returned docs
    returned_docs = sorted(cosine_scores.items(), key=lambda x: x[1], reverse=True)
    print("\n'Returned Docs':")
    for doc in returned_docs:
        print(doc[0], end=' ')
    print("\n")


print("\n'After insert query results':\n")
try:
    after_insert()
except:
    print("Query Not Found")
