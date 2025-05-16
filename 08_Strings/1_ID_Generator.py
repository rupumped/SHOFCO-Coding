def generate_student_id(name, grade, year):
	"""
	Generates a SHOFCO student ID.
	
	Args:
		name (str): Student's full name
		grade (str): Student's grade/class
		year (str): Current year
		
	Returns:
		str: Student ID in format: INITIALS-GRADE-YEAR (e.g., JM-8-2025)
	"""
	# Your code here:
	# 1. Extract initials from name
	# 2. Convert all components to uppercase
	# 3. Combine using the required format
	
	# Get name parts and extract initials
	name_parts = name.split()
	initials = ""
	for part in name_parts:
		if part:  # Check if part is not empty
			initials += part[0]
	
	# Format the components
	formatted_initials = initials.upper()
	formatted_grade = grade.strip()
	formatted_year = year.strip()
	
	# Create ID
	student_id = f"{formatted_initials}-{formatted_grade}-{formatted_year}"
	
	return student_id

if __name__ == "__main__":
	# Test the function
	student_name = input("Enter your full name: ")
	student_grade = input("Enter your grade/class: ")
	current_year = input("Enter current year: ")
	
	student_id = generate_student_id(student_name, student_grade, current_year)
	print(f"Your SHOFCO student ID: {student_id}")