'''
9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and 
a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() 
that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes 
individually, and then call both methods.

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
'''

'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, 
and call describe_restaurant() for each instance.

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
'''

'''
9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other
attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users,
and call both methods for each user.
'''
