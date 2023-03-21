import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer

# Define the source text
source_text = "Green tea is loaded with antioxidants and nutrients that have powerful effects on the body. Studies have shown that drinking green tea can reduce inflammation in the body and help with weight loss. Green tea may lower your risk of developing type II diabetes. Green tea has also been shown to improve brain function and prevent neurodegenerative diseases like Alzheimer's and Parkinson's."

# Define the user prompt
user_prompt = "What are the benefits of green?"

# Tokenize the source text and user prompt
source_tokens = nltk.word_tokenize(source_text.lower())
user_prompt_tokens = nltk.word_tokenize(user_prompt.lower())

# Remove stop words from the source text and user prompt
stop_words = set(stopwords.words('english'))
source_words = [word for word in source_tokens if word.casefold() not in stop_words]
user_prompt_words = [word for word in user_prompt_tokens if word.casefold() not in stop_words]

# Calculate the frequency distribution of words in the source text
freq_dist = FreqDist(source_words)

# Select the sentences from the source text that are most relevant to the user prompt
sentences = sent_tokenize(source_text)
relevant_sentences = []
for sentence in sentences:
    sentence_words = nltk.word_tokenize(sentence.lower())
    sentence_words = [word for word in sentence_words if word.casefold() not in stop_words]
    relevance_score = sum([freq_dist[word] for word in sentence_words])
    relevant_sentences.append((sentence, relevance_score))
relevant_sentences = sorted(relevant_sentences, key=lambda x: x[1], reverse=True)

# Fuse the user prompt with the top relevant sentence
top_sentence = relevant_sentences[0][0]
ps = PorterStemmer()
prompt_words = [ps.stem(word) for word in user_prompt_words]
for word in prompt_words:
    if word in top_sentence:
        top_sentence = top_sentence.replace(word, "<b>" + word + "</b>")

# Generate the summary
summary = top_sentence

# Print the summary
print(summary)
