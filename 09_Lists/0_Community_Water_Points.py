def display_water_status(water_points, water_status):
	"""Display the status of all water points."""
	print("Water Point Status Report:")
	for i in range(len(water_points)):
		print(f"{water_points[i]}: {water_status[i]}")

def count_working_points(water_status):
	"""Count water points that are fully working."""
	working_count = 0
	for status in water_status:
		if status == "Working":
			working_count += 1
	return working_count

def list_working_points(water_points, water_status):
	"""List all working water points."""
	print("\nWorking water points:")
	for i in range(len(water_points)):
		if water_status[i] == "Working":
			print(f"- {water_points[i]}")

if __name__ == "__main__":
	# Lists of water points and their status
	water_points = ["Olympic", "Eldoret", "Kisumu", "Lodwar", "Garissa"]
	water_status = ["Working", "Under repair", "Working", "Working", "Low pressure"]
	
	# Display status report
	display_water_status(water_points, water_status)
	
	# Count and display working points
	working_count = count_working_points(water_status)
	print(f"\n{working_count} out of {len(water_points)} water points are fully working")
	
	# List all working points
	list_working_points(water_points, water_status)