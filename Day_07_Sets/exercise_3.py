# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]

age_set = set(age)
print(len(age)) # 8
print(len(age_set)) # 5, the list has a bigger length than the set

# 2. Explain the difference between the following data types: string, list, tuple and set
# String : A string is a sequence of characters
# List : A list is an ordered collection of items, which can be of different data types
# Tuple : A tuple is similar to a list, but it is immutable
# Set : A set is an unordered collection of unique items

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words
txt = "I am a teacher and I love to inspire and teach people"
split_txt = txt.split()
print(len(split_txt)) # The original length is 12 words
set_txt = set(split_txt)
print(len(set_txt)) # There is 10 uunique words