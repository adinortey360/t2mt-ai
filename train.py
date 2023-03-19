import os
import sqlite3
import string

def extract_sentences_from_file(filename):
    with open(filename, 'r') as f:
        text = f.read()
        sentences = text.split('. ')
        return sentences

def extract_sentences_from_corpus(corpus_folder):
    sentences = []
    for root, dirs, files in os.walk(corpus_folder):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                file_sentences = extract_sentences_from_file(file_path)
                sentences.extend(file_sentences)
    return sentences

def find_unique_words(sentences):
    unique_words = {}
    translator = str.maketrans('', '', string.punctuation)
    for sentence in sentences:
        sentence = sentence.translate(translator)
        words = sentence.lower().split()
        for i, word in enumerate(words):
            if word not in unique_words:
                unique_words[word] = {
                    "count": 1,
                    "preceding_words": []
                }
            else:
                unique_words[word]["count"] += 1
            if i > 0:
                unique_words[word]["preceding_words"].append(words[:i])
    return unique_words

corpus_folder = "corpus"
sentences = extract_sentences_from_corpus(corpus_folder)
unique_words = find_unique_words(sentences)

# Create a new SQLite database
conn = sqlite3.connect("unique_words.db")
c = conn.cursor()

# Create a table for unique words
c.execute("CREATE TABLE unique_words (word TEXT, count INT)")

# Insert each unique word into the table
for word, data in unique_words.items():
    count = data["count"]
    c.execute("INSERT INTO unique_words VALUES (?, ?)", (word, count))

# Create a table for preceding words
c.execute("CREATE TABLE preceding_words (word TEXT, preceding_word TEXT)")

# Insert each preceding word into the table
for word, data in unique_words.items():
    preceding_words = data["preceding_words"]
    for preceding_word_list in preceding_words:
        for preceding_word in preceding_word_list:
            c.execute("INSERT INTO preceding_words VALUES (?, ?)", (word, preceding_word))

# Commit changes and close the connection
conn.commit()
conn.close()
