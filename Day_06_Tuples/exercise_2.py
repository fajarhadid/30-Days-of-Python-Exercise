# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('Orange', 'Banana', 'Grape')
vegetables = ('Cucumber', 'Tomato', 'Chili')
animal_products = ('Milk', 'Egg', 'Honey')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
print(food_stuff_lt[4])

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3]) # ['Orange', 'Banana', 'Grape']
print(food_stuff_lt[-3:]) # ['Milk', 'Egg', 'Honey']

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) # False

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries) # True