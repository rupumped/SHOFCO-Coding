from datetime import datetime, timedelta

# Get today's date
today = datetime.now()
print(f"Today's date: {today.strftime('%d %B %Y')}")

# Calculate due date (today + 14 days)
loan_period = 14  # days
due_date = today + timedelta(days=loan_period)

# Display the due date
print(f"If you borrow a book today, it will be due on: {due_date.strftime('%d %B %Y')}")

# Display day of the week for the due date
weekday = due_date.strftime("%A")
print(f"That will be a {weekday}")