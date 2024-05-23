#########################  9-1. Restaurant:

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant = Restaurant("Alice Pizza", "Pizza")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('\n\n\n')

######################  9-2. Three Restaurants: 

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")


restaurant1 = Restaurant("Alice Pizza", "Pizza")
restaurant2 = Restaurant("Sushi Palace", "Japanese")
restaurant3 = Restaurant("Burger Barn", "American")

restaurant1.describe_restaurant()
print('\n')
restaurant2.describe_restaurant()
print('\n')
restaurant3.describe_restaurant()
print('\n\n\n')

#####################  9-3. Users:

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user1 = User("John", "Doe", "johndoe", "johndoe@example.com", "New York")
user2 = User("Jane", "Doe", "janedoe", "janedoe@example.com", "Los Angeles")
user3 = User("Bob", "Smith", "bobsmith", "bobsmith@example.com", "Chicago")
#user1
user1.describe_user()
user1.greet_user()
print('\n')
#user2
user2.describe_user()
user2.greet_user()
print('\n')
#user3
user3.describe_user()
user3.greet_user()
print('\n\n\n')
#######################  9-4. Number Served:

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


restaurant = Restaurant("Alice Pizza", "Italian")
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")
print('\n\n\n')

#######################  9-5. Login Attempts

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("John", "Doe", "johndoe", "johndoe@example.com", "New York")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Login attempts: {user.login_attempts}")

user.reset_login_attempts()

print(f"Login attempts: {user.login_attempts}")
print('\n\n\n')

#######################  9-6. Ice Cream Stand:
    
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sunny's Ice Cream", "Ice Cream")
ice_cream_stand.flavors = ["Chocolate", "Vanilla", "Strawberry"]
ice_cream_stand.display_flavors()
print('\n\n\n')

#####################  9-7. Admin:

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com", "New York")
admin.show_privileges()
print('\n\n\n')

#########################  9-8. Privileges:

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

privileges = Privileges()
privileges.show_privileges()
print('\n\n\n')

######################  9-9. Battery Upgrade:

class ElectricCar:
    def __init__(self):
        self.battery = Battery()

class Battery:
    def __init__(self):
        self.capacity = 50

    def get_range(self):
        return self.capacity * 10

    def upgrade_battery(self):
        if self.capacity!= 65:
            self.capacity = 65

electric_car = ElectricCar()
print(electric_car.battery.get_range())
electric_car.battery.upgrade_battery()
print(electric_car.battery.get_range())
print("\n\n\n")

######################  9-10. Imported Restaurant:

#restaurant.py
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

#main.py
from restaurant import Restaurant

restaurant = Restaurant("Alice Pizza", "Pizza")
restaurant.describe_restaurant()
print("\n\n\n")

######################  9-11. Imported Admin:

# user.py
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

# main.py
from user import Admin

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com", "New York")
admin.show_privileges()
print("\n\n\n")

######################  9-12. Multiple Modules:

# user.py
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

# privileges.py
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

# admin.py
from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges.privileges:
            print(f"- {privilege}")

# main.py
from admin import Admin

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com", "New York")
admin.show_privileges()
