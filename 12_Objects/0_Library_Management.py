class LibraryBook:
	def __init__(self, title, author, category, pages):
		self.title = title
		self.author = author
		self.category = category
		self.pages = pages
		self.available = True
		self.borrower = None
		self.due_date = None
	
	def borrow(self, student_name, days=14):
		if self.available:
			self.available = False
			self.borrower = student_name
			import datetime
			self.due_date = datetime.datetime.now() + datetime.timedelta(days=days)
			return True
		else:
			return False
	
	def return_book(self):
		if not self.available:
			self.available = True
			self.borrower = None
			self.due_date = None
			return True
		else:
			return False
	
	def is_overdue(self):
		if not self.available and self.due_date:
			import datetime
			return datetime.datetime.now() > self.due_date
		return False
	
	def display_info(self):
		status = "Available" if self.available else f"Borrowed by {self.borrower}"
		print(f"Title: {self.title}")
		print(f"Author: {self.author}")
		print(f"Category: {self.category}")
		print(f"Pages: {self.pages}")
		print(f"Status: {status}")
		if not self.available:
			print(f"Due date: {self.due_date.strftime('%d-%m-%Y')}")


if __name__ == "__main__":
	# Create some books
	book1 = LibraryBook("Things Fall Apart", "Chinua Achebe", "Fiction", 209)
	book2 = LibraryBook("Mathematics Grade 8", "Kenya Education Board", "Textbook", 156)
	
	# Test book1
	print("Book 1 information:")
	book1.display_info()
	print("\nBorrowing book 1...")
	book1.borrow("Wanjiku")
	book1.display_info()
	
	# Test book2
	print("\nBook 2 information:")
	book2.display_info()
	print("\nBorrowing book 2...")
	book2.borrow("Omondi", days=7)
	book2.display_info()
	
	# Return a book
	print("\nReturning book 2...")
	book2.return_book()
	book2.display_info()