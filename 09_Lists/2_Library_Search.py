def search_books(book_titles, book_available, search_term):
	"""Search for books containing the search term."""
	found = False
	for i in range(len(book_titles)):
		# Check if search term is in the title (case insensitive)
		if search_term.lower() in book_titles[i].lower():
			found = True
			availability = "Available" if book_available[i] else "Checked out"
			print(f"Found: {book_titles[i]} - {availability}")
	
	if not found:
		print("No books found matching your search.")
	
	return found

def library_search_system(book_titles, book_available):
	"""Run the interactive library search system."""
	while True:
		search = input("\nEnter a book to search for (or 'exit' to quit): ")
		
		if search.lower() == "exit":
			print("Thank you for using the SHOFCO library system!")
			break
		
		search_books(book_titles, book_available, search)

if __name__ == "__main__":
	# Lists for library books
	book_titles = ["Python Basics", "Math Adventures", "Kenya History", "Science Explorer", "English Grammar"]
	book_available = [True, False, True, True, False]
	
	print("Welcome to the SHOFCO Library System")
	library_search_system(book_titles, book_available)