# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
sorted_ages = sorted(ages)
min_age = min(sorted_ages) # 19
max_age = max(sorted_ages) # 26

# Find the median age (one middle item or two middle items divided by two)
n = len(ages)
if n % 2 == 1:
    median = ages[n // 2]
else:
    median = (ages[n // 2 - 1] + ages[n // 2]) // 2

print(f"The median age is {median}")

# Find the average age (sum of all items divided by their number)
avg = sum(ages) / 10
print(avg) # 22.8

# Find the range of the ages (max minus min)
ages_range = max_age - min_age
print(ages_range) # 7

# Compare the value of (min - average) and (max - average), use abs() method
minavg = min(ages) - avg
print(abs(minavg))
maxavg = max(ages) - avg
print(abs(maxavg))