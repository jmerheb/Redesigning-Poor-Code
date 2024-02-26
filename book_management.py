from datetime import datetime

class book_manager:
    def __init__(self, storage):
        self.book_storage = storage

    # This function lists all book titles from storage when it is called by main.
    def list_books(self):
        titles = ""
        for book in self.book_storage.get_books():
            titles += "\n"
            titles += book['title']
        if titles == "":
            print("\nLibrary is empty.")
        else:
            print(titles)

    # These are the add/delete functions that add/delete books from storage when it is called by main.
    def add_book(self, title, author, isbn):
        self.book_storage.add_book(title, author, isbn)
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'ISBN: {isbn}'
        operation = f'ADD BOOK'
        self.book_storage.add_log(fix_dt, operation, object)

    def delete_book(self, isbn):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'ISBN: {isbn}'
        operation = f'DELETE BOOK'
        self.book_storage.add_log(fix_dt, operation, object)
        return self.book_storage.delete_book(isbn)

    # These are the update functions that will edit books from storage by title/author/isbn when called by main.
    def update_book_by_title(self, isbn, new_title):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'ISBN: {isbn}'
        operation = f'UPDATE BOOK'
        self.book_storage.add_log(fix_dt, operation, object)
        return self.book_storage.update_book_by_title(isbn, new_title)

    def update_book_by_author(self, isbn, new_author):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'ISBN: {isbn}'
        operation = f'UPDATE BOOK'
        self.book_storage.add_log(fix_dt, operation, object)
        return self.book_storage.update_book_by_author(isbn, new_author)

    def update_book_by_isbn(self, isbn, new_isbn):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'ISBN: {isbn}'
        operation = f'UPDATE BOOK'
        self.book_storage.add_log(fix_dt, operation, object)
        return self.book_storage.update_book_by_isbn(isbn, new_isbn)

    # These are the search functions that will search and return books from storage by title/author/isbn when called
    # by main.
    def search_book_by_title(self, title):
        title_list = []
        for book in self.book_storage.get_books():
            if book['title'].lower() == title.lower():
                title_list.append(book)
        book_str = ""
        for book in title_list:
            keys = list(book.keys())
            book_str += "\n"
            for key in keys:
                book_str += f"{key.capitalize()}: {book[key]}\n"
        if book_str == "":
            return "\nNo books found."
        else:
            return book_str

    def search_book_by_author(self, author):
        author_list = []
        for book in self.book_storage.get_books():
            if book["author"].lower() == author.lower():
                author_list.append(book)
        book_str = ""
        for book in author_list:
            keys = list(book.keys())
            book_str += "\n"
            for key in keys:
                book_str += f"{key.capitalize()}: {book[key]}\n"
        if book_str == "":
            return "\nNo books found."
        else:
            return book_str

    def search_book_by_isbn(self, isbn):
        book_str = ""
        for book in self.book_storage.get_books():
            if book["isbn"] == isbn:
                keys = list(book.keys())
                book_str += "\n"
                for key in keys:
                    book_str += f"{key.capitalize()}: {book[key]}\n"
        if book_str == "":
            return "\nNo books found."
        else:
            return book_str

    # This is the write function that will call the write_book function from storage before the code terminates to
    # add all data changes to the csv files. It also calls write_logs to trigger any log update.
    def write_books(self):
        self.book_storage.write_book()
        self.book_storage.write_logs()