# Water tank information
tank_capacity = int(input("Tank Capacity (L): "))  # liters
daily_usage = int(input("Daily Usage (L): "))     # liters per day

# Calculate how many complete days the tank will last
days_complete = tank_capacity // daily_usage

# Calculate remaining water after those complete days
remaining_water = tank_capacity % daily_usage

# Calculate what percentage of an additional day the remaining water provides
percentage_additional_day = (remaining_water / daily_usage) * 100

# Calculate total days (including partial days)
total_days = tank_capacity / daily_usage

# Display results
print("===== Water Tank Calculator =====")
print(f"Tank Capacity: {tank_capacity} liters")
print(f"Daily Usage: {daily_usage} liters per day")
print(f"Complete Days: {days_complete} days")
print(f"Remaining Water: {remaining_water} liters")
print(f"Additional Day Percentage: {percentage_additional_day:.1f}%")
print(f"Total Days (including partial): {total_days:.2f} days")
print("=================================")

# Try changing the tank capacity and daily usage to see how the results change!