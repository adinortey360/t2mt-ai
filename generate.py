import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Define a function to read text files from a directory and concatenate them
def read_corpus(folder_path):
    corpus_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r") as f:
                corpus_text += f.read()
    return corpus_text

# Read the corpus from the "corpus" folder
corpus_folder = "corpus"
corpus_text = read_corpus(corpus_folder)

# Split the corpus text into paragraphs
paragraphs = re.split(r'\n\s*\n', corpus_text)

# Define a function to match user input to a paragraph
def match_paragraph(input_text):
    # Remove punctuation, convert to lowercase, and tokenize the input text
    input_text = re.sub(r'[^\w\s]', '', input_text).lower()
    input_tokens = word_tokenize(input_text)
    # Remove stop words from the input tokens
    stop_words = set(stopwords.words('english'))
    input_tokens = [word for word in input_tokens if not word in stop_words]
    # Initialize variables to keep track of the best match so far
    best_match_score = 0
    best_match_paragraph = "I'm sorry, I couldn't find a paragraph that matches your query."
    # Loop through each paragraph and calculate a score based on word matches
    for paragraph in paragraphs:
        # Remove stop words from the paragraph
        paragraph_tokens = word_tokenize(paragraph)
        paragraph_tokens = [word for word in paragraph_tokens if not word in stop_words]
        # Calculate a score based on word matches
        paragraph_score = sum([1 for word in paragraph_tokens if word.lower() in input_tokens])
        if paragraph_score > best_match_score:
            best_match_score = paragraph_score
            best_match_paragraph = paragraph
    # Return the best matching paragraph
    return best_match_paragraph

# Start the chatbot
print("Hello! I'm a mental health chatbot. Please enter your query below.")
while True:
    user_input = input("you: ")
    best_match_paragraph = match_paragraph(user_input)
    print("bot:", best_match_paragraph)
