def check_password_strength(password):
	"""
	Checks the strength of a password.
	
	Args:
		password (str): The password to evaluate
		
	Returns:
		tuple: (strength_score, feedback_message)
	"""
	# Your code here:
	# 1. Check length of password
	# 2. Check for uppercase, lowercase, digits, special chars
	# 3. Calculate strength score and generate feedback
	
	score = 0
	feedback = []
	
	# Check length
	if len(password) < 6:
		feedback.append("Password is too short")
	elif len(password) >= 10:
		score += 2
		feedback.append("Good length")
	else:
		score += 1
	
	# Check for uppercase
	if any(char.isupper() for char in password):
		score += 1
		feedback.append("Contains uppercase letters")
	else:
		feedback.append("Add uppercase letters")
	
	# Check for lowercase
	if any(char.islower() for char in password):
		score += 1
		feedback.append("Contains lowercase letters")
	else:
		feedback.append("Add lowercase letters")
	
	# Check for digits
	if any(char.isdigit() for char in password):
		score += 1
		feedback.append("Contains numbers")
	else:
		feedback.append("Add numbers")
	
	# Check for special characters
	special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?"
	if any(char in special_chars for char in password):
		score += 1
		feedback.append("Contains special characters")
	else:
		feedback.append("Add special characters")
	
	# Generate strength message
	if score < 3:
		strength = "Weak"
	elif score < 5:
		strength = "Moderate"
	else:
		strength = "Strong"
	
	feedback_message = f"Password strength: {strength}\nFeedback: {', '.join(feedback)}"
	
	return (score, feedback_message)

if __name__ == "__main__":
	# Test the function
	password = input("Enter a password to check: ")
	
	score, feedback = check_password_strength(password)
	print(feedback)