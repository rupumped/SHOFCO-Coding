def search_book(title, available_books):
	"""Search for a book in the library.
	
	Args:
		title: The title to search for
		available_books: Dictionary of books with availability status
		
	Returns:
		Information about the book if found
		
	Raises:
		KeyError: If the book is not found
	"""
	title = title.lower()
	
	if title in available_books:
		return available_books[title]
	else:
		raise KeyError("Book not found")

def display_book_status(book_info):
	"""Display information about a book."""
	print(f"Title: {book_info['title']}")
	print(f"Author: {book_info['author']}")
	
	if book_info['available']:
		print("Status: Available")
		print(f"Location: Shelf {book_info['shelf']}")
	else:
		print("Status: Currently borrowed")
		print(f"Due back: {book_info['due_date']}")

def run_library_search():
	"""Run the library book search program."""
	# Sample book database (in a real program, this would come from a file)
	books = {
		"things fall apart": {
			"title": "Things Fall Apart",
			"author": "Chinua Achebe",
			"available": True,
			"shelf": "B3"
		},
		"river and the source": {
			"title": "The River and the Source",
			"author": "Margaret A. Ogola",
			"available": False,
			"due_date": "May 5"
		},
		"born a crime": {
			"title": "Born a Crime",
			"author": "Trevor Noah",
			"available": True,
			"shelf": "A7"
		}
	}
	
	try:
		book_title = input("Enter the book title you are looking for: ")
		book_info = search_book(book_title, books)
		display_book_status(book_info)
	
	except KeyError:
		print("Sorry, that book is not in our library.")
		suggestion = input("Would you like to suggest this book for purchase? (yes/no): ")
		if suggestion.lower() == "yes":
			print("Thank you! Your suggestion has been recorded.")
	
	except Exception as e:
		print(f"An error occurred: {e}")

if __name__ == "__main__":
	print("Welcome to SHOFCO Library Book Search!")
	run_library_search()