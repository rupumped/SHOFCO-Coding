# First, we need to import the datetime module
from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()
print("Current date and time:", current_datetime)

# Extract parts of the datetime
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)