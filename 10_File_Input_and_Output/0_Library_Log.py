def log_borrowed_book(student_name, book_title, date_borrowed):
	"""
	Logs information about a borrowed book to a file.
	
	Args:
		student_name (str): Name of student borrowing the book
		book_title (str): Title of the book being borrowed
		date_borrowed (str): Date when the book was borrowed
	"""
	# Open file in append mode to add new entries
	with open("library_log.txt", "a") as file:
		file.write(f"{student_name},{book_title},{date_borrowed},Not Returned\n")
	print(f"Book '{book_title}' has been logged as borrowed by {student_name}.")

def display_borrowed_books():
	"""
	Reads and displays all borrowed books from the log file.
	"""
	try:
		with open("library_log.txt", "r") as file:
			print("\n--- BORROWED BOOKS LOG ---")
			print("Student, Book Title, Date Borrowed, Status")
			print("----------------------------------------")
			for line in file:
				print(line.strip())
	except FileNotFoundError:
		print("No books have been borrowed yet.")

if __name__ == "__main__":
	# Program starts here when run directly
	print("SHOFCO Library Book Logger")
	print("-------------------------")
	
	while True:
		print("\nOptions:")
		print("1. Log a borrowed book")
		print("2. View all borrowed books")
		print("3. Exit")
		
		choice = input("\nEnter your choice (1-3): ")
		
		if choice == "1":
			name = input("Enter student name: ")
			title = input("Enter book title: ")
			date = input("Enter today's date (DD/MM/YYYY): ")
			log_borrowed_book(name, title, date)
		elif choice == "2":
			display_borrowed_books()
		elif choice == "3":
			print("Thank you for using the Library Book Logger!")
			break
		else:
			print("Invalid choice. Please try again.")