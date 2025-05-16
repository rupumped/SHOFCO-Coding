from datetime import datetime

# Get current date
today = datetime.now()

# Get birth date information from user
birth_year = int(input("Enter your birth year (e.g., 2008): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day (1-31): "))

# Create date object for the birth date
birth_date = datetime(birth_year, birth_month, birth_day)

# Calculate age
age_in_days = (today - birth_date).days
age_in_years = age_in_days // 365  # Approximate

# Display results
print(f"You are approximately {age_in_years} years old")
print(f"That's about {age_in_days} days of life experience!")
print(f"You were born on a {birth_date.strftime('%A')}")