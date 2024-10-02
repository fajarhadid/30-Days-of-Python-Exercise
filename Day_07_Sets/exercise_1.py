it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Find the length of the set it_companies
print(len(it_companies)) # 7

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies) # {'Oracle', 'Twitter', 'Facebook', 'IBM', 'Google', 'Apple', 'Microsoft', 'Amazon'}

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tokopedia', 'Gojek', 'Traveloka'])
print(it_companies) # {'Apple', 'Microsoft', 'Oracle', 'Facebook', 'Google', 'Tokopedia', 'Amazon', 'Gojek', 'Traveloka', 'Twitter', 'IBM'}

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Gojek')
print(it_companies) # {'Apple', 'Microsoft', 'Oracle', 'Facebook', 'Google', 'Tokopedia', 'Amazon', 'Traveloka', 'Twitter', 'IBM'}

age_set = set(age)
print(len(age))
print(len(age_set))