import csv
from datetime import datetime

class book_storage:
    def __init__(self):
        with open('Books.csv', 'r') as csv_file:
            books_reader = csv.reader(csv_file)
            self.books_fields = next(books_reader)
            self.csv_list = []

            # Creates book log list.
            self.log_list = []
            self.log_fields = ["Date", "Operation", "Object"]

            # Reformats list of dicts from Books.csv to be used more easily in other functions.
            self.books_fields[0] = 'title'
            for line in books_reader:
                book_dict = {}
                for i in range(0, len(self.books_fields)):
                    book_dict[self.books_fields[i]] = line[i]

                self.csv_list.append(book_dict)

    # These functions write updated logs to BookLogs."
    def add_log(self, date, operation, object):
        log = f"{date} - {operation} PERFORMED ON {object}\n"
        self.log_list.append(log)

    def write_logs(self):
        with open ('./BookLogs', 'a') as log_file:
            log_file.writelines(self.log_list)

    # Returns list of dicts of all books from Books.csv.
    def get_books(self):
        return self.csv_list

    # These functions add/delete books to/from Books.csv with the information called by book manager.
    def add_book(self, title, author, isbn):
        self.csv_list.append({"title": title, "author": author, "isbn": isbn, "availability": 'true'})

    def delete_book(self, isbn):
        for book in self.csv_list:
            if book["isbn"] == isbn:
                self.csv_list.remove(book)
                return "\nBook deleted."
        return "\nISBN does not exist."

    # These functions edit books from Books.csv with the information called by book manager.
    def update_book_by_title(self, isbn, new_title):
        for book in self.csv_list:
            if book["isbn"] == isbn:
                book["title"] = new_title
                return "\nSuccessfully updated book."
        return "\nISBN does not exist."

    def update_book_by_author(self, isbn, new_author):
        for book in self.csv_list:
            if book["isbn"] == isbn:
                book["author"] = new_author
                return "\nSuccessfully updated book."
        return "\nISBN does not exist."

    def update_book_by_isbn(self, isbn, new_isbn):
        for book in self.csv_list:
            if int(book["isbn"]) == isbn:
                book["isbn"] = new_isbn
                return "\nSuccessfully updated book."
        return "\nISBN does not exist."

    # This function checks to see if a book is available when it is called by checkout manager. If the book is
    # available, this function will update its availability on Books.csv and allow the function in checkout manager to
    # continue.
    def checkout_book(self, isbn):
        for book in self.csv_list:
            if int(book["isbn"]) == int(isbn) and str(book["availability"]).lower() == "true":
                book["availability"] = "false"
                return True
        return False

    # This function checks to see if a book that a user wants to check in is actually checked out by them when it is
    # called by checkout manager. If it is, this function will update its availability on Books.csv and allow the
    # function in checkout manager to continue.
    def checkin_book(self, isbn):
        for book in self.csv_list:
            if int(book["isbn"]) == int(isbn) and str(book["availability"]).lower() == "false":
                book["availability"] = "true"
                return True
        return False

    # This is the write function that will write to Books.csv before the code terminates.
    def write_book(self):
        with open('Books.csv', 'w', newline="") as csv_file:
            books_writer = csv.DictWriter(csv_file, fieldnames=self.books_fields)
            books_writer.writeheader()
            books_writer.writerows(self.csv_list)

class user_storage:
    def __init__(self):
        with open('Users.csv', 'r') as csv_file:
            users_reader = csv.reader(csv_file)
            self.users_fields = next(users_reader)
            self.csv_list = []

            # Creates user log list.
            self.log_list = []
            self.log_fields = ["Date", "Operation", "Object"]

            # Reformats list of dicts from Users.csv to be used more easily in other functions.
            self.users_fields[0] = 'name'
            for line in users_reader:
                user_dict = {}
                for i in range(0, len(self.users_fields)):
                    user_dict[self.users_fields[i]] = line[i]

                self.csv_list.append(user_dict)

    # These functions write updated logs to UserLogs."
    def add_log(self, date, operation, object):
        log = f"{date} - {operation} PERFORMED ON {object}\n"
        self.log_list.append(log)

    def write_logs(self):
        with open('./UserLogs', 'a') as log_file:
            log_file.writelines(self.log_list)

    # Returns list of dicts of all users from Users.csv.
    def get_users(self):
        return self.csv_list

    # These functions add/delete users to/from Users.csv with the information called by user manager.
    def add_user(self, name, user_id):
        self.csv_list.append({"name": name, "user_id": user_id, "books": "none"})

    def delete_user(self, user_id):
        for user in self.csv_list:
            if user["user_id"] == user_id:
                self.csv_list.remove(user)
                return "\nUser deleted."
        return "\nUser ID does not exist."

    # These functions edit users from Users.csv with the information called by user manager.
    def update_user_by_name(self, user_id, new_name):
        for user in self.csv_list:
            if user["user_id"] == user_id:
                user["name"] = new_name
                return "\nSuccessfully updated user."
        return "\nUser ID does not exist."

    def update_user_by_id(self, user_id, new_user_id):
        for user in self.csv_list:
            if int(user["user_id"]) == user_id:
                user["user_id"] = new_user_id
                return "\nSuccessfully updated user."
        return "\nUser ID does not exist."

    # This function adds books to user profiles when they check them out. This function occurs after checkout
    # manager successfully runs through checkout_book in book_storage.
    def checkout_book(self, user_id, isbn):
        for user in self.csv_list:
            if int(user["user_id"]) == int(user_id):
                if user["books"] == "none":
                    user["books"] = f"{isbn}:"
                    dt = datetime.now()
                    fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
                    object = f'USER ID: {user_id}'
                    operation = f'BOOK CHECK-OUT'
                    self.add_log(fix_dt, operation, object)
                    return "\nSuccessfully checked-out book."
                else:
                    user["books"] += f"{isbn}:"
                    dt = datetime.now()
                    fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
                    object = f'USER ID: {user_id}'
                    operation = f'BOOK CHECK-OUT'
                    self.add_log(fix_dt, operation, object)
                    return "\nSuccessfully checked-out book."

    # This function removes books from user profiles when they check them in. This function occurs after checkout
    # manager successfully runs through checkin_book in book_storage.
    def checkin_book(self, user_id, isbn):
        for user in self.csv_list:
            if int(user["user_id"]) == int(user_id):
                if user["books"] == "none":
                    return "\nUser has no books checked-out."
                else:
                    books = user["books"].split(':')[:-1]
                    if str(isbn) in books:
                        books.remove(str(isbn))
                        books_str = ':'.join(books) + ':'
                        if books_str == ':':
                            books_str = "none"
                        new_user = user
                        new_user["books"] = books_str
                        self.csv_list.remove(user)
                        self.csv_list.append(new_user)

                        dt = datetime.now()
                        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
                        object = f'USER ID: {user_id}'
                        operation = f'BOOK CHECK-IN'
                        self.add_log(fix_dt, operation, object)
                        return "\nSuccessfully checked-in book."
                    else:
                        return "\nUser never checked-out book."

    # This is the write function that will write to Users.csv before the code terminates.
    def write_user(self):
        with open('Users.csv', 'w', newline="") as csv_file:
            users_writer = csv.DictWriter(csv_file, fieldnames=self.users_fields)
            users_writer.writeheader()
            users_writer.writerows(self.csv_list)