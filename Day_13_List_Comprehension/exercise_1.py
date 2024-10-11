# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print(negative_and_zero)

# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for sublist in list_of_lists for innerlist in sublist for number in innerlist]
print(flattened_list)

# 3. Using list comprehension create the following list of tuples:
number_list = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(number_list)

# 4. Using list comprehension create the following list of tuples:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_list = [[x.upper(), x[:3].upper(), y.upper()] for country in countries for x, y in country]
print(flat_list)

# 5. Flatten the following list to a new list:
dict_list = [{'country': x.upper(), 'city': y.upper()} for country in countries for x,y in country]
print(dict_list)

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name_list = [x + " " + y for name in names for x,y in name]
print(full_name_list)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2 : (y2 - y1) / (x2 - x1)
print(slope(1,2,3,4))
