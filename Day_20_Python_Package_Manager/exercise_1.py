import requests
import re
from collections import Counter
url = 'https://folger-main-site-assets.s3.amazonaws.com/uploads/2022/11/romeo-and-juliet_TXT_FolgerShakespeare.txt'

response = requests.get(url)
text = response.text

words = re.findall(r'\b\w+\b', text, re.I)
words_count = Counter(words)

most_frequent_words = words_count.most_common(10)

print(most_frequent_words)