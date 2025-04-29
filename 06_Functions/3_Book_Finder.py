def find_book_location(book_title):
	"""
	Determine where a book is located in the SHOFCO library.
	"""
	# Convert book title to lowercase for easier comparison
	title_lower = book_title.lower()
	
	if "history" in title_lower or "culture" in title_lower:
		section = "History Section (Blue Shelves)"
	elif "science" in title_lower or "math" in title_lower:
		section = "Science Section (Green Shelves)"
	elif "story" in title_lower or "novel" in title_lower or "tale" in title_lower:
		section = "Fiction Section (Red Shelves)"
	elif "computer" in title_lower or "programming" in title_lower:
		section = "Technology Section (Yellow Shelves)"
	else:
		section = "General Section (White Shelves)"
	
	return section

# Example usage
if __name__ == "__main__":
	book1 = "The Story of Kenya"
	book2 = "Computer Programming for Beginners"
	book3 = "Advanced Mathematics"
	
	print(f"'{book1}' can be found in the {find_book_location(book1)}")
	print(f"'{book2}' can be found in the {find_book_location(book2)}")
	print(f"'{book3}' can be found in the {find_book_location(book3)}")
	
	# Try with your favorite book!