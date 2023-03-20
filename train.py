import os
import re
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="t2mt"
)

# Create a cursor object
cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS articles (id INT AUTO_INCREMENT PRIMARY KEY, filename TEXT, paragraph TEXT, FULLTEXT(paragraph))")

# Define a function to read text files from a directory and split them into articles and paragraphs
def read_corpus(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r") as f:
                article_text = f.read()
                # Split the article into paragraphs
                paragraphs = re.split(r'\n\s*\n', article_text)
                # Insert each paragraph into the database
                for paragraph in paragraphs:
                    cursor.execute("INSERT INTO articles (filename, paragraph) VALUES (%s, %s)", (filename, paragraph))
    # Commit changes to the database
    db.commit()

# Read the corpus from the "corpus" folder
corpus_folder = "corpus"
read_corpus(corpus_folder)

# Close the database connection
db.close()
