# Step 1: Define the function
def welcome_student(student_name):
	message = f"Karibu, {student_name}! Welcome to SHOFCO Computer Lab."
	return message

# Step 2: Use if __name__ == "__main__": to call the function
if __name__ == "__main__":
	# Call the function with different names
	greeting1 = welcome_student("Wanjiku")
	greeting2 = welcome_student("Otieno")
	
	# Print the results
	print(greeting1)
	print(greeting2)
	
	# Try calling the function again with your own name!