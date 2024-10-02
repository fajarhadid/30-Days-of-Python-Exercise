# 1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C) # {19, 20, 22, 24, 25, 26, 27, 28}

# 2. Find A intersection B
print(A.intersection(B)) # {19, 20, 22, 24, 25, 26}

# 3. Is A subset of B
print(A.issubset(B)) # True

# 4. Are A and B disjoint sets
print(B.isdisjoint(A)) # False

# 5. Join A with B and B with A
a_with_b = A.union(B)
b_with_a = B.union(A)
print(a_with_b)
print(b_with_a)

# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B)) # {27, 28}

# 7. Delete the sets completely
del A
del B
del C