import re
import mysql.connector
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="t2mt"
)

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
    # Construct SQL query conditions
    conditions = []
    for token in input_tokens:
        conditions.append("(CONVERT(`id` USING utf8) LIKE '%" + token + "%' OR CONVERT(`filename` USING utf8) LIKE '%" + token + "%' OR CONVERT(`paragraph` USING utf8) LIKE '%" + token + "%')")
    # Join conditions with "AND" operator
    query_conditions = " AND ".join(conditions)
    # Query the database for articles that contain all of the input words
    mycursor = mydb.cursor()
    query = "SELECT paragraph FROM articles WHERE " + query_conditions
    print(query)
    mycursor.execute(query)
    result = mycursor.fetchall()
    # Loop through each article and calculate a score based on word matches
    matches = []
    for row in result:
        article_text = row[0]
        paragraphs = re.split(r'\n\s*\n', article_text)
        for paragraph in paragraphs:
            # Remove stop words from the paragraph
            paragraph_tokens = word_tokenize(paragraph)
            paragraph_tokens = [word for word in paragraph_tokens if not word in stop_words]
            # Calculate a score based on word matches
            paragraph_score = sum([1 for word in paragraph_tokens if word.lower() in input_tokens])
            if paragraph_score > 0:
                matches.append((paragraph, paragraph_score))
    # Sort the matches by score, in descending order
    matches = sorted(matches, key=lambda x: x[1], reverse=True)
    # If there is at least one match, return the best matching paragraph
    if len(matches) > 0:
        best_match_paragraph = matches[0][0]
    # Return the best matching paragraph
    return best_match_paragraph


# Start the chatbot
print("Hello! I'm T2MT. Talk to me")
while True:
    user_input = input("you: ")
    best_match_paragraph = match_paragraph(user_input)
    print("bot:", best_match_paragraph)
