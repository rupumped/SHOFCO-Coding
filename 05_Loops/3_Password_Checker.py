# Set the correct password
correct_password = "shofco2025"
attempts = 0
max_attempts = 3

print("Welcome to the SHOFCO Computer Lab")

# Keep asking for password until correct or too many attempts
while attempts < max_attempts:
    password = input("Please enter the password: ")
    attempts = attempts + 1
    
    # Check if password is correct
    if password == correct_password:
        print("Correct password! Access granted.")
        break
    else:
        attempts_left = max_attempts - attempts
        if attempts_left > 0:
            print(f"Incorrect password. You have {attempts_left} attempts left.")
        else:
            print("Too many incorrect attempts. Access denied.")