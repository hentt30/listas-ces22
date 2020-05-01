import string
import re
from collections import OrderedDict


def cleanword(word):
    res = word.translate(str.maketrans('', '', string.punctuation))
    return res


def has_dashdash(word):
    res = word.find('--')
    if res == -1:
        return False
    else:
        return True


def extract_words(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    clean_text = regex.sub(' ', text)
    words = clean_text.split()
    clean_words = [cleanword(element.lower()) for element in words]
    return clean_words


def wordcount(element, words):
    has_element = [1 if word == element else 0 for word in words]
    return sum(has_element)


def wordset(words):
    res = []
    for word in words:

        if word not in res:
            res.append(word)
    return res


def longestword(words):
    length_list = [len(word) for word in words]
    return max(length_list)


a = wordset(["or", "a", "am", "is", "are", "be", "but",
             "am"])

print(a)
