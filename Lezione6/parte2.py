'''
ESERCIZIO N.2

1. Write a class called Student with the attributes name (str) and studyProgram (str);
2. create three instance. one for yourself, left and right neighbour;
3. Add a method printInfo that prints the name and studyProgram of a Student. Test your method on the object!
4. modify the code and add age and gender to the attributes. Modify your printing methods respectively too
'''
'''
class Student:
    def __init__(self, name, study_program, age = None, gender = None):
        self.name = name
        self.study_program = study_program
        self.age = age
        self.gender = gender

    def print_info(self):
        print("Name:", self.name)
        print("Study Program:", self.study_program)
        if self.age is not None:
            print("Age:", self.age)
        if self.gender is not None:
            print("Gender:", self.gender)
        print()

Me = Student("Edoardo_Di_Lisio", "Cyber_Security", 20, "Male")
Left_neighbour = Student("Mario_Rossi", "Cyber_Security", 20, "Male")
Right_neighbour = Student("Anna_Bianchi", "Cyber_Security", 22, "Female")

Me.print_info()
Left_neighbour.print_info()
Right_neighbour.print_info()
'''
'''
ESERCIZIO N.3
1.  Create two realistic instances of Animals
2.  Print the name of each object
3.  Change the amount of legs of one object using the dot notation
4.  Add a method setLegs() to set the legs of an object and repeat task 3 but this time using the method.
5.  Add a method getLegs() to return the amount of legs
6.  Add a method named printInfo that prints all attributes of the Animal
'''

#primo metodo
'''
class Animals:
    def __init__(self, Name:str, Age:str, Legs:str) -> None:
        self.name = Name
        self.age = Age
        self.legs = Legs
        
    def setLegs(self, legs: int):
        self.legs = legs
        
    def getLegs(self):
        return self.legs
        
    def printInfo(self) -> str:
        print(f'{self.name}, {self.age}, {self.legs}')

Dog : Animals = Animals (Name="Bob", Age=4, Legs=4)
Bird : Animals = Animals (Name="Rocky", Age=10, Legs=2)

#punto 1
print(Dog.name, "\n",Bird.name, sep='')

#punto 2
Bird.legs = 5
print(Bird.legs)

#punto 3
Bird.setLegs(1)
print(Bird.legs)

#punto 4
Bird.getLegs()
print(Bird.getLegs())

Bird.printInfo()
'''
#secondo metodo
'''
class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def set_legs(self, legs):
        self.legs = legs

    def get_legs(self):
        return self.legs

    def print_info(self):
        print("Name:", self.name)
        print("Species:", self.species)
        print("Legs:", self.legs)
        print()

# Create two instances of Animal
animal1 = Animal("Bobby", "Dog", 4)
animal2 = Animal("Arlo", "Cat", 4)

# Print the name of each object
print("Name of animal1:", animal1.name)
print("Name of animal2:", animal2.name)

# Change the amount of legs of one object using the dot notation
animal1.legs = 3

# Print the amount of legs using dot notation
print("Legs of animal1 (after modification):", animal1.legs)

# Change the amount of legs of animal1 using the method
animal1.set_legs(4)

# Print the amount of legs using the method
print("Legs of animal1 (after method call):", animal1.get_legs())

# Print all attributes of each animal using the print_info method
print("Info of animal1:")
animal1.print_info()

print("Info of animal2:")
animal2.print_info()
'''

'''
ESERCIZIO 4

1.  Write a new class called Food, it should have name, price and
    description as attributes.
2.  Instantiate at least three different foods you know and like.
3.  Create a new class called Menu, it should have a list (of Foods) as attribute.
    __init__ should take a list of Foods as optional parameters (default=[])
4.  Create a addFood() and removeFood() for the Menu
5.  Create a few new Food instances. Add each to the Menu using the respective
    Method.
6.  Add a method printPrices() that list all items on the Menu with their
    prices.
7.  Add a Menu method getAveragePrice() that returns the average Food
    price of the Menu
'''

class Food:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

class Menu:
    def __init__(self):
        self.foods = []

    def addFood(self, food):
        self.foods.append(food)

    def removeFood(self, food):
        self.foods.remove(food)

    def printPrices(self):
        for food in self.foods:
            print(food.name, "-", food.price)

    def getAveragePrice(self):
        if not self.foods:
            return 0
        total_price = sum(food.price for food in self.foods)
        return total_price / len(self.foods)

# Creare alcuni oggetti Food
pizza = Food("Pizza", 12.99, "Una pizza classica italiana con condimenti")
burger = Food("Burger", 8.99, "Un succulento hamburger di manzo in un panino con condimenti")
insalata = Food("Insalata", 7.49, "Un mix fresco di verdure con condimento")

# Creare un menu e aggiungere il cibo
menu = Menu()
menu.addFood(pizza)
menu.addFood(burger)
menu.addFood(insalata)

# Stampare i prezzi del menu
print("Prezzi nel menu:")
menu.printPrices()

# Calcolare il prezzo medio degli articoli nel menu
average_price = menu.getAveragePrice()
print("\nPrezzo medio degli articoli nel menu:", average_price)
