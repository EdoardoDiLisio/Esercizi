class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges.privileges:
            print(f"- {privilege}")
