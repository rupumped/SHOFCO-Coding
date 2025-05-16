from datetime import datetime

# Define some important dates (year, month, day)
# Note: You can change these dates to match actual SHOFCO events
computer_competition = datetime(2025, 8, 15)
end_of_term = datetime(2025, 7, 30)
career_day = datetime(2025, 9, 5)

# Get current date (ignore time part)
today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# Calculate days until each event
days_to_competition = (computer_competition - today).days
days_to_end_of_term = (end_of_term - today).days
days_to_career_day = (career_day - today).days

# Display results
print(f"Days until Computer Programming Competition: {days_to_competition}")
print(f"Days until End of Term: {days_to_end_of_term}")
print(f"Days until Career Day: {days_to_career_day}")