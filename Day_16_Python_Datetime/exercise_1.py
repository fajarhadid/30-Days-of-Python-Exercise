from datetime import datetime

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('Timestamp:', timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted date:", formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time
date_string = "5 December, 2019"
print(date_string) # 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# 4. Calculate the time difference between now and new year
from datetime import date
today = date(year=2024, month=9, day=30)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today # 93 days left for new year (from 30 September 2024)
print("Time left for new year:",time_left_for_newyear)

# 5. Calculate the time difference between 1 January 1970 and now
start_date = datetime(1970, 1, 1)
current_date = now

time_difference = current_date - start_date
print(f"Time difference: {time_difference}")
print(f"Total days: {time_difference.days}")
print(f"Total seconds: {time_difference.seconds}")

# 6. 