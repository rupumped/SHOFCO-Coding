minutes = int(input("Minutes: "))  # time in minutes
hours = minutes // 60  # whole hours
remaining_minutes = minutes % 60  # remaining minutes

# Display conversions
print("===== Unit Conversion =====")
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")
print("===========================")

# Try creating your own unit conversions!