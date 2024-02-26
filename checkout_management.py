
class checkout_manager:
    def __init__(self, b_storage, u_storage):
        self.b_storage = b_storage
        self.u_storage = u_storage

    # These functions check-out/check-in books for certain users from storage when it is called by main.
    def checkout_book(self, user_id, isbn):
        res = self.b_storage.checkout_book(isbn)
        if res:
            return self.u_storage.checkout_book(user_id, isbn)
        else:
            return "\nThis book is already checked-out."

    def checkin_book(self, user_id, isbn):
        res = self.b_storage.checkin_book(isbn)
        if res:
            return self.u_storage.checkin_book(user_id, isbn)
        else:
            return "\nThis book was never checked-out."