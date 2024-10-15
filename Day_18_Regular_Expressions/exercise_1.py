import re
from collections import Counter

# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to  develop an application what else can you love.'

# Normalize the text and find words using regex
words = re.findall(r'\b\w+\b', paragraph, re.I)

# Count the occurrences of each word
word_count = Counter(words)

# Convert to a list of tuples sorted by frequency
sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

print(sorted_word_count)

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.  Extract these numbers from this whole text and find the distance between the two furthest particles
txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction'
points = re.findall(r'-?\d+', txt)
sorted_points = list(map(int, points))
distance = max(sorted_points) - min(sorted_points)

print(points) # ['-12', '-4', '-3', '-1', '0', '4', '8']
print(sorted_points) # [-12, -4, -3, -1, 0, 4, 8]
print(distance) # 20