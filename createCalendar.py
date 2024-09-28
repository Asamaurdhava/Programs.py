print("This program prints the day of the input date.")

import calendar

def find_day(month, day, year):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Remove the year restriction to allow for a wider range of dates
    dayInt = calendar.weekday(int(year), int(month), int(day))
    return days[dayInt]

date = input("\nEnter a date separated by a whitespace (MM DD YYYY): ")

month, day, year = date.split(" ")

theDay = find_day(month, day, year)

# Convert year to integer for proper comparison
year_int = int(year)
current_year = 2024  # Update this to the current year

if year_int < current_year:
    print(f"\nIt was {theDay.upper()} on {date}.")
elif year_int == current_year:
    print(f"\nIt's {theDay.upper()} on {date}.")
else:
    print(f"\nIt'll be {theDay.upper()} on {date}.")
