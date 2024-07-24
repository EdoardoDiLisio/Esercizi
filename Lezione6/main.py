##################################################  LEZIONE 6  ##########################################################

##################  9-10  ##################
from restaurant import Restaurant

restaurant = Restaurant("Alice Pizza", "Pizza")
restaurant.describe_restaurant()

##################  9-11  ##################
from user import Admin

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com", "New York")
admin.show_privileges()

##################  9-12  ##################

from admin import Admin

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com", "New York")
admin.show_privileges()

##################   .     ##################