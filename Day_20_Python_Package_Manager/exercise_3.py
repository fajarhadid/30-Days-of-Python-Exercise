import requests
from collections import Counter

countries_api = 'https://restcountries.com/v3.1/all'
response = requests.get(countries_api)
countries_data = response.json()

country_areas = []
languages = []
for country in countries_data:
    name = country.get('name', {}).get('common')
    area = country.get('area')
    if name and area:
        country_areas.append((name, area))
    if 'languages' in country:
        for lang in country['languages'].values():
            languages.append(lang)

largest_countries = sorted(country_areas, key=lambda x: x[1], reverse=True)[:10]
for country, area in largest_countries:
    print(f"Country: {country}, Area: {area}")

print("=" * 30)

language_counts = Counter(languages)
most_spoken_language = language_counts.most_common(10)
for language, count in most_spoken_language:
    print(f"Language: {language}, Count: {count}")

print("=" * 30)

languages = set(languages)
total_languages = len(languages)
print(f"Total Number of Languages: {total_languages}")