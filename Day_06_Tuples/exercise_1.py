# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Fatima', 'Lily', 'Zoe', 'Rose')
brothers = ('Jake', 'Luke', 'Isaac', 'Alex')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings) # ('Fatima', 'Lily', 'Zoe', 'Rose', 'Jake', 'Luke', 'Isaac', 'Alex')

# 4. How many siblings do you have?
print(len(siblings)) # 8

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
father = "Michael"
mother = "Sarah"
siblings.append(father)
siblings.append(mother)
family_members = tuple(siblings)
print(family_members) # ('Fatima', 'Lily', 'Zoe', 'Rose', 'Jake', 'Luke', 'Isaac', 'Alex', 'Michael', 'Sarah')