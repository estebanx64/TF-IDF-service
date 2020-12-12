import numpy as np
import pandas as pd
import urllib.request
import nltk

from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer


symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
length_checker = np.vectorize(len)


def preprocessing_text(words: np.array) -> np.array:
    # Clean symbols
    for i in symbols:
        words = np.char.replace(words, i, "")

    # Remove aphostrope
    words = np.char.replace(words, "'", "")

    # Lowercase strings
    words = np.char.lower(words)

    # Remove Characters with a single letter
    arr_len = length_checker(words)
    words = words[arr_len > 1]

    return words


def tfidf_url(url: str) -> dict:
    page = urllib.request.urlopen(url)
    html_page = page.read()

    soup = BeautifulSoup(html_page, "html.parser")
    article_paragraphs = soup.find_all("p")

    article_text = ""

    for paragrahp in article_paragraphs:
        article_text += paragrahp.text

    corpus = nltk.sent_tokenize(article_text)

    corpus = preprocessing_text(corpus)

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(corpus)

    df = pd.DataFrame({
        "term": vectorizer.get_feature_names(),
        "tf-idf": np.concatenate(vectors[0].T.todense().tolist())
    })
    df = df.sort_values("tf-idf", ascending=False)
    terms = df.to_dict("records")
    return terms
