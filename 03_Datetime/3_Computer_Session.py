from datetime import datetime, timedelta

# Get current time
now = datetime.now()
print(f"Current time: {now.strftime('%H:%M:%S')}")

# Session length in minutes
session_length = 60

# Simulate session start time (20 minutes ago)
elapsed_time = int(input('How many minutes ago did your session start? '))
session_start = now - timedelta(minutes=elapsed_time)
print(f"Session started at: {session_start.strftime('%H:%M:%S')}")

# Calculate session end time
session_end = session_start + timedelta(minutes=session_length)
print(f"Session ends at: {session_end.strftime('%H:%M:%S')}")

# Calculate remaining time
remaining_minutes = (session_end - now).seconds // 60
print(f"You have {remaining_minutes} minutes remaining in your session")