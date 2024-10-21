# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
def lines_and_words_counter(txt):
    with open(f"./data/{txt}") as f:
        lines = f.read().splitlines()
        line_count = 0
        word_count = 0
        for line in lines:
            line_count += 1
            for word in line:
                word_count +=1
        return f"Number of lines: {line_count}\nNumber of words: {word_count}\n"

print(lines_and_words_counter('obama_speech.txt')) # lines : 66 words : 13276
print(lines_and_words_counter('michelle_obama_speech.txt')) # lines : 83 words : 11623
print(lines_and_words_counter('donald_trump_speech.txt')) # lines : 48 words : 7185
print(lines_and_words_counter('melania_trump_speech.txt')) # lines : 33 words : 7439

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json
def most_spoken_languages(file, n):
    with open(f"./data/{file}", "r", encoding="utf8") as f:
        data = f.read()
    
    country_data = json.loads(data)

    languages = []
    for country in country_data:
        if 'languages' in country:
            for lang in country['languages']:
                languages.append(lang)
    
    unique_languages = set()
    unique_languages = languages

    lang_count = {}
    for lang in unique_languages:
        lang_count[lang] = languages.count(lang)

    most_spoken = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
    return most_spoken[:n]

print(most_spoken_languages('countries_data.json', 10))

# 3 . Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries(file, n):
    with open(f"./data/{file}", "r", encoding="utf8") as f:
        data = f.read()
    
    country_data = json.loads(data)

    country_population = {}
    for country in country_data:
        if "population" in country:
            country_population[country['name']] = country['population']
    
    most_populated = sorted(country_population.items(), key=lambda x: x[1], reverse=True)
    return most_populated[:n]

print(most_populated_countries('countries_data.json', 10))