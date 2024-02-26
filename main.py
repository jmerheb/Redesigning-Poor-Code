from checkout_management import checkout_manager
from book_management import book_manager
from user_management import user_manager
from storage import book_storage, user_storage


# Main menu that is displayed when program runs.
def main_menu():
    print("\nLibrary Management System")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Checkout a book")
    print("4. Checkin a book")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice


# Menu that displays if user chooses "Manage Books" from main menu.
def book_menu():
    print("\nManage Books")
    print("1. List all books")
    print("2. Add a book")
    print("3. Delete a book")
    print("4. Update a book")
    print("5. Search a book")
    print("0. Back")
    book_choice = input("Enter choice: ")
    return book_choice


# Menu that displays if user chooses "Manage Users" from main menu.
def user_menu():
    print("\nManage Users")
    print("1. List all users")
    print("2. Add a user")
    print("3. Delete a user")
    print("4. Update a user")
    print("5. Search a user")
    print("0. Back")
    user_choice = input("Enter choice: ")
    return user_choice


# Menu that displays if user chooses "Search a book" from book menu.
def book_search():
    print("\nWhat would you like to search by?")
    print("1. Title")
    print("2. Author")
    print("3. ISBN")
    print("0. Back")
    book_search_by = input("Enter choice: ")
    return book_search_by


# Menu that displays if user chooses "Update a book" from book menu.
def book_update():
    print("What part of the book would you like to update?")
    print("1. Title")
    print("2. Author")
    print("3. ISBN")
    print("0. Nevermind")
    book_update_by = input("Enter choice: ")
    return book_update_by


# Menu that displays if user chooses "Search a user" from user menu.
def user_search():
    print("\nWhat would you like to search by?")
    print("1. Name")
    print("2. User ID")
    print("0. Back")
    user_search_by = input("Enter choice: ")
    return user_search_by


# Menu that displays if user chooses "Update a user" from user menu.
def user_update():
    print("What part of the user would you like to update?")
    print("1. Name")
    print("2. User ID")
    print("0. Nevermind")
    user_update_by = input("Enter choice: ")
    return user_update_by


'''
The main method runs first and handles user input. It allows for input errors by responding to the user when they input
anything incorrectly and allows them to keep trying until they terminate the code. When the code is terminated, all 
changes in data are saved to the csv files, and the user can start the code up again to continue where they left off. 
'''
def main():
    b_storage = book_storage()
    book_management = book_manager(b_storage)
    u_storage = user_storage()
    user_management = user_manager(u_storage)
    checkout_management = checkout_manager(b_storage, u_storage)
    while True:
        choice = main_menu()
        if choice == '1':
            while True:
                book_choice = book_menu()
                if book_choice == '1':
                    book_management.list_books()
                    break
                elif book_choice == '2':
                    title = input("Enter title: ")
                    author = input("Enter author: ")
                    isbn = input("Enter ISBN: ")
                    book_management.add_book(title, author, isbn)
                    print("\nBook added.")
                    break
                elif book_choice == '3':
                    isbn = input("Enter the ISBN of the book you would like to delete: ")
                    print(book_management.delete_book(isbn))
                    break
                elif book_choice == '4':
                    while True:
                        isbn = input("\nEnter the ISBN of the book you would like to update: ")
                        book_update_by = book_update()
                        if book_update_by == '1':
                            title = input("Enter the new title of the book: ")
                            print(book_management.update_book_by_title(isbn, title))
                            break
                        elif book_update_by == '2':
                            author = input("Enter the new author of the book: ")
                            print(book_management.update_book_by_author(isbn, author))
                            break
                        elif book_update_by == '3':
                            new_isbn = input("Enter the new ISBN of the book: ")
                            print(book_management.update_book_by_isbn(isbn, new_isbn))
                            break
                        elif book_update_by == '0':
                            break
                        else:
                            print("Invalid choice, please try again.")
                elif book_choice == '5':
                    while True:
                        book_search_by = book_search()
                        if book_search_by == '1':
                            title = input("Enter the title of the book(s) you would like to search: ")
                            print(book_management.search_book_by_title(title))
                            break
                        elif book_search_by == '2':
                            author = input("Enter the author of the book(s) you would like to search: ")
                            print(book_management.search_book_by_author(author))
                            break
                        elif book_search_by == '3':
                            isbn = input("Enter the ISBN of the book you would like to search: ")
                            print(book_management.search_book_by_isbn(isbn))
                            break
                        elif book_search_by == '0':
                            break
                        else:
                            print("Invalid choice, please try again.")
                elif book_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '2':
            while True:
                user_choice = user_menu()
                if user_choice == '1':
                    user_management.list_users()
                    break
                elif user_choice == '2':
                    name = input("Enter user name: ")
                    user_id = input("Enter user ID: ")
                    user_management.add_user(name, user_id)
                    print("\nUser added.")
                    break
                elif user_choice == '3':
                    user_id = input("Enter the user ID of the user you would like to delete: ")
                    print(user_management.delete_user(user_id))
                    break
                elif user_choice == '4':
                    while True:
                        user_id = input("\nEnter the User ID of the user you would like to update: ")
                        user_update_by = user_update()
                        if user_update_by == '1':
                            name = input("Enter the new name of the user: ")
                            print(user_management.update_user_by_name(user_id, name))
                            break
                        elif user_update_by == '2':
                            new_user_id = input("Enter the new ID of the user: ")
                            print(user_management.update_user_by_id(user_id, new_user_id))
                            break
                        elif user_update_by == '0':
                            break
                        else:
                            print("Invalid choice, please try again.")
                elif user_choice == '5':
                    while True:
                        user_search_by = user_search()
                        if user_search_by == '1':
                            name = input("Enter the name of the user(s) you would like to search: ")
                            print(user_management.search_user_by_name(name))
                            break
                        elif user_search_by == '2':
                            user_id = input("Enter the ID of the user you would like to search: ")
                            print(user_management.search_user_by_id(user_id))
                            break
                        elif user_search_by == '0':
                            break
                        else:
                            print("Invalid choice, please try again.")
                elif user_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")

        elif choice == '3':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkout: ")
            print(checkout_management.checkout_book(user_id, isbn))
        elif choice == '4':
            user_id = input("Enter user ID: ")
            isbn = input("Enter ISBN of the book to checkin: ")
            print(checkout_management.checkin_book(user_id, isbn))
        elif choice == '0':
            print("\nExiting.")
            book_management.write_books()
            user_management.write_users()
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
