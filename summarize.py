import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

# Input paragraph
text = """Climate Change: Understanding the Problem and Its Impacts

Climate change is one of the most pressing issues facing our world today. It is caused by the build-up of greenhouse gases in the atmosphere, primarily carbon dioxide (CO2), that trap heat and cause the Earth's temperature to rise. This rise in temperature, known as global warming, has far-reaching impacts on the environment, ecosystems, and human societies.

The main driver of climate change is human activity, specifically the burning of fossil fuels such as coal, oil, and gas for energy. This releases large amounts of CO2 into the atmosphere, which accumulates over time and traps more heat. Other human activities that contribute to climate change include deforestation, agriculture, and industrial processes.

The impacts of climate change are wide-ranging and severe. One of the most significant impacts is the increase in extreme weather events such as heatwaves, droughts, floods, and storms. These events can cause significant damage to infrastructure, homes, and crops, and result in loss of life. They also exacerbate existing inequalities, as vulnerable populations such as low-income communities and people living in coastal areas are disproportionately affected.

Climate change also has major implications for ecosystems and biodiversity. Rising temperatures and changing weather patterns disrupt ecosystems and alter the distribution and behavior of plant and animal species. This can lead to the loss of species and habitats, and impact food security for humans who rely on these ecosystems.

In addition, climate change affects human health. Extreme heat can lead to heat stroke and other heat-related illnesses, while poor air quality caused by pollution exacerbates respiratory diseases such as asthma. Changes in the distribution of disease-carrying insects such as mosquitoes also have implications for the spread of diseases such as malaria and dengue fever.

Addressing climate change requires urgent action at all levels, from individuals to governments and international organizations. There are many ways to reduce greenhouse gas emissions and mitigate the impacts of climate change, including:

Transitioning to renewable energy sources such as wind, solar, and hydropower
Improving energy efficiency in buildings and transportation
Reducing deforestation and promoting reforestation and afforestation
Implementing sustainable agriculture and reducing food waste
Investing in research and development of new technologies to address climate change
Individuals can also take action to reduce their carbon footprint and advocate for policies that address climate change. Simple steps such as using energy-efficient light bulbs, reducing meat consumption, and using public transportation or carpooling can all make a difference.

In conclusion, climate change is a complex and urgent issue that requires immediate action. The impacts of climate change are far-reaching and have serious implications for human societies and ecosystems. Addressing climate change will require a collective effort from individuals, governments, and international organizations to reduce greenhouse gas emissions and adapt to the impacts of a changing climate."""

# Tokenize the input text into sentences and words
sentences = sent_tokenize(text)
words = word_tokenize(text)

# Remove stopwords and punctuation from the words
stop_words = set(stopwords.words('english'))
words = [word for word in words if word.casefold() not in stop_words and word.isalpha()]

# Compute the word frequency distribution
freq_dist = FreqDist(words)

# Compute the score of each sentence based on the word frequency distribution
sent_scores = {}
for sentence in sentences:
    sentence_words = word_tokenize(sentence)
    sentence_words = [word for word in sentence_words if word.casefold() not in stop_words and word.isalpha()]
    score = 0
    for word in sentence_words:
        score += freq_dist[word]
    sent_scores[sentence] = score

# Select the top N sentences with the highest scores as the summary
N = 2
summary = ""
for sentence, score in sorted(sent_scores.items(), key=lambda x: x[1], reverse=True)[:N]:
    summary += sentence + " "

# Print the summary
print(summary)
