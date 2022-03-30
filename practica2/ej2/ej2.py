from textNumpy import texyNumpy
from collections import Counter

text = texyNumpy


def max_word_repeted(str=''):
    text_splited = str.split(' ')
    words_counter = list(Counter(text_splited).most_common(1)[0])
    return words_counter[0]


word = max_word_repeted(text)

print(f'la palabra mas repetida es   \'{word}\'')
