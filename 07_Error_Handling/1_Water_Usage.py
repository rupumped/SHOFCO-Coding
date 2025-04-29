def calculate_weekly_usage(daily_usage):
	"""Calculate weekly water usage in liters.
	
	Args:
		daily_usage: Daily water usage in liters
		
	Returns:
		Weekly water usage in liters
		
	Raises:
		ValueError: If daily usage is negative
	"""
	if daily_usage < 0:
		raise ValueError("Water usage cannot be negative")
	
	return daily_usage * 7

def get_conservation_tip(usage_level):
	"""Return a water conservation tip based on usage level.
	
	Args:
		usage_level: String indicating usage level ('low', 'medium', or 'high')
		
	Returns:
		A conservation tip
		
	Raises:
		ValueError: If usage level is not valid
	"""
	if usage_level == "low":
		return "Great job conserving water! Keep it up!"
	elif usage_level == "medium":
		return "Tip: Turn off taps while brushing teeth to save water."
	elif usage_level == "high":
		return "Tip: Consider reusing washing water for cleaning floors."
	else:
		raise ValueError("Invalid usage level. Use 'low', 'medium', or 'high'.")

def determine_usage_level(weekly_usage, household_size):
	"""Determine the water usage level.
	
	Args:
		weekly_usage: Weekly water usage in liters
		household_size: Number of people in household
		
	Returns:
		String indicating usage level ('low', 'medium', or 'high')
	"""
	avg_per_person = weekly_usage / household_size
	
	if avg_per_person < 140:  # 20 liters per day
		return "low"
	elif avg_per_person < 350:  # 50 liters per day
		return "medium"
	else:
		return "high"

def run_water_calculator():
	"""Run the water usage calculator program."""
	try:
		print("Let's calculate your household water usage!")
		
		household_size = int(input("How many people live in your household? "))
		if household_size <= 0:
			raise ValueError("Household size must be at least 1")
		
		daily_usage = float(input("How many liters of water does your household use daily? "))
		weekly_usage = calculate_weekly_usage(daily_usage)
		
		print(f"\nYour weekly household water usage is {weekly_usage} liters.")
		print(f"That's about {weekly_usage/household_size:.1f} liters per person per week.")
		
		usage_level = determine_usage_level(weekly_usage, household_size)
		tip = get_conservation_tip(usage_level)
		print(tip)
		
	except ValueError as e:
		if "could not convert" in str(e):
			print("Error: Please enter valid numbers.")
		else:
			print(f"Error: {e}")
	
	except ZeroDivisionError:
		print("Error: Household size cannot be zero.")
	
	except Exception as e:
		print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
	print("Welcome to SHOFCO Water Usage Calculator!")
	run_water_calculator()