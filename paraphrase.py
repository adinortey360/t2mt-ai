import gensim
import nltk
nltk.download('punkt')

# Tokenize input sentence
input_sentence = "What is the best way to make very good food for the public"
tokenized = nltk.word_tokenize(input_sentence.lower())

# Load pre-trained word embeddings
model = Word2Vec(tokenized, min_count=1, size=100)
s_emb = []
for w in sentence:
    if w in model:
        s_emb.append(model.get_vector(w))
    else:
        s_emb.append(np.zeros(100))


# Print vector representation of input sentence
print(s_emb)
