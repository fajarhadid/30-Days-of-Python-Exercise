# 1. Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def change_to_upper(country):
    return country.upper()

countries_upper_case = map(change_to_upper, countries)
print(list(countries_upper_case))

# 2. Use map to create a new list by changing each number to its square in the numbers list
def square(x):
    return x ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

# 3. Use map to change each name to uppercase in the names list
def name_to_upper(name):
    return name.upper()

names_upper_case = map(name_to_upper, names)
print(list(names_upper_case))

# 4. Use filter to filter out countries containing 'land'
def is_contain_land(country):
    if 'land' in country:
        return True
    return False

land_country = filter(is_contain_land, countries)
print(list(land_country))

# 5. Use filter to filter out countries having exactly six characters
def six_char_country(country):
    if len(country) == 6:
        return True
    return False

six_character_country = filter(six_char_country, countries)
print(list(six_character_country))

# 6. Use filter to filter out countries containing six letters and more in the country list
def six_or_more_char_country(country):
    if len(country) >= 6:
        return True
    return False

long_country_name = filter(six_or_more_char_country, countries)
print(list(long_country_name))

# 7, Use filter to filter out countries starting with an 'E'
def start_with_e(country):
    if country[0] == 'E':
        return True
    return False

e_country = filter(start_with_e, countries)
print(list(e_country))

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
def is_odd(x):
    return x % 2 != 0

def add(x, y):
    return x + y

result = reduce(add, filter(is_odd, map(square, numbers)))
print(result)

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items
def get_string_lists(lst):
    string_items = list(filter(lambda x: isinstance(x, str), lst))
    return string_items

example_list = [1, "A", 3, "B", 4, 5, "C"]
print(get_string_lists(example_list))

# 10. Use reduce to sum all the numbers in the numbers list
def sum_numbers(x, y):
    return x + y

total = reduce(add, numbers)
print(total)

# 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenate(c1, c2):
    return f"{c1}, {c2}"

country_string = reduce(concatenate, countries[:-1])
result = f"{country_string}, and {countries[-1]} are north European countries."
print(result)