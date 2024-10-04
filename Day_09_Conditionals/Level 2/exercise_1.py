score = int(input("Enter the score: "))
grade = ""

if score >= 80 and score <=100:
    grade = "A"
elif score >= 70 and score <= 89:
    grade = "B"
elif score >= 60 and score <= 69:
    grade = "C"
elif score >= 50 and score <= 59:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")