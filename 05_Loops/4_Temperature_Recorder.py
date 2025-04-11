# Starting values
total_temperature = 0
days = 7

# Get temperature for each day
for day in range(1, days + 1):
    temperature = int(input(f"Enter temperature for day {day} (in °C): "))
    total_temperature = total_temperature + temperature
    print(f"Recorded {temperature}°C for day {day}")
    
# Calculate and display average
average_temperature = total_temperature / days
print(f"Average temperature over {days} days: {average_temperature}°C")