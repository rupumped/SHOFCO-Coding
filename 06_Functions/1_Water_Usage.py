def calculate_water_usage(buckets_per_day, family_size):
	"""
	Calculate weekly water usage for a family.
	
	Parameters:
	- buckets_per_day: Number of buckets used daily
	- family_size: Number of people in the family
	
	Returns:
	- Total liters used in a week
	"""
	# Each bucket is about 20 liters
	liters_per_bucket = 20
	
	# Calculate daily usage
	daily_usage = buckets_per_day * liters_per_bucket
	
	# Calculate weekly usage
	weekly_usage = daily_usage * 7
	
	# Calculate usage per person
	usage_per_person = weekly_usage / family_size
	
	return weekly_usage, usage_per_person

# Example usage
if __name__ == "__main__":
	total_weekly, per_person = calculate_water_usage(3, 5)
	print(f"Your family uses {total_weekly} liters of water per week.")
	print(f"That's about {per_person:.1f} liters per person per week.")
	
	# Try different values!