# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum
def sum_two_numbers(num1, num2):
    return num1 + num2
print(sum_two_numbers(10, 29))

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle
def area_of_circle(r):
    PI = 3.14
    area = PI * r * r
    print(area)
area_of_circle(7)

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback
def add_all_nums(*args):
    total = 0
    for i in args:
        if isinstance(i, int):
            total += i
        else:
            print("Please input a number")
    print(total)
add_all_nums(14, 20, 39)

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
def convert_celcius_to_fahrenheit(degree):
    f = (degree * 9 / 5) + 32
    print(f)
convert_celcius_to_fahrenheit(30)

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer
def check_season(month):
    if month in ('December', 'January', 'February'):
        print("It's Winter!")
    elif month in ('March', 'April', 'May'):
        print("It's Spring!")
    elif month in ('June', 'July', 'August'):
        print("It's Summer!")
    else:
        print("It's Autumn!")
check_season("August")

# 6. Write a function called calculate_slope which return the slope of a linear equatio
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    print(slope)
calculate_slope(2, 5, 9, 19)

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn
import cmath
def solve_quadratic_eqn(a, b ,c):
    if a == 0:
        raise ValueError("'a' must not be zero for a quadratic equation")
    D = b**2 - 4*a*c

    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)

    return x1, x2
solutions = solve_quadratic_eqn(1, -3, 2)
print(f"The solutions are: {solutions[0]} and {solutions[1]}")

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list
def print_list(list):
    print(list)
print_list(['Apple', 'Banana', 'Orange'])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(lst):
    return [i for i in reversed(lst)]
print(reverse_list(["A", "B", "C"]))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    return [i.capitalize() for i in lst]
print(capitalize_list_items(["oke", "banget", "bjir"]))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end
def add_item(lst, item):
    lst.append(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item(food_staff, 'Mango'))

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range
def sum_of_numbers(num):
    total = 0
    for i in range(num+1):
        total += i
    print(total)
sum_of_numbers(100)

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range
def sum_of_odds(num):
    total = 0
    for i in range(num+1):
        if i % 2 != 0:
            total += i
    print(total)
sum_of_odds(100)

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range
def sum_of_evens(num):
    total = 0
    for i in range(num+1):
        if i % 2 == 0:
            total += i
    print(total)
sum_of_evens(100)