# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Terror', 'breed':'Bulldog', 'legs':4, 'age':5}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 30,
    "marital_status": "Single",
    "skills": ["Python", "Data Analysis", "Data Engineering"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main St, Apt 4B"
}

# 4. Get the length of the student dictionary
print(len(student)) # 9

# 5. Get the value of skills and check the data type, it should be a list
print(type(student.get("skills")))

# 6. Modify the skills values by adding one or two skills
student["skills"].append("HTML")
print(student)

# 7. Get the dictionary keys as a list
keys = student.keys()
print(list(keys))

# 8. Get the dictionary values as a list
values = student.values()
print(list(values))

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())

# 10. Delete one of the items in the dictionary
del student['address']
print(student.items())

# 11. Delete one of the dictionaries
del dog