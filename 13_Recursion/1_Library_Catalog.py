def explore_library_catalog(catalog, category_path=None, indent=0):
	"""
	Recursively explore the SHOFCO library catalog hierarchy
	
	Args:
		catalog: Dictionary representing the library catalog
		category_path: Current path in the catalog being explored
		indent: Current indentation level for display
	"""
	# Initialize category path if none
	if category_path is None:
		category_path = ["Main Catalog"]
		current_category = catalog
	else:
		# Navigate to the current category
		current_category = catalog
		for category in category_path[1:]:  # Skip "Main Catalog"
			current_category = current_category[category]
	
	# Print current location in the catalog
	print("\n" + "=" * 40)
	print("Current location: " + " > ".join(category_path))
	print("=" * 40)
	
	# Display all items in this category
	items = []
	subcategories = []
	
	for key, value in current_category.items():
		if isinstance(value, dict):
			# This is a subcategory
			book_count = count_books(value)
			print(f"📚 {key} ({book_count} books)")
			subcategories.append(key)
		else:
			# This is a book entry
			items.append(key)
			print(f"📖 {key} - {value}")
	
	# Provide navigation options
	print("\nWhat would you like to do?")
	if len(category_path) > 1:
		print("0. Go back to parent category")
	
	if subcategories:
		print("Enter a subcategory number:")
		for i, subcat in enumerate(subcategories, 1):
			print(f"{i}. Browse {subcat}")
	
	if not subcategories and not items:
		print("This category is empty!")
		
	# Get user choice
	choice = input("\nYour choice (or q to quit): ")
	
	if choice.lower() == 'q':
		print("\nThank you for exploring the SHOFCO Library Catalog!")
		return
	
	try:
		choice_num = int(choice)
		
		if choice_num == 0 and len(category_path) > 1:
			# Go back to parent category
			explore_library_catalog(catalog, category_path[:-1], indent)
		elif 1 <= choice_num <= len(subcategories):
			# Explore subcategory
			selected = subcategories[choice_num - 1]
			new_path = category_path + [selected]
			explore_library_catalog(catalog, new_path, indent + 2)
		else:
			print("\nInvalid choice! Please try again.")
			explore_library_catalog(catalog, category_path, indent)
			
	except ValueError:
		print("\nPlease enter a number or 'q'.")
		explore_library_catalog(catalog, category_path, indent)


def count_books(catalog):
	"""
	Recursively count all books in a catalog or subcatalog
	
	Args:
		catalog: Dictionary of the catalog to count
		
	Returns:
		Total number of books in this catalog and all subcatalogs
	"""
	total = 0
	
	for key, value in catalog.items():
		if isinstance(value, dict):
			# This is a subcategory, recursively count its books
			total += count_books(value)
		else:
			# This is a book
			total += 1
			
	return total


if __name__ == "__main__":
	print("SHOFCO Library Catalog Explorer")
	print("Navigate through our library's categories and find books!\n")
	
	# Create a sample hierarchical library catalog
	library_catalog = {
		"Fiction": {
			"African Literature": {
				"Things Fall Apart": "Chinua Achebe (1958)",
				"Weep Not, Child": "Ngũgĩ wa Thiong'o (1964)",
				"Americanah": "Chimamanda Ngozi Adichie (2013)"
			},
			"World Literature": {
				"To Kill a Mockingbird": "Harper Lee (1960)",
				"The Kite Runner": "Khaled Hosseini (2003)"
			}
		},
		"Non-Fiction": {
			"Science": {
				"Brief History of Time": "Stephen Hawking (1988)",
				"Silent Spring": "Rachel Carson (1962)"
			},
			"Technology": {
				"Computer Basics": "SHOFCO IT Department (2022)",
				"Python for Beginners": "SHOFCO Computer Lab (2023)"
			},
			"History": {
				"African History": {
					"Long Walk to Freedom": "Nelson Mandela (1994)",
					"Kenya: Between Hope and Despair": "Daniel Branch (2011)"
				},
				"World History": {
					"Sapiens": "Yuval Noah Harari (2011)"
				}
			}
		},
		"Educational": {
			"Mathematics": {
				"Basic Algebra": "SHOFCO Education (2021)",
				"Geometry Fundamentals": "SHOFCO Education (2022)"
			},
			"Languages": {
				"English Grammar": "SHOFCO English Department (2021)",
				"Kiswahili Msingi": "SHOFCO Languages (2020)"
			}
		}
	}
	
	# Start exploring the catalog
	explore_library_catalog(library_catalog)