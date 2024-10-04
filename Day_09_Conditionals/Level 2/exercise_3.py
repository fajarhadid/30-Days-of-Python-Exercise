fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter your fruit: ")

if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")