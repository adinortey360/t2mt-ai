import nltk
import random

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.corpus import wordnet

def get_wordnet_pos(tag):
    if tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def paraphrase_sentence(sentence):
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    paraphrase_tokens = []
    for word, tag in tags:
        wn_tag = get_wordnet_pos(tag) or wordnet.NOUN
        synsets = wordnet.synsets(word, pos=wn_tag)
        if synsets:
            synset = random.choice(synsets)
            lemma = synset.lemmas()[0]
            paraphrase = lemma.name().replace('_', ' ').lower()
            if paraphrase != word:
                paraphrase_tokens.append(paraphrase)
            else:
                paraphrase_tokens.append(word)
        else:
            paraphrase_tokens.append(word)
    paraphrased_sentence = " ".join(paraphrase_tokens)

    return paraphrased_sentence


sentence = "What is the best way to make very good food for the public"
paraphrase = paraphrase_sentence(sentence)
print("Original sentence: ", sentence)
print("Paraphrase: ", paraphrase)
