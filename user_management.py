from datetime import datetime

class user_manager:
    def __init__(self, storage):
        self.user_storage = storage

    # This function lists all user names from storage when it is called by main.
    def list_users(self):
        names = ""
        for user in self.user_storage.get_users():
            names += "\n"
            names += user['name']
        if names == "":
            print("\nLibrary is empty.")
        else:
            print(names)

    # These are the add/delete functions that add/delete users from storage when it is called by main.
    def add_user(self, name, user_id):
        self.user_storage.add_user(name, user_id)
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'USER ID: {user_id}'
        operation = f'ADD USER'
        self.user_storage.add_log(fix_dt, operation, object)

    def delete_user(self, user_id):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'USER ID: {user_id}'
        operation = f'DELETE USER'
        self.user_storage.add_log(fix_dt, operation, object)
        return self.user_storage.delete_user(user_id)

    # These are the update functions that will edit users from storage by name/user-ID when called by main.
    def update_user_by_name(self, user_id, new_name):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'USER ID: {user_id}'
        operation = f'UPDATE USER'
        self.user_storage.add_log(fix_dt, operation, object)
        return self.user_storage.update_user_by_name(user_id, new_name)

    def update_user_by_id(self, user_id, new_user_id):
        dt = datetime.now()
        fix_dt = f'{dt.year} {dt.month}-{dt.day} {dt.hour}:{dt.minute}:{dt.second}'
        object = f'USER ID: {user_id}'
        operation = f'UPDATE USER'
        self.user_storage.add_log(fix_dt, operation, object)
        return self.user_storage.update_user_by_id(user_id, new_user_id)

    # These are the search functions that will search and return users from storage by name/user-ID when called
    # by main.
    def search_user_by_name(self, name):
        name_list = []
        for user in self.user_storage.get_users():
            if user['name'].lower() == name.lower():
                name_list.append(user)
        user_str = ""
        for user in name_list:
            keys = list(user.keys())
            user_str += "\n"
            for key in keys:
                if key == "books":
                    if user[key] == "none":
                        pass
                    else:
                        new_val = user[key].split(":")
                        new_val = new_val[:len(new_val) - 1]
                        book_str = ""
                        for val in new_val:
                            book_str += f"{val}, "
                        user_str += f"{key.capitalize()}: {book_str}\n"
                        continue
                user_str += f"{key.capitalize()}: {user[key]}\n"
        if user_str == "":
            return "\nNo users found."
        else:
            return user_str

    def search_user_by_id(self, user_id):
        user_str = ""
        for user in self.user_storage.get_users():
            if user["user_id"] == user_id:
                keys = list(user.keys())
                user_str += "\n"
                for key in keys:
                    user_str += f"{key.capitalize()}: {user[key]}\n"
        if user_str == "":
            return "\nNo users found."
        else:
            return user_str

    # This is the write function that will call the write_user function from storage before the code terminates to
    # add all data changes to the csv files. It also calls write_logs to trigger any log update.
    def write_users(self):
        self.user_storage.write_user()
        self.user_storage.write_logs()