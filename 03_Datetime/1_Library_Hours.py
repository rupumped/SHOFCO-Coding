from datetime import datetime

# Library opening hours
opening_time = 9  # 9:00 AM
closing_time = 17  # 5:00 PM

# Get current date and time
now = datetime.now()

# Format and display today's date
today_date = now.strftime("%d %B %Y")  # Example: "16 May 2025"
print(f"Today's date: {today_date}")

# Display library hours
print(f"SHOFCO Library Hours for today:")
print(f"Opening time: {opening_time}:00")
print(f"Closing time: {closing_time}:00")

# Calculate how many hours the library is open
hours_open = closing_time - opening_time
print(f"The library is open for {hours_open} hours today")