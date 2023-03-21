import re

# Define patterns for different named entity types
patterns = {
    'person': r'\b[A-Z][a-z]* [A-Z][a-z]*\b',
    'organization': r'\b[A-Z][a-z]*([ ]?[A-Z][a-z]*)*\b (Inc\.|Corp\.|Ltd\.|Co\.)',
    'location': r'\b[A-Z][a-z]*([ ]?[A-Z][a-z]*)*\b(?: [A-Z][a-z]*)*, \b[A-Z][a-z]*([ ]?[A-Z][a-z]*)*\b',
    'date': r'\b(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)?, \d{4}\b',
    'money': r'\$\d{1,3}(,\d{3})*(\.\d{2})?',
    'percentage': r'\d+(\.\d+)?%',
    'product': r'\b[A-Z][a-z]*([ ]?[A-Z][a-z]*)*\b(?: [0-9][a-z]*)*',
    'event': r'\b([A-Z][a-z]*)+ (Cup|Olympics)',
    'title': r'\b([A-Z][a-z]*)+ (Book|Movie|Music)',
    'disease': r'\b[A-Z][a-z]* [A-Z][a-z]*\b',
    'medication': r'\b[A-Z][a-z]*\b',
    'chemical': r'\b[A-Z][a-z]*(?: [A-Z][a-z]*)*\b',
    'food': r'\b[A-Z][a-z]*\b',
    'sport': r'\b[A-Z][a-z]*\b'
}

def extract_named_entities(text):
    named_entities = {}
    for entity_type, pattern in patterns.items():
        named_entities[entity_type] = re.findall(pattern, text)
    return named_entities
