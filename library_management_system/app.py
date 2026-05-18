from login import login_menu
from manager import LibraryManager


def book_title():
    return str(input("Enter the Book Title:")).lower().strip()


manager = LibraryManager()
while True:
    print("====Welcome to Library Management System====")
    print("=" * 50)
    user_name = input("UserName:")
    user_phonenumber = input("User Phone Number:")
    login_success = login_menu(user_name, user_phonenumber)

    if login_success:
        while True:
            print(f"==== Welcome {user_name} ====")

            try:
                user_menu_choice = int(
                    input("==MENU==\n1-Borrow Book\n2-Return Book\n3-Search Book\n4-Exit\n"))
            except ValueError:
                print("Enter numbers only")
                continue

            if user_menu_choice == 1:
                book_borrow_success = manager.borrow_book(book_title())
                
                if book_borrow_success:
                    manager.save_books()
                    print("Borrowed Successfully")
                else:
                    print("Error")
                    
            elif user_menu_choice == 2:
                book_return_success = manager.return_book(book_title())

                if book_return_success:
                    manager.save_books()
                    print("Returned Successfully")
                else:
                    print("Error")
                    

            elif user_menu_choice == 3:
                book_data = manager.search_book(book_title())
                if book_data:
                    availability = "Available" if book_data.is_available else "Borrowed"
                    print(
                        f"Title: {book_data.title.title()} "
                        f"by {book_data.author.title()}\n"
                        f"Availability: {availability}"
                    )
                else:
                    print("Book Not Found")
                    

            elif user_menu_choice == 4:
                print("Logging out...")
                break
    else:
        print("Login Failed")
