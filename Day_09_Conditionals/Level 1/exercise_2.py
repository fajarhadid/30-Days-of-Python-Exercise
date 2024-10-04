my_age = 24
your_age = int(input("Enter your age: "))

if my_age < your_age:
    print(f"You are {your_age - my_age} years older than me ")
elif my_age > your_age:
    print(f"You are {my_age - your_age} years younger than me ")
else:
    print("We are cool bro")