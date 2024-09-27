# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
_thirty = 'Thirty'
_days = 'Days'
_of = 'Of'
_python = 'Python'
result = _thirty + " " + _days + " " + _of + " " + _python
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
coding = 'Coding'
_for = 'For'
_all = 'All'
result_c = coding + " " + _for + " " + _all
print(result_c)

# 3. Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"

# 4. Print the variable company using print()
print(company)

# 5. Print the length of the company string using len() method and print()
print(len(company))

# 6. Change all the characters to uppercase letters using upper() method
print(company.upper())

# 7, Change all the characters to lowercase letters using lower() method
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string
print(company[0:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods
print(company.find('Coding'))


# 11. Replace the word coding in the string 'Coding For All' to Python
company = company.replace("Coding","Python")
print(company)

# 12. Change Python for All to Python for Everyone using the replace method or other methods
company = company.replace("All","Everyone")
print(company)

# 13. Split the string 'Coding For All' using space as the separator (split())
str = 'Coding For All'
print(str.split(' '))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(str.split(","))

# 15. What is the character at index 0 in the string Coding For All.
str = 'Coding For All'
print(str[0])

# 16. What is the last index of the string Coding For All.
print(len(str)-1)

# 17. What character is at index 10 in "Coding For All" string.
print(str[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'
abr = ""
for char in company.split(' '):
    abr = abr + char[0]
print(abr)

# 19. Create an acronym or an abbreviation for the name 'Coding For All'
abr=""
for char in str.split(' '):
    abr = abr + char[0]
print(abr)

# 20. Use index to determine the position of the first occurrence of C in Coding For All
print(str.index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All
print(str.index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(str.rfind('l'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
txt = 'You cannot end a sentence with because because because is a conjunction'
print(txt.find('because'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(txt.rfind('because'))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_index = txt.index('because because because')
end_index = start_index + len('because because because')
sliced_phrase = txt[start_index:end_index]
print(sliced_phrase)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(txt.index('because'))

# 28. Does ''Coding For All' start with a substring Coding?
print(str.startswith('Coding'))

# 29. Does 'Coding For All' end with a substring coding?
print(str.endswith('coding'))

# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string
code = ' Coding For All '
print(code.strip(' '))

# 31. Which one of the following variables return True when we use the method isidentifier()
a = '30DaysOfPython'
b = 'thirty_days_of_python'
print(a.isidentifier())
print(b.isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(libraries)
print(joined_string)

# 33. Use the new line escape sequence to separate the following sentences
sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."
combined_sentences = sentence1 + '\n' + sentence2
print(combined_sentences)

# 34. Use a tab escape sequence to write the following lines
print('Name\tAge\tCountry\tCity\t')
print('Asabeneh\t250\tFinland\tHelsinki')

# 35. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of circle with radius {radius} is {area}")

# 36. Make the following using string formatting methods:
c = 8
d = 6
print(f"{c} + {d} = {c + d}")
print(f"{c} - {d} = {c - d}")
print(f"{c} * {d} = {c * d}")
print(f"{c} / {d} = {round(c / d, 2)}")
print(f"{c} % {d} = {c % d}")
print(f"{c} // {d} = {c // d}")
print(f"{c} ** {d} = {c ** d}")