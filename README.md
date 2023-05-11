# Data Storage and Information Retrieval

This is a Python project that performs tokenization, stop word removal, positional indexing, phrase query searching, term frequency-inverse document frequency (TF-IDF) calculation, cosine similarity computation, and document ranking. The project consists of three parts, each of which is described in detail below.

## Part 1: Tokenization and Stop Word Removal

This part reads 10 text files and applies tokenization to each file to split it into individual words. Stop words are also removed from the text, except for the words "in" and "to".

## Part 2: Positional Indexing and Phrase Query Searching

The second part of the project builds a positional index for the text files and displays each term with the number of documents containing the term, as well as the positions of the term in each document. The system also allows users to search for a phrase in the text using the positional index, and returns the documents that match the query.

## Part 3: TF-IDF Calculation, Cosine Similarity Computation, and Document Ranking

The final part of the project computes the term frequency and inverse document frequency for each term in each document, and displays the resulting TF-IDF matrix. The system then computes the cosine similarity between the query and each matched document, and ranks the documents based on their similarity to the query.

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine.
2. Install any required dependencies.
3. Run the main.py script to execute the project.

## Technologies

- Python
- numpy
- pandas
- nltk

#### Output

### Term Frequency (TF)

| Term      | d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 | d9 | d10 |
|-----------|----|----|----|----|----|----|----|----|----|-----|
| antony    | 1  | 1  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0   |
| brutus    | 1  | 1  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0   |
| caeser    | 1  | 1  | 0  | 1  | 1  | 1  | 0  | 0  | 0  | 0   |
| calpurnia | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0   |
| cleopatra | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0   |
| mercy     | 1  | 0  | 1  | 1  | 1  | 1  | 0  | 0  | 0  | 0   |
| worser    | 1  | 0  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 0   |
| angels    | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 0   |
| fools     | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| fear      | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 1   |
| in        | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| rush      | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| to        | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| tread     | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| where     | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |

### Inverse Document Frequency (IDF)

### w-tf(1+ log tf) Results

| Term     | d1 | d2 | d3 | d4 | d5 | d6 | d7 | d8 | d9 | d10 |
|----------|----|----|----|----|----|----|----|----|----|-----|
| antony   | 1  | 1  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0   |
| brutus   | 1  | 1  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0   |
| caeser   | 1  | 1  | 0  | 1  | 1  | 1  | 0  | 0  | 0  | 0   |
| calpurnia| 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0   |
| cleopatra| 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0   |
| mercy    | 1  | 0  | 1  | 1  | 1  | 1  | 0  | 0  | 0  | 0   |
| worser   | 1  | 0  | 1  | 1  | 1  | 0  | 0  | 0  | 0  | 0   |
| angels   | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 0   |
| fools    | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| fear     | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 1   |
| in       | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| rush     | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| to       | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| tread    | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |
| where    | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1  | 1   |

### DF-IDF Results

| Term     | df | idf        |
|----------|----|-----------|
| antony   | 3  | 0.5228787 |
| brutus   | 3  | 0.5228787 |
| caeser   | 5  | 0.30103   |
| calpurnia| 1  | 1         |
| cleopatra| 1  | 1         |
| mercy    | 5  | 0.30103   |
| worser   | 4  | 0.39794   |
| angels   | 3  | 0.5228787 |
| fools    | 4  | 0.39794   |
| fear     | 3  | 0.5228787 |
| in       | 4  | 0.39794   |
| rush     | 4  | 0.39794   |
| to       | 4  | 0.39794   |
| tread    | 4  | 0.39794   |
| where    | 4  | 0.39794   |

### TF.IDF Results

