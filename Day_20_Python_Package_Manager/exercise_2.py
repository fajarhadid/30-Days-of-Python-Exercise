import requests
import numpy as np
from collections import defaultdict

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats_data = response.json()

weights = []
life_span = []
frequency_table = defaultdict(int)

for cat in cats_data:
    breed = cat.get('name')
    country = cat.get('origin')
    if 'weight' in cat:
        weight_range = cat['weight']['metric']
        if weight_range:
            min_weight, max_weight = map(float, weight_range.split(' - '))
            weights.append((min_weight + max_weight) / 2)
    if 'life_span' in cat:
        life_span_range = cat['life_span']
        if life_span_range:
            min_life_span, max_life_span = map(float, life_span_range.split(' - '))
            life_span.append((min_life_span + max_life_span) / 2)
    if breed and country:
        frequency_table[(country, breed)] += 1

min_weight = np.min(weights) # 3.0
max_weight = np.max(weights) # 7.5
mean_weight = np.mean(weights) # 4.708955223880597
median_weight = np.median(weights) # 4.5
std_weight = np.std(weights) # 1.0585446702386354
print(f"Min Weight: {min_weight}\nMax Weight: {max_weight}\nMean Weight: {mean_weight}\nMedian Weight: {median_weight}\nStandard Deviation: {std_weight}\n")

min_life_span = np.min(life_span) # 10.5
max_life_span = np.max(life_span) # 19.0
mean_life_span = np.mean(life_span) # 13.746268656716419
median_life_span = np.median(life_span) # 13.5
std_life_span = np.std(life_span) # 1.5725564658451314
print(f"Min Life Span: {min_life_span}\nMax Life Span: {max_life_span}\nMean Life Span: {mean_life_span}\nMedian Life Span: {median_life_span}\nStandard Deviation: {std_life_span}\n")

# Convert the frequency dictionary to a list for better visualization
frequency_list = [(country, breed, count) for (country, breed), count in frequency_table.items()]

# Print the frequency table
for country, breed, count in frequency_list:
    print(f"Country: {country}, Breed: {breed}, Count: {count}")