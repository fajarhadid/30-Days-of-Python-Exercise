# 1. Explain the difference between map, filter, and reduce
# Map : Transforms each element in a collection (like a list or array) into a new collection by applying a function.
# Filter : Creates a new collection containing only the elements that meet a certain condition.
# Reduce : Combines all elements in a collection into a single cumulative result by applying a function that takes two arguments.

# 2. Explain the difference between higher order function, closure and decorator
# Higher-Order Function : A higher-order function is a function that either takes one or more functions as arguments or returns a function as its result.
# Closure : A closure is a function that captures the lexical scope in which it was defined, allowing it to remember the variables from that scope even when the function is executed outside that scope.
# Decorator : A decorator is a specific type of higher-order function that takes another function as an argument and extends or alters its behavior, returning a new function.

# 3. Define a call function before map, filter or reduce, see examples.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(x):
    return x ** 2

squared_numbers = map(square, numbers)
print(list(squared_numbers))

def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

from functools import reduce
def add(x, y):
    return x + y

total = reduce(add, numbers)
print(total)

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)