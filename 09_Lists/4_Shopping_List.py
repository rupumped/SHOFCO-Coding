def add_items(budget):
	"""Add items to the shopping list within budget."""
	items = []
	prices = []
	remaining = budget
	
	while True:
		# Show remaining budget
		print(f"\nRemaining budget: {remaining} KSh")
		
		# Get item details
		item = input("Enter item name (or 'done' to finish): ")
		if item.lower() == 'done':
			break
		
		while True:
			try:
				price = float(input(f"Enter price of {item} in KSh: "))
				if price > 0:
					break
				else:
					print("Price must be greater than zero.")
			except ValueError:
				print("Please enter a valid number.")
		
		# Check if within budget
		if price <= remaining:
			items.append(item)
			prices.append(price)
			remaining -= price
			print(f"{item} added to shopping list")
		else:
			print(f"Cannot afford {item}. Exceeds remaining budget.")
	
	return items, prices, remaining

def display_shopping_list(items, prices):
	"""Display the complete shopping list."""
	if not items:
		print("\nYour shopping list is empty.")
		return
	
	print("\nYour Shopping List:")
	total = 0
	for i in range(len(items)):
		print(f"{i+1}. {items[i]}: {prices[i]} KSh")
		total += prices[i]
	
	print(f"\nTotal items: {len(items)}")
	print(f"Total cost: {total} KSh")

def display_sorted_items(items, prices):
	"""Display items sorted by price."""
	if not items:
		return
	
	print("\nItems sorted by price (lowest to highest):")
	
	# Create a list of indexes
	indexes = list(range(len(items)))
	
	# Sort indexes based on prices
	for i in range(len(indexes)):
		for j in range(i+1, len(indexes)):
			if prices[indexes[i]] > prices[indexes[j]]:
				# Swap indexes
				indexes[i], indexes[j] = indexes[j], indexes[i]
	
	# Display sorted items
	for i in indexes:
		print(f"{items[i]}: {prices[i]} KSh")

if __name__ == "__main__":
	# Get budget
	while True:
		try:
			budget = float(input("Enter your shopping budget in KSh: "))
			if budget > 0:
				break
			else:
				print("Budget must be greater than zero.")
		except ValueError:
			print("Please enter a valid number.")
	
	print("\nSHOFCO Market Shopping Assistant")
	print(f"Your budget: {budget} KSh")
	
	# Add items to shopping list
	items, prices, remaining = add_items(budget)
	
	# Display shopping list
	display_shopping_list(items, prices)
	print(f"Remaining budget: {remaining} KSh")
	
	# Display items sorted by price
	display_sorted_items(items, prices)