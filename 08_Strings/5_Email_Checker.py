def is_valid_email(email):
	"""
	Validates if a string is a properly formatted email address.
	
	Args:
		email (str): The email address to validate
		
	Returns:
		tuple: (is_valid, reason)
	"""
	# Your code here:
	# 1. Check for @ symbol
	# 2. Check for domain with period
	# 3. Check for other validity requirements
	
	# Initial validation checks
	if not email or email.isspace():
		return (False, "Email cannot be empty")
	
	# Check for @ symbol
	if '@' not in email:
		return (False, "Email must contain an @ symbol")
	
	# Split into local and domain parts
	try:
		local, domain = email.split('@', 1)
	except ValueError:
		return (False, "Email must have exactly one @ symbol")
	
	# Check local part
	if not local:
		return (False, "Username part before @ cannot be empty")
	
	# Check domain part
	if not domain:
		return (False, "Domain part after @ cannot be empty")
	
	if '.' not in domain:
		return (False, "Domain must include a period (e.g., .com, .org)")
	
	# Check domain extension
	domain_parts = domain.split('.')
	if len(domain_parts) < 2:
		return (False, "Domain must have at least one period")
	
	extension = domain_parts[-1]
	if not extension:
		return (False, "Domain extension cannot be empty")
	
	if len(extension) < 2:
		return (False, "Domain extension must be at least 2 characters")
	
	# Basic character validation
	allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_@")
	if not all(c in allowed_chars for c in email):
		return (False, "Email contains invalid characters")
	
	return (True, "Email address is valid")

if __name__ == "__main__":
	# Test the function
	email = input("Enter an email address to validate: ")
	
	is_valid, reason = is_valid_email(email)
	
	if is_valid:
		print("✓ Valid email address!")
	else:
		print(f"✗ Invalid email address: {reason}")