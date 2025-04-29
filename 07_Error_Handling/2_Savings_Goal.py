def calculate_months_to_goal(goal_amount, monthly_saving):
	"""Calculate how many months it will take to reach a savings goal.
	
	Args:
		goal_amount: The target amount to save
		monthly_saving: Amount saved each month
		
	Returns:
		Number of months to reach goal
		
	Raises:
		ValueError: If inputs are negative or zero
	"""
	if goal_amount <= 0:
		raise ValueError("Goal amount must be positive")
	if monthly_saving <= 0:
		raise ValueError("Monthly saving must be positive")
	
	months = goal_amount / monthly_saving
	return months

def format_time_duration(months):
	"""Format number of months as years and months.
	
	Args:
		months: Number of months
		
	Returns:
		Formatted string of years and months
	"""
	years = int(months // 12)
	remaining_months = int(months % 12)
	
	if years == 0:
		return f"{remaining_months} months"
	elif years == 1 and remaining_months == 0:
		return "1 year"
	elif years > 1 and remaining_months == 0:
		return f"{years} years"
	elif years == 1:
		return f"1 year and {remaining_months} months"
	else:
		return f"{years} years and {remaining_months} months"

def suggest_savings_strategy(goal_amount, time_limit_months):
	"""Suggest monthly saving amount to reach goal within time limit.
	
	Args:
		goal_amount: The target amount to save
		time_limit_months: Maximum months to reach goal
		
	Returns:
		Required monthly saving amount
		
	Raises:
		ValueError: If inputs are negative or zero
	"""
	if goal_amount <= 0:
		raise ValueError("Goal amount must be positive")
	if time_limit_months <= 0:
		raise ValueError("Time limit must be positive")
	
	monthly_saving = goal_amount / time_limit_months
	return monthly_saving

def run_savings_calculator():
	"""Run the savings goal calculator program."""
	try:
		print("Let's calculate your savings plan!")
		
		goal_name = input("What are you saving for? ")
		goal_amount = float(input(f"How much money do you need for your {goal_name}? (KSh) "))
		
		# Ask user which calculation they want to do
		print("\nWhat would you like to calculate?")
		print("1. How long will it take to reach my goal?")
		print("2. How much should I save each month to reach my goal by a specific date?")
		
		choice = input("Enter your choice (1 or 2): ")
		
		if choice == "1":
			monthly_saving = float(input("How much can you save each month? (KSh) "))
			months = calculate_months_to_goal(goal_amount, monthly_saving)
			time_str = format_time_duration(months)
			
			print(f"\nTo save KSh {goal_amount:.2f} for your {goal_name}:")
			print(f"- Saving KSh {monthly_saving:.2f} each month")
			print(f"- You will reach your goal in {time_str}")
			
		elif choice == "2":
			time_limit = input("When do you want to reach your goal? (e.g., '2 years' or '18 months') ")
			
			# Parse the time input
			months = 0
			if "year" in time_limit and "month" in time_limit:
				# Pattern like "2 years and 6 months"
				parts = time_limit.split(" and ")
				years = int(parts[0].split()[0])
				months = int(parts[1].split()[0])
				months += years * 12
			elif "year" in time_limit:
				# Pattern like "2 years"
				years = int(time_limit.split()[0])
				months = years * 12
			elif "month" in time_limit:
				# Pattern like "18 months"
				months = int(time_limit.split()[0])
			else:
				raise ValueError("Please enter time in years or months format")
			
			monthly_saving = suggest_savings_strategy(goal_amount, months)
			
			print(f"\nTo save KSh {goal_amount:.2f} for your {goal_name} in {time_limit}:")
			print(f"- You need to save KSh {monthly_saving:.2f} each month")
			
		else:
			print("Invalid choice. Please run the program again and select 1 or 2.")
		
	except ValueError as e:
		if "could not convert" in str(e):
			print("Error: Please enter valid numbers for amounts and time periods.")
		else:
			print(f"Error: {e}")
	
	except Exception as e:
		print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
	print("Welcome to SHOFCO Financial Goals Calculator!")
	run_savings_calculator()