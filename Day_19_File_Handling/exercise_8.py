# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
import re
from collections import Counter
def find_most_repeated_words(file, n):
    with open(f"./data/{file}") as file:
        text = file.read()
    
    words = re.findall(r'\b\w+\b', text, re.I)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_repeated = word_counts.most_common(n)
    
    return most_repeated

print(find_most_repeated_words('romeo_and_juliet.txt', 10))

# Output :
# [('the', 768), ('I', 655), ('to', 566), ('and', 562), ('of', 487), ('a', 462), ('in', 342), ('is', 338), ('you', 321), ('my', 310)]