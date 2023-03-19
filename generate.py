import os
import re
import numpy as np
import gensim.downloader as api

# Download pre-trained GloVe embeddings
glove_model = api.load("glove-wiki-gigaword-100")

# Read in the corpus text file
corpus_dir = "corpus/"
corpus_files = [os.path.join(corpus_dir, f) for f in os.listdir(corpus_dir)]
corpus_text = ""
for corpus_file in corpus_files:
    with open(corpus_file, "r") as f:
        corpus_text += f.read()

# Preprocess the corpus text
corpus_text = re.sub(r"[^a-zA-Z0-9\s]", "", corpus_text)  # remove punctuation
corpus_text = corpus_text.lower()  # convert to lowercase

# Build the vocabulary
words = corpus_text.split()
unique_words = sorted(set(words))
vocab_size = len(unique_words)
word_to_idx = {word: idx for idx, word in enumerate(unique_words)}

# Build the embeddings matrix
embedding_dim = glove_model.vector_size
embeddings = np.zeros((vocab_size, embedding_dim))
for word, idx in word_to_idx.items():
    try:
        embeddings[idx] = glove_model[word]
    except KeyError:
        pass

# Define a function to get the embedding for a word
def get_embedding(word):
    idx = word_to_idx[word]
    return embeddings[idx]

# Define a function to predict the next word given an input text
def predict_next_word(input_text):
    input_words = input_text.split()
    num_input_words = len(input_words)
    if num_input_words == 0:
        return ""
    elif num_input_words == 1:
        prev_word = input_words[0]
        next_word = "like" if prev_word in ["i", "you", "he", "she", "it", "we", "they"] else ""
    else:
        prev_word = input_words[-1]
        prev_embedding = get_embedding(prev_word)
        similarities = embeddings.dot(prev_embedding)
        similarities[word_to_idx[prev_word]] = -np.inf
        max_idx = np.argmax(similarities)
        next_word = unique_words[max_idx]
    return next_word


input_text = "every pet"
max_length = 10
for i in range(max_length):
    next_word = predict_next_word(input_text)
    if next_word == "":
        break
    input_text += " " + next_word
print(f"The generated sequence is '{input_text}'.")
