import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

class TextSummarizer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def summarize(self, text, num_sentences=3):
        # Tokenize the input text into sentences and words
        sentences = sent_tokenize(text)
        words = word_tokenize(text)

        # Remove stopwords and punctuation from the words
        words = [word for word in words if word.casefold() not in self.stop_words and word.isalpha()]

        # Compute the word frequency distribution
        freq_dist = FreqDist(words)

        # Compute the score of each sentence based on the word frequency distribution
        sent_scores = {}
        for sentence in sentences:
            sentence_words = word_tokenize(sentence)
            sentence_words = [word for word in sentence_words if word.casefold() not in self.stop_words and word.isalpha()]
            score = 0
            for word in sentence_words:
                score += freq_dist[word]
            sent_scores[sentence] = score

        # Select the top N sentences with the highest scores as the summary
        summary = ""
        for sentence, score in sorted(sent_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]:
            summary += sentence + " "

        return summary.strip()
