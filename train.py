import os

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

corpus_folder = "corpus"
sentences = extract_sentences_from_corpus(corpus_folder)
print(sentences)
