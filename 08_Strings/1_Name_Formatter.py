def format_name(first_name, last_name):
	"""
	Formats a name by capitalizing the first letter of each part.
	
	Args:
		first_name (str): The first name to format
		last_name (str): The last name to format
		
	Returns:
		str: The properly formatted full name
	"""
	# Your code here:
	# 1. Capitalize each name part
	# 2. Combine into full name
	
	formatted_first = first_name.capitalize()
	formatted_last = last_name.capitalize()
	full_name = formatted_first + " " + formatted_last
	
	return full_name

if __name__ == "__main__":
	# Test the function
	first = input("Enter your first name: ").strip()
	last = input("Enter your last name: ").strip()
	
	formatted = format_name(first, last)
	print(f"Formatted name: {formatted}")