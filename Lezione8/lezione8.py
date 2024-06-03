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
print("\n\n")

#  Exercise 3: Library Management System 

class Book:
    def __init__(self, title, author, isbn):
        # Initializing attributes for a book
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        # Generating a string representation of the book
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
    
    @classmethod
    def from_string(cls, book_str):
        # This method creates a Book instance from a string in the format "title, author, isbn"
        # Splitting the book string into title, author, and isbn
        title, author, isbn = book_str.split(', ')
        # Returning a new Book instance using the extracted information
        return cls(title, author, isbn)

class Member:
    def __init__(self, name, member_id):
        # Initializing attributes for a member
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        # Adding a book to the list of borrowed books for the member
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        # Removing a book from the list of borrowed books for the member
        self.borrowed_books.remove(book)
    
    def __str__(self):
        # Generating a string representation of the member
        return f"Name: {self.name}, Member ID: {self.member_id}"

    @classmethod
    def from_string(cls, member_str):
        # This method creates a Member instance from a string in the format "name, member_id"
        # Splitting the member string into name and member_id
        name, member_id = member_str.split(', ')
        # Returning a new Member instance using the extracted information
        return cls(name, member_id)

class Library:
    total_books = 0
    
    def __init__(self):
        # Initializing attributes for a library
        self.books = []
        self.members = []
    
    def add_book(self, book):
        # Adding a book to the library and incrementing total_books
        self.books.append(book)
        Library.total_books += 1
    
    def remove_book(self, book):
        # Removing a book from the library and decrementing total_books
        self.books.remove(book)
        Library.total_books -= 1
    
    def register_member(self, member):
        # Adding a member to the library
        self.members.append(member)
    
    def lend_book(self, book, member):
        # Lending a book to a member if both book and member exist
        if book in self.books and member in self.members:
            member.borrow_book(book)
            self.remove_book(book)
            print(f"{book.title} has been borrowed by {member.name}.")
        else:
            print("Book or member not found or registered.")
    
    def __str__(self):
        # Generating a string representation of the library
        book_list = "\n".join([book.__str__() for book in self.books])
        member_list = "\n".join([member.__str__() for member in self.members])
        return f"Books:\n{book_list}\nMembers:\n{member_list}"

    @classmethod
    def library_statistics(cls):
        # Printing the total number of books in the library
        print(f"Total number of books in the library: {cls.total_books}")

#Test

# Creating instances and testing
divina_commedia = Book.from_string("La Divina Commedia, D. Alighieri, 999000666")
member1 = Member.from_string("John Doe, 001")
library = Library()

# Adding the book to the library
library.add_book(divina_commedia)

# Registering the member
library.register_member(member1)

# Displaying the library before lending
print("Library before lending:")
print(library)

# Lending the book to the member
library.lend_book(divina_commedia, member1)

# Displaying the library after lending
print("\nLibrary after lending:")
print(library)

# Displaying library statistics
Library.library_statistics()
print("\n\n")

#  Exercise 4: University Management System

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        # Initializing common attributes for all subclasses
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_role(self):
        # Abstract method to be implemented by subclasses
        pass
    
    def __str__(self):
        # Generating a string representation of the person
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        # Initializing additional attributes specific to students
        self.student_id = student_id
        self.courses = []
    
    def get_role(self):
        return "Student"
    
    def enroll(self, course):
        # Enrolling the student in a course
        self.courses.append(course)

class Professor(Person):
    def __init__(self, name, age, professor_id, department):
        super().__init__(name, age)
        # Initializing additional attributes specific to professors
        self.professor_id = professor_id
        self.department = department
        self.courses = []
    
    def get_role(self):
        return "Professor"
    
    def assign_to_course(self, course):
        # Assigning the professor to a course
        self.courses.append(course)

class Course:
    def __init__(self, course_name, course_code):
        # Initializing attributes for a course
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.professor = None
    
    def add_student(self, student):
        # Adding a student to the course
        self.students.append(student)
    
    def set_professor(self, professor):
        # Setting the professor for the course
        self.professor = professor
    
    def __str__(self):
        # Generating a string representation of the course
        return f"Course Name: {self.course_name}, Course Code: {self.course_code}"

class Department:
    def __init__(self, department_name):
        # Initializing attributes for a department
        self.department_name = department_name
        self.courses = []
        self.professors = []
    
    def add_course(self, course):
        # Adding a course to the department
        self.courses.append(course)
    
    def add_professor(self, professor):
        # Adding a professor to the department
        self.professors.append(professor)
    
    def __str__(self):
        # Generating a string representation of the department
        return f"Department Name: {self.department_name}"

class University:
    def __init__(self, name):
        # Initializing attributes for a university
        self.name = name
        self.departments = []
        self.students = []
    
    def add_department(self, department):
        # Adding a department to the university
        self.departments.append(department)
    
    def add_student(self, student):
        # Adding a student to the university
        self.students.append(student)
    
    def __str__(self):
        # Generating a string representation of the university
        department_list = "\n".join([department.__str__() for department in self.departments])
        return f"University Name: {self.name}\nDepartments:\n{department_list}"

# Creating instances and testing
math_course = Course("Mathematics", "MATH101")
physics_course = Course("Physics", "PHY101")
professor_smith = Professor("John Smith", 45, "P001", "Mathematics")
professor_doe = Professor("Jane Doe", 50, "P002", "Physics")
math_department = Department("Math Department")
physics_department = Department("Physics Department")
my_university = University("My University")

# Adding courses and professors to departments
math_department.add_course(math_course)
math_department.add_professor(professor_smith)
physics_department.add_course(physics_course)
physics_department.add_professor(professor_doe)

# Adding departments to the university
my_university.add_department(math_department)
my_university.add_department(physics_department)

# Enrolling students in courses
student1 = Student("Alice", 20, "S001")
student1.enroll(math_course)
student1.enroll(physics_course)

# Displaying the university
print("University Details:")
print(my_university)
