# Library variables - try changing these values to see different results
has_library_card = input("Do you have a library card? (Y/N): ").upper() == 'Y'
is_registered_student = input("Are you a registered student? (Y/N): ").upper() == 'Y'
books_currently_borrowed = int(input("How many books are you currently borrowing? "))
days_overdue = int(input("How many days overdue are the books you are borrowing? If none, enter 0: "))  # if any books are overdue, how many days

# Check eligibility with detailed messages and nested conditionals
if not is_registered_student:
    print("You cannot borrow books: Only registered SHOFCO students can use the library.")
elif not has_library_card:
    print("You cannot borrow books: Please visit the librarian to get your library card.")
elif days_overdue > 0:
    fine = days_overdue * 5  # 5 KSh per day late
    print(f"You need to pay an overdue fine of {fine} KSh before borrowing more books.")
else:
    # Eligible to borrow, but need to check limits
    print("Checking how many books you can borrow...")
    
    grade_level = int(input("What grade are you in? "))
    
    if grade_level >= 9:
        max_books = 3
    elif grade_level >= 6:
        max_books = 2
    else:
        max_books = 1
    
    books_available = max_books - books_currently_borrowed
    
    if books_available <= 0:
        print(f"You have already borrowed your limit of {max_books} books.")
        print("Please return at least one book before borrowing more.")
    else:
        print(f"You can borrow {books_available} more book(s)!")
        
        # Optional: Ask if student wants to search for a book
        wants_to_search = input("Would you like to search for a book? (Y/N): ").upper() == 'Y'
        
        if wants_to_search:
            print("Redirecting to book search system...")
        else:
            print("Thank you for visiting the SHOFCO library!")