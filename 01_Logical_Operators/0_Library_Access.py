# Library variables
has_library_card = True
has_returned_previous_books = True
is_registered_student = True

# Check if person can borrow books (needs all three conditions)
can_borrow_books = has_library_card and has_returned_previous_books and is_registered_student

# Display results
print("Library Card:", has_library_card)
print("Previous Books Returned:", has_returned_previous_books)
print("Registered Student:", is_registered_student)
print("Can Borrow Books:", can_borrow_books)

# Try changing the variables to False and see how the result changes!