import re

# Define a dictionary of articles
articles = {
    "article1": "Mental Health and Its Importance\nMental health refers to the overall psychological well-being of a person. It involves the way a person thinks, feels, and behaves. Mental health is important for everyone, as it affects our ability to cope with stress, make meaningful connections with others, and lead fulfilling lives. If you are experiencing mental health issues, it is important to seek help and support from a healthcare professional.",
    "article2": "Common Mental Health Disorders\nThere are several common mental health disorders, including depression, anxiety, and bipolar disorder. These disorders can have a significant impact on a person's quality of life, making it difficult to perform everyday tasks and maintain healthy relationships. Treatment options for these disorders include medication, therapy, and lifestyle changes.",
    "article3": "Self-Care for Mental Health\nSelf-care is an important aspect of maintaining good mental health. It involves taking care of your physical, emotional, and spiritual needs. Some self-care practices include getting enough sleep, eating a healthy diet, exercising regularly, and engaging in activities that bring you joy and fulfillment. Practicing self-care can help reduce stress, improve mood, and promote overall well-being.",
    "article4": "Stigma and Mental Health\nStigma is a major barrier to seeking help for mental health issues. It can cause people to feel ashamed or embarrassed about their symptoms, and may prevent them from seeking the care and support they need. It is important to recognize that mental health issues are common and treatable, and to promote understanding and acceptance of those who are struggling with mental health challenges."
}

# Define a function to match user input to an article
def match_article(input_text):
    # Remove punctuation and convert to lowercase
    input_text = re.sub(r'[^\w\s]', '', input_text).lower()
    # Initialize variables to keep track of the best match so far
    best_match_score = 0
    best_match_article = "I'm sorry, I couldn't find an article that matches your query."
    # Loop through each article and calculate a score based on word matches
    for article_key, article_text in articles.items():
        article_score = sum([1 for word in article_text.split() if word.lower() in input_text])
        if article_score > best_match_score:
            best_match_score = article_score
            best_match_article = article_text
    # Return the best matching article
    return best_match_article

# Test the search engine
while True:
    user_input = input("Please enter a query about mental health: ")
    best_match_article = match_article(user_input)
    print("The best article that matches your query is:\n", best_match_article)