| Term     | d1        | d2        | d3        | d4        | d5        | d6        | d7        | d8        | d9        | d10       |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| antony   | 0.5228787 | 0.5228787 | 0         | 0         | 0         | 0.5228787 | 0         | 0         | 0         | 0         |
| brutus   | 0.5228787 | 0.5228787 | 0         | 0.5228787 | 0         | 0         | 0         | 0         | 0         | 0         |
| caeser   | 0.30103   | 0.30103   | 0         | 0.30103   | 0.30103   | 0.30103   | 0         | 0         | 0         | 0         |
| calpurnia| 0         | 1         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| cleopatra| 1         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| mercy    | 0.30103   | 0         | 0.30103   | 0.30103   | 0.30103   | 0.30103   | 0         | 0         | 0         | 0         |
| worser   | 0.39794   | 0         | 0.39794   | 0.39794   | 0.39794   | 0         | 0         | 0         | 0         | 0         |
| angels   | 0         | 0         | 0         | 0         | 0         | 0         | 0.5228787 | 0.5228787 | 0.5228787 | 0         |
| fools    | 0         | 0         | 0         | 0         | 0         | 0         | 0.39794   | 0.39794   | 0.39794   | 0.39794   |
| fear     | 0         | 0         | 0         | 0         | 0         | 0         | 0.5228787 | 0.5228787 | 0         | 0.5228787 |
| in       | 0         | 0         | 0         | 0         | 0         | 0         | 0.39794   | 0.39794   | 0.39794   | 0.39794   |
| rush     | 0         | 0         | 0         | 0         | 0         | 0         | 0.39794   | 0.39794   | 0.39794   | 0.39794   |
| to       | 0         | 0         | 0         | 0         | 0         | 0         | 0.39794   | 0.39794   | 0.39794   | 0.39794   |
| tread    | 0         | 0         | 0         | 0         | 0         | 0         | 0.39794   | 0.39794   | 0.39794   | 0.39794   |
| where    | 0         | 0         | 0         | 0         | 0         | 0         | 0.39794   | 0.39794   | 0.39794   | 0.39794   |

### Document Length

| Document | Length    |
|----------|-----------|
| d1       | 1.3734623 |
| d2       | 1.2796185 |
| d3       | 0.4989743 |
| d4       | 0.782941  |
| d5       | 0.5827473 |
| d6       | 0.6742702 |
| d7       | 1.2234958 |
| d8       | 1.2234958 |
| d9       | 1.1061373 |
| d10      | 1.1061373 |

### Normalized TF.IDF

| Term     | d1        | d2        | d3        | d4        | d5        | d6        | d7        | d8        | d9        | d10       |
|----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| antony   | 0.3807012 | 0.4086208 | 0         | 0         | 0         | 0.7754736 | 0         | 0         | 0         | 0         |
| brutus   | 0.3807012 | 0.4086208 | 0         | 0.6678393 | 0         | 0         | 0         | 0         | 0         | 0         |
| caeser   | 0.219176  | 0.2352498 | 0         | 0.3844862 | 0.5165704 | 0.4464531 | 0         | 0         | 0         | 0         |
| calpurnia| 0         | 0.7814829 | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| cleopatra| 0.728087  | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         | 0         |
| mercy    | 0.219176  | 0         | 0.6032976 | 0.3844862 | 0.5165704 | 0.4464531 | 0         | 0         | 0         | 0         |
| worser   | 0.2897349 | 0         | 0.7975161 | 0.5082631 | 0.682869  | 0         | 0         | 0         | 0         | 0         |
| angels   | 0         | 0         | 0         | 0         | 0         | 0         | 0.4273646 | 0.4273646 | 0.4727069 | 0         |
| fools    | 0         | 0         | 0         | 0         | 0         | 0         | 0.3252484 | 0.3252484 | 0.3597564 | 0.3597564 |
| fear     | 0         | 0         | 0         | 0         | 0         | 0         | 0.4273646 | 0.4273646 | 0         | 0.4727069 |
| in       | 0         | 0         | 0         | 0         | 0         | 0         | 0.3252484 | 0.3252484 | 0.3597564 | 0.3597564 |
| rush     | 0         | 0         | 0         | 0         | 0         | 0         | 0.3252484 | 0.3252484 | 0.3597564 | 0.3597564 |
| to       | 0         | 0         | 0         | 0         | 0         | 0         | 0.3252484 | 0.3252484 | 0.3597564 | 0.3597564 |
| tread    | 0         | 0         | 0         | 0         | 0         | 0         | 0.3252484 | 0.3252484 | 0.3597564 | 0.3597564 |
| where    | 0         | 0         | 0         | 0         | 0         | 0         | 0.3252484 | 0.3252484 | 0.3597564 | 0.3597564 |

---

## Contact

If you have any questions or feedback about the Employment Dashboard, please feel free to contact us:

- Email:
---

© 2022 Data Storage and Information Retrieval. All rights reserved.
