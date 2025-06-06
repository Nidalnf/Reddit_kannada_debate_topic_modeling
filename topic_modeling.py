# topic_modeling.py

import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from gensim import corpora, models

# Download NLTK data if not already done
nltk.download('stopwords')
nltk.download('punkt')

# -------- STEP 1: LOAD COMMENTS --------
with open("comments.txt", "r", encoding="utf-8") as file:
    comments = file.readlines()

# -------- STEP 2: CLEAN TEXT --------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove links
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # remove special chars/numbers
    text = re.sub(r"\s+", " ", text).strip()  # remove extra whitespace
    return text

cleaned_comments = [clean_text(comment) for comment in comments]

# -------- STEP 3: TOKENIZE & REMOVE STOPWORDS --------
stop_words = set(stopwords.words("english"))

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    return [word for word in tokens if word not in stop_words and len(word) > 2]

tokenized_comments = [tokenize(comment) for comment in cleaned_comments]

# -------- STEP 4: CREATE DICTIONARY & CORPUS --------
dictionary = corpora.Dictionary(tokenized_comments)
corpus = [dictionary.doc2bow(text) for text in tokenized_comments]

# -------- STEP 5: APPLY LDA --------
lda_model = models.LdaModel(corpus, num_topics=4, id2word=dictionary, passes=10)

# -------- STEP 6: DISPLAY TOPICS --------
print("\n--- TOPICS FOUND ---")
for idx, topic in lda_model.print_topics(num_words=5):
    print(f"Topic {idx+1}: {topic}")
