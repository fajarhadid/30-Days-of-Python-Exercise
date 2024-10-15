# 1. Clean the following text. After cleaning, count three most frequent words in the string.
import re
from collections import Counter
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(txt):
    cleaned = re.sub(r'[^a-zA-Z0-9\s.,!?\'"]+', '', txt)
    print(cleaned)

clean_text(sentence)

def most_frequent_words(txt):
    cleaned_sentence = re.sub(r'[^a-zA-Z0-9\s.,!?\'"]+', '', txt)
    words = re.findall(r'\b\w+\b', cleaned_sentence, re.I)
    word_count = Counter(words)
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:3]

    print(sorted_word_count)

most_frequent_words(sentence)