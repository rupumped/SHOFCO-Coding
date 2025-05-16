def analyze_temperatures(days, temperatures):
	"""Analyze the collected temperature data."""
	# Calculate statistics
	average = sum(temperatures) / len(temperatures)
	highest = max(temperatures)
	lowest = min(temperatures)
	
	# Find the hottest and coldest days
	hottest_index = temperatures.index(highest)
	coldest_index = temperatures.index(lowest)
	
	# Display results
	print("\nWeekly Temperature Report:")
	print(f"Average temperature: {average:.1f}°C")
	print(f"Highest temperature: {highest}°C on {days[hottest_index]}")
	print(f"Lowest temperature: {lowest}°C on {days[coldest_index]}")
	
	# Display days above average
	print("\nDays with above average temperature:")
	for i in range(len(temperatures)):
		if temperatures[i] > average:
			print(f"- {days[i]}: {temperatures[i]}°C")

def main():
	days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	temperatures = [14, 15, 19, 26, 25, 23, 25]

	# Analyze data
	analyze_temperatures(days, temperatures)

if __name__ == "__main__":
	main()