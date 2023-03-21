import os
import re
import mysql.connector
import spacy

# Load the spaCy NER model
nlp = spacy.load("en_core_web_sm")

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="t2mt"
)

# Create a cursor object
cursor = db.cursor()

# Define the database schema
cursor.execute("CREATE TABLE IF NOT EXISTS articles (id INT AUTO_INCREMENT PRIMARY KEY, filename TEXT, paragraph TEXT, entities TEXT, FULLTEXT(paragraph, entities))")

# Define a function to read text files from a directory and split them into articles and paragraphs
def read_corpus(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r") as f:
                article_text = f.read()
                # Split the article into paragraphs
                paragraphs = re.split(r'\n\s*\n', article_text)
                # Extract named entities from each paragraph using spaCy
                for paragraph in paragraphs:
                    doc = nlp(paragraph)
                    # Extract the named entities and their tags
                    entities = [(ent.text, ent.label_) for ent in doc.ents]
                    # Insert each paragraph and its entities into the database
                    cursor.execute("INSERT INTO articles (filename, paragraph, entities) VALUES (%s, %s, %s)", (filename, paragraph, entities))
    # Commit changes to the database
    db.commit()

# Read the corpus from the "corpus" folder
corpus_folder = "corpus"
read_corpus(corpus_folder)

# Close the database connection
db.close()
