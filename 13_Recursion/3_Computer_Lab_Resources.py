def optimize_lab_resources(resources, budget, current_index=0, current_selections=None, best_solution=None):
	"""
	Recursively find the optimal computer lab resources to purchase within a budget
	
	Args:
		resources: List of (name, cost, value) tuples
		budget: Maximum amount to spend
		current_index: Current resource being considered
		current_selections: Resources selected so far
		best_solution: Best solution found so far
	
	Returns:
		Tuple of (max_value, selected_resources)
	"""
	# Initialize tracking variables
	if current_selections is None:
		current_selections = []
	if best_solution is None:
		best_solution = (0, [])  # (total_value, selections)
	
	# Base case: we've considered all resources
	if current_index >= len(resources):
		# Calculate total value and cost of current selections
		total_value = sum(resources[i][2] for i in current_selections)
		total_cost = sum(resources[i][1] for i in current_selections)
		
		# If this solution is better than our best so far, update best
		if total_value > best_solution[0] and total_cost <= budget:
			best_solution = (total_value, current_selections.copy())
			
		return best_solution
	
	# Try including the current resource
	current_selections.append(current_index)
	include = optimize_lab_resources(resources, budget, current_index + 1, current_selections, best_solution)
	
	# Update best solution if including was better
	if include[0] > best_solution[0]:
		best_solution = include
	
	# Try excluding the current resource
	current_selections.pop()
	exclude = optimize_lab_resources(resources, budget, current_index + 1, current_selections, best_solution)
	
	# Return the better of the two options
	if include[0] > exclude[0]:
		return include
	else:
		return exclude


if __name__ == "__main__":
	print("SHOFCO Computer Lab Resource Optimizer")
	print("This program helps decide the best way to spend the computer lab budget\n")
	
	# Define available resources: (name, cost in KSh, educational value 1-10)
	lab_resources = [
		("Basic Coding Textbooks (10)", 2500, 7),
		("Computer Mice (5)", 1500, 4),
		("Keyboards (5)", 2000, 4),
		("Programming Software License", 5000, 9),
		("Headphones (10)", 3000, 6),
		("Projector", 15000, 8),
		("Wi-Fi Router", 4000, 7),
		("USB Drives (20)", 3500, 5),
		("Computer Tables (2)", 6000, 6),
		("Chairs (5)", 3500, 4),
		("Electrical Extensions", 2000, 5),
		("Educational Games", 1500, 3),
		("Python Reference Guides", 2500, 8),
		("Printer", 8000, 7),
		("Whiteboard", 3000, 6)
	]
	
	# Get budget input
	try:
		available_budget = float(input("Enter available budget in KSh: "))
		
		print(f"\nFinding optimal resource allocation for {available_budget} KSh budget...\n")
		value, selected = optimize_lab_resources(lab_resources, available_budget)
		
		# Display results
		if selected:
			print("Recommended purchases:")
			total_cost = 0
			
			for idx in selected:
				name, cost, val = lab_resources[idx]
				total_cost += cost
				print(f"- {name}: {cost} KSh (Value: {val}/10)")
			
			print(f"\nTotal cost: {total_cost} KSh")
			print(f"Total educational value: {value}")
			print(f"Remaining budget: {available_budget - total_cost} KSh")
		else:
			print("Couldn't find a valid combination of resources within your budget.")
			
	except ValueError:
		print("Please enter a valid budget amount.")