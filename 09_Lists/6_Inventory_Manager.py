def display_inventory(item_names, quantities, categories):
	"""Display the current inventory in a formatted table."""
	print("\nSHOFCO Inventory Status:")
	print("------------------------")
	print("ID  Item\t\tQuantity\tCategory")
	print("--  ----\t\t--------\t--------")
	
	for i in range(len(item_names)):
		# Format output with proper spacing
		item_space = "\t\t" if len(item_names[i]) < 10 else "\t"
		print(f"{i+1}.  {item_names[i]}{item_space}{quantities[i]}\t\t{categories[i]}")

def add_item(item_names, quantities, categories):
	"""Add a new item to the inventory."""
	name = input("Enter item name: ")
	
	# Validate quantity as a positive integer
	while True:
		try:
			quantity = int(input("Enter quantity: "))
			if quantity >= 0:
				break
			else:
				print("Quantity must be a positive number.")
		except ValueError:
			print("Please enter a valid number.")
	
	category = input("Enter category: ")
	
	# Add the new item to our lists
	item_names.append(name)
	quantities.append(quantity)
	categories.append(category)
	
	print(f"{name} has been added to inventory.")

def update_quantity(item_names, quantities, categories):
	"""Update the quantity of an existing item."""
	display_inventory(item_names, quantities, categories)
	
	# Get item ID and validate
	while True:
		try:
			item_id = int(input("\nEnter item ID to update: "))
			if 1 <= item_id <= len(item_names):
				break
			else:
				print(f"Please enter a valid ID between 1 and {len(item_names)}")
		except ValueError:
			print("Please enter a valid number.")
	
	# Convert to list index
	item_index = item_id - 1
	
	print(f"Current quantity of {item_names[item_index]}: {quantities[item_index]}")
	action = input("Add or remove items? (add/remove): ").lower()
	
	# Validate and update quantity
	while True:
		try:
			amount = int(input("Enter quantity: "))
			if amount >= 0:
				break
			else:
				print("Quantity must be a positive number.")
		except ValueError:
			print("Please enter a valid number.")
	
	if action == "add":
		quantities[item_index] += amount
		print(f"Added {amount} {item_names[item_index]}.")
	elif action == "remove":
		if amount <= quantities[item_index]:
			quantities[item_index] -= amount
			print(f"Removed {amount} {item_names[item_index]}.")
		else:
			print(f"Error: Not enough {item_names[item_index]} in inventory.")
			print(f"Current quantity: {quantities[item_index]}")
	else:
		print("Invalid action. No changes made.")

def search_items(item_names, quantities, categories):
	"""Search for items by name or category."""
	search_term = input("Enter search term: ").lower()
	
	print(f"\nSearch results for '{search_term}':")
	print("-----------------------------")
	
	found = False
	for i in range(len(item_names)):
		# Search in both name and category
		if (search_term in item_names[i].lower() or 
			search_term in categories[i].lower()):
			found = True
			print(f"{item_names[i]} - Quantity: {quantities[i]} - Category: {categories[i]}")
	
	if not found:
		print("No items found matching your search.")

def low_stock_alert(item_names, quantities, threshold=20):
	"""Identify and display items with low stock."""
	print("\nLow Stock Alert:")
	print("---------------")
	
	low_count = 0
	for i in range(len(item_names)):
		if quantities[i] < threshold:
			print(f"⚠️ {item_names[i]} - Only {quantities[i]} remaining")
			low_count += 1
	
	if low_count == 0:
		print("All items are well-stocked.")

def inventory_menu(item_names, quantities, categories):
	"""Display and handle the inventory system menu."""
	while True:
		print("\nOptions:")
		print("1. Display current inventory")
		print("2. Add new item")
		print("3. Update item quantity")
		print("4. Search inventory")
		print("5. Low stock alert")
		print("6. Exit")
		
		choice = input("\nSelect an option (1-6): ")
		
		if choice == "1":
			display_inventory(item_names, quantities, categories)
		elif choice == "2":
			add_item(item_names, quantities, categories)
		elif choice == "3":
			update_quantity(item_names, quantities, categories)
		elif choice == "4":
			search_items(item_names, quantities, categories)
		elif choice == "5":
			low_stock_alert(item_names, quantities)
		elif choice == "6":
			print("Thank you for using the SHOFCO Inventory System!")
			break
		else:
			print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
	# Initialize inventory lists
	item_names = ["Notebooks", "Pens", "Water Filters", "Textbooks", "First Aid Kits"]
	quantities = [50, 120, 15, 75, 10]
	categories = ["School", "School", "Health", "School", "Health"]
	
	print("SHOFCO Community Center Inventory System")
	print("=======================================")
	
	# Start the inventory management system
	inventory_menu(item_names, quantities, categories)