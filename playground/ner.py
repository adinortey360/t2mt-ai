import nltk
from nltk.tokenize import word_tokenize

text = "John lives in New York City and works at Microsoft. He was born on January 1st, 1990."
tokens = word_tokenize(text)
tagged = nltk.pos_tag(tokens)

named_entities = []
current_entity = []
for i in range(len(tagged)):
    # Rule 1: Check for consecutive proper nouns
    if tagged[i][1] == 'NNP':
        current_entity.append(tagged[i][0])
    elif current_entity:
        # Rule 2: Check for proper nouns followed by a preposition and another proper noun
        if i < len(tagged) - 2 and tagged[i][1] == 'IN' and tagged[i+1][1] == 'NNP' and tagged[i+2][1] == 'NNP':
            current_entity.append(tagged[i][0])
            current_entity.append(tagged[i+1][0])
            current_entity.append(tagged[i+2][0])
            named_entities.append((' '.join(current_entity), 'Location'))
            current_entity = []
        # Rule 3: Check for personal titles followed by a proper noun
        elif i < len(tagged) - 1 and tagged[i][1] == 'NNP' and (tagged[i-1][0].lower() in ['mr.', 'ms.', 'mrs.'] or tagged[i-2][0].lower() in ['dr.', 'prof.']):
            current_entity.append(tagged[i-1][0])
            current_entity.append(tagged[i][0])
            named_entities.append((' '.join(current_entity), 'Person'))
            current_entity = []
        else:
            named_entities.append((' '.join(current_entity), 'Person'))
            current_entity = []
    # Rule 4: Check for numeric dates in format MM/DD/YYYY or YYYY-MM-DD
    elif tagged[i][1] == 'CD' and (len(tagged[i][0]) == 10 or len(tagged[i][0]) == 8) and (tagged[i][0][2] == '/' or tagged[i][0][4] == '-'):
        named_entities.append((tagged[i][0], 'Date'))

if current_entity:
    named_entities.append((' '.join(current_entity), 'Person'))

print(named_entities)
