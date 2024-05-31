#  EDOARDO DI LISIO

#  Exercise 1: Creating an Abstract Class with Abstract Methods
from abc import ABC, abstractmethod
import math

# Define the abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Define the Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

# Define the Rectangle subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Test examples
def test_shapes():
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]
    
    for shape in shapes:
        print(f"{shape.__class__.__name__}:")
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}\n")

# Run the test examples
test_shapes()
print("\n\n")


#  Exercise 2: Implementing Static Methods

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Test examples
def test_math_operations():
    print("MathOperations Tests:")
    print(f"Add 3 and 5: {MathOperations.add(3, 5)}")
    print(f"Multiply 4 and 7: {MathOperations.multiply(4, 7)}")
    print(f"Add -1 and 10: {MathOperations.add(-1, 10)}")
    print(f"Multiply 0 and 5: {MathOperations.multiply(0, 5)}")

# Run the test examples
test_math_operations()


#  Exercise 3: Library Management System 




#  Exercise 4: University Management System

