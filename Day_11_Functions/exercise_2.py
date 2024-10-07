# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number
def even_and_odds(num):
    evens = 0
    odds = 0
    for i in range(num+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of evens are {evens}")
    print(f"The number of odds are {odds}")
even_and_odds(100)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
print("Factorial of 5 is",factorial(5))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(item):
    if item is None or (isinstance(item, (str, tuple, list, dict)) and len(item) == 0):
        return "It's empty"
    else:
        return"It's not empty"
print(is_empty(""))

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)
from statistics import mean,median, mode, variance, stdev
def calculate_mean(lst):
    return mean(lst)
print("Mean of the list is:", calculate_mean([15, 9, 55, 41, 35, 20, 62, 49]))

def calculate_median(lst):
    return median(lst)
print("Median of the list is:", calculate_median([4, 5, 8, 9, 10, 17]))

def calculate_mode(lst):
    return mode(lst)
print("Mode of the list is:", calculate_mode([15, 9, 55, 41, 35, 20, 62, 49, 49, 49]))

def calculate_range(lst):
    return len(lst)
print("Range of the list is:", calculate_range([5, 9, 55, 41, 35, 20, 62, 49]))

def calculate_variance(lst):
    return variance(lst)
print("Variance of the list is: ", calculate_variance([15, 9, 55, 41, 35, 20, 62, 49]))

def calculate_std(lst):
    return stdev(lst)
print("Standard Deviation of the list is: ", calculate_std([15, 9, 55, 41, 35, 20, 62, 49]))