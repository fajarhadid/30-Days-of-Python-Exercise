# 1. Write a function called is_prime, which checks if a number is prime
def is_prime(num):
    if num == 0 or num == 1:
        print(f"{num} is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
            else:
                print(f"{num} is a prime number")
                break
is_prime(5)

# 2. Write a functions which checks if all items are unique in the list
def is_unique(lst):
    return len(lst) == len(set(lst))
print(is_unique([1,2,3,4]))

# 3. Write a function which checks if all the items of the list are of the same data type
def is_same_type(lst):
    return all(isinstance(element, type(lst[0])) for element in lst)
print(is_same_type([1,2,"c"]))

# 4. Write a function which check if provided variable is a valid python variable 
import keyword
def is_valid_variable(var_name):
    return var_name.isidentifier() and not keyword.iskeyword(var_name)
print(is_valid_variable("my_var"))  # True
print(is_valid_variable("1st_var"))  # False