#  EDOARDO DI LISIO
#  13.06.24

'''
1.
Safe Square Root: Write a function safe_sqrt(number) that calculates the square root of a number using math.sqrt(). 
Handle ValueError if the input is negative by returning an informative message.

2.
Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria (i.e., minimum length 
of 20 characters, at least three uppercase characters, and at least four special characters).  Raise a custom exception 
(e.g., InvalidPasswordError) for invalid passwords.

3.
Context Managers for File Handling: Use the with statement and context managers to open and close a file. Handle potential IOError 
within the with block for clean resource management.

4.
Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date, 
delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a 
given new date. Note that a date is an object for your database; it must be instantiated from a string.

5.
An interactive calculator: It is required to develop an interactive calculator with at least 10 test cases using UnitTest trying to 
(possibly) cover all execution paths! User input is assumed to be a formula that consists of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Split user input using str.split(), and check whether the resulting list is valid:
If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third inputs to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and 
instead raise a FormulaError.
If the second input is not '+' or '-', again raise a FormulaError.
If the input is valid, perform the calculation and print out the result. The user is then prompted to provide new input, and so on, 
until the user enters quit.

6.
Personalized math library: Create a Python library that provides functions for handling fractions, with built-in error handling. 
The library must include functions for the following operations:
Create a fraction from the numerator and denominator.
Collect the numerator and denominator of a fraction.
Simplify a fraction.
Add, subtract, multiply and divide fractions.
Check whether one fraction is equivalent to another. 
All library functions must use the try-except block to handle potential errors, such as null denominators, unsupported 
operations, or division by zero. The library must raise custom exceptions to indicate specific errors to the user.

7.
Custom Exception for Data Structure Integrity: Define a custom exception class DataStructureIntegrityError.  
Define the custom data structure linked list use classes with methods to append, remove and access a given element, and 
write functions that operate on that (i.e., print the list,  reverse the list, and check whether the list is ordered). Raise 
this exception if the data structure's integrity is compromised (e.g., empty list access, index error).
'''
#1.
print("EX.1")
import math

def safe_sqrt(number):
    """
    Calcola la radice quadrata di un numero. Se il numero è negativo,
    restituisce un messaggio informativo.
    """
    try:
        return math.sqrt(number)
    except ValueError:
        return "Non è possibile calcolare la radice quadrata di un numero negativo."

# Test
print(safe_sqrt(9))  # 3.0
print(safe_sqrt(-9))  # Non è possibile calcolare la radice quadrata di un numero negativo.
print("\n\n")

#2.
print("EX.2")
class InvalidPasswordError(Exception):
    """Custom exception for invalid passwords."""
    pass

def validate_password(password):
    """
    Verifica se una password soddisfa i criteri:
    - Lunghezza minima di 20 caratteri
    - Almeno 3 caratteri maiuscoli
    - Almeno 4 caratteri speciali
    """
    if len(password) < 20:
        raise InvalidPasswordError("La password deve essere lunga almeno 20 caratteri.")
    
    uppercase_count = sum(1 for char in password if char.isupper())
    special_count = sum(1 for char in password if not char.isalnum())
    
    if uppercase_count < 3:
        raise InvalidPasswordError("La password deve contenere almeno 3 caratteri maiuscoli.")
    
    if special_count < 4:
        raise InvalidPasswordError("La password deve contenere almeno 4 caratteri speciali.")
    
    return "Password valida."

# Test
try:
    print(validate_password("Password123!@#"))  # La password deve essere lunga almeno 20 caratteri.
except InvalidPasswordError as e:
    print(e)
print("\n\n")

#3.
print("EX.3")
def read_file(filename):
    """
    Legge il contenuto di un file gestendo l'eventuale IOError.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except IOError as e:
        return f"Errore di I/O: {e}"

# Test
print(read_file("esempio.txt"))  # Contenuto del file o Errore di I/O
print("\n\n")

#4.
print("EX.4")
class DateDatabase:
    def __init__(self):
        self.dates = []

    def add_date(self, date):
        self.dates.append(date)
    
    def delete_date(self, date):
        if date in self.dates:
            self.dates.remove(date)
    
    def modify_date(self, old_date, new_date):
        if old_date in self.dates:
            index = self.dates.index(old_date)
            self.dates[index] = new_date
    
    def query_date(self, date):
        return date in self.dates

# Test
db = DateDatabase()
db.add_date("12.06.2023")
print(db.query_date("12.06.2023"))  # True
db.modify_date("12.06.2023", "13.06.2023")
print(db.query_date("13.06.2023"))  # True
db.delete_date("13.06.2023")
print(db.query_date("13.06.2023"))  # False
print("\n\n")

#5.
print("EX.5")
class FormulaError(Exception):
    """Custom exception for errors in the formula."""
    pass

def process_formula(formula):
    """
    Processa una formula matematica e restituisce il risultato.
    Se la formula è errata, solleva un'eccezione FormulaError.
    """
    tokens = formula.split()
    if len(tokens) != 3:
        raise FormulaError("La formula deve contenere esattamente 3 elementi.")
    
    num1, operator, num2 = tokens
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise FormulaError("Il primo e il terzo elemento devono essere numeri.")
    
    if operator not in ['+', '-']:
        raise FormulaError("L'operatore deve essere '+' o '-'.")
    
    if operator == '+':
        return num1 + num2
    else:
        return num1 - num2

def interactive_calculator(formulas):
    """
    Calcolatrice che processa una lista di formule.
    """
    for formula in formulas:
        if formula.lower() == 'quit':
            break
        try:
            result = process_formula(formula)
            print(f"Risultato: {result}")
        except FormulaError as e:
            print(f"Errore: {e}")

# Esempio di utilizzo:
formulas = [
    "3 + 4",
    "10 - 2",
    "10 * 2",  # Errore: operatore non valido
    "a + 2",   # Errore: numero non valido
    "1 +",     # Errore: numero di elementi errato
    "quit"
]
interactive_calculator(formulas)

print("\n\n")

#6.
print("EX.6")
class FractionError(Exception):
    """Custom exception for fraction errors."""
    pass

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise FractionError("Il denominatore non può essere zero.")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()
    
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
    
    def add(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def subtract(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def multiply(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def divide(self, other):
        if other.numerator == 0:
            raise FractionError("Divisione per zero non è permessa.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)
    
    def is_equivalent(self, other):
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

# Test
f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print(f1.add(f2))  # 5/4
print(f1.subtract(f2))  # -1/4
print(f1.multiply(f2))  # 3/8
print(f1.divide(f2))  # 2/3
print(f1.is_equivalent(Fraction(2, 4)))  # True
print("\n\n")

#7.
print("EX.7")
class DataStructureIntegrityError(Exception):
    """Custom exception for data structure integrity errors."""
    pass

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
    
    def remove(self, value):
        if not self.head:
            raise DataStructureIntegrityError("Lista vuota.")
        
        if self.head.value == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next is None:
            raise DataStructureIntegrityError("Elemento non trovato.")
        
        current.next = current.next.next
    
    def access(self, index):
        if not self.head:
            raise DataStructureIntegrityError("Lista vuota.")
        
        current = self.head
        for i in range(index):
            if not current.next:
                raise DataStructureIntegrityError("Indice fuori dai limiti.")
            current = current.next
        
        return current.value
    
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def is_ordered(self):
        if not self.head or not self.head.next:
            return True
        
        current = self.head
        while current.next:
            if current.value > current.next.value:
                return False
            current = current.next
        return True

# Test
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # 1 -> 2 -> 3 -> None
print(ll.access(1))  # 2
ll.remove(2)
ll.print_list()  # 1 -> 3 -> None
ll.reverse()
ll.print_list()  # 3 -> 1 -> None
print(ll.is_ordered())  # False
ll.reverse()
print(ll.is_ordered())  # True
