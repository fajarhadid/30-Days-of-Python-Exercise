month = input("Enter the month: ")
season = ""

if month in ('September', 'October', 'November'):
    season = "Autumn"
elif month in ('December', 'January', 'February'):
    season = "Winter"
elif month in ('March', 'April', 'May'):
    season = "Spring"
else:
    season = "Summer"
    
print(f"This is the {season} season")