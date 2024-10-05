# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
odd_res = 0
even_res =0
for i in range(101):
    if i % 2 == 0:
        even_res += i
    else:
        odd_res += i
print(f"The sum of all evens is {even_res}")
print(f"The sum of all evens is {odd_res}")