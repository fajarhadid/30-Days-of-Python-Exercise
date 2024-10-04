person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    print(person["skills"][2])
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if "skills" in person and "Python" in person["skills"]:
    print("You have a python skill")
# Decide a title based on skills.
if "Javascript" in person["skills"] and "React" in person["skills"]:
    print('He is a front end developer')
elif "Node" in person["skills"] and "Python" in person["skills"] and "MongoDB" in person["skills"]:
    print('He is a backend developer')
elif "React" in person["skills"] and "Node" in person["skills"] and "MongoDB" in person["skills"]:
    print('He is a fullstack developer')
else:
    print('Unknown Title')

# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_marred'] == True and person['country'] == "Finland":
    print(person['first_name'], person['last_name'], "lives in", person['country'], "He is married")