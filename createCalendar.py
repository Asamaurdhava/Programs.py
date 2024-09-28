print("This program prints the day of the input date.")

import calendar

def find_day(month, day, year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if int(year) > 2000 and int(year) < 3000:
        dayInt = calendar.weekday(int(year), int(month), int(day))
        return days[dayInt]
        

date = input("\nEnter a date separated by a whitespace (MM DD YYYY): ")

month, day, year = date.split(" ")

theDay = find_day(month, day, year)

if year < "2024":
    print(f"\nIt was {theDay.upper()} on {date}.")
elif year == "2024":
    print(f"\nIt's {theDay.upper()} on {date}.")
else:
    print(f"\nIt'll be {theDay.upper()} on {date}.")
