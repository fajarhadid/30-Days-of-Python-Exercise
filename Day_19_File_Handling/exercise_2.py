# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
def extract_email(file):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    with open(f"./data/{file}") as f:
        content = f.read()

    emails = re.findall(email_pattern, content)
    unique_emails = set(emails)
    email_list = list(unique_emails)
    return email_list

print(extract_email('email_exchanges_big.txt'))
print(len(extract_email('email_exchanges_big.txt'))) # There are 1851 unique emails

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
from collections import Counter

def find_most_common_words(file, n):
    # Open the sample txt file from the data folder
    with open(f"./data/{file}") as file:
        text = file.read()
    
    # Normalize the text to lowercase and use regex to find words
    words = re.findall(r'\b\w+\b', text, re.I)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common = word_counts.most_common(n)
    
    return most_common

print(find_most_common_words('sample_text.txt', 10))

# 6. Find ten most frequent words from the speech
def find_most_frequent_words(file, n):
    with open(f"./data/{file}") as file:
        text = file.read()
    

    words = re.findall(r'\b\w+\b', text, re.I)
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_frequent = word_counts.most_common(n)
    
    return most_frequent

print(find_most_common_words('obama_speech.txt', 10))
print(find_most_common_words('michelle_obama_speech.txt', 10))
print(find_most_common_words('donald_trump_speech.txt', 10))
print(find_most_common_words('melania_trump_speech.txt', 10))