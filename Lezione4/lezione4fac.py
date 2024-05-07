'''
1. School Grading System:

     Create a function that takes a student's name and their scores in different subjects as input.
    The function calculates the average score and prints the student's name, average, and a message indicating whether the 
    student passed the exam (average >= 60) or failed.
    Create a for loop to iterate over a list of students and scores, calling the function for each student.

2. Guess the Number Game:

    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.

3. E-commerce Shopping Cart:

    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.

4. Text Analysis:

     Create a function that reads a text file and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.
    Implement error handling to handle missing files or other input issues.


5. Inventory Management System:

     Create a function that defines an item with a code, name, quantity, and price.
     Create a database or dictionary to store the items in inventory.
    Implement functions to add, remove, search, and update items in the inventory.
    Use for loops and conditional statements to manage the various inventory operations.

6. Password Generator:

    Create a function that generates a random password with a specified length and desired character types (lowercase letters,
    uppercase letters, numbers, symbols).
    Allow the user to specify the password length and desired character types.
    Generate and return a random password that meets the user's criteria.

7. Roman Numeral Conversion:

    Create a function that converts a given integer to its Roman numeral representation.
    Handle numbers from 1 to 3999.
    Use a combination of string manipulation and conditional statements to build the Roman numeral.

8. ATM Machine Simulator:

    Create a function that simulates an ATM machine.
    Initialize an account with a starting balance.
    Allow the user to perform transactions such as deposit, withdraw, and check balance.
     Validate transactions against the account balance and available funds.
    Provide appropriate feedback to the user for each transaction.


9. Caesar Cipher Encryption/Decryption

    Create functions for encrypting and decrypting a message using the Caesar cipher.
    Allow the user to specify the shift value (number of positions to shift each letter).
     Handle both encryption and decryption using the same function with appropriate adjustments.
    Encrypt and decrypt the given message using the specified shift value.


10. Anagram Checker:

    Create a function that checks whether two given strings are anagrams of each other.
    Convert both strings to lowercase and remove any non-alphabetic characters.
    Sort the characters of each string and compare the sorted strings for equality.
    Indicate whether the strings are anagrams or not.

11. Word Search Puzzle Solver:

    Create a function that solves a word search puzzle.
    Provide a 2D grid representing the puzzle and a list of words to find.
    Implement a backtracking algorithm to search for the words in the grid, marking visited cells to avoid repetition.
    Output the locations of the found words within the grid.


12. Sieve of Eratosthenes Prime Number Generator:

    Create a function that generates a list of prime numbers up to a specified limit using the Sieve of Eratosthenes algorithm.
    Initialize an array of all numbers up to the limit, marking each number as prime initially.
    Iterate through the array, starting from 2, and mark every multiple of the current number as non-prime.
    The remaining unmarked numbers are the prime numbers within the limit.
    Return the list of prime numbers.


13. Fractal Tree Generator:

    Create a function that generates a fractal tree using recursion.
    Specify the starting trunk length and branching angle.
    Draw the trunk and then recursively call the function to draw two branches at the specified angle, each with a shorter length.
    Repeat the branching process until a desired level of detail is reached.



14. Sudoku Solver:

    Create a function that solves a Sudoku puzzle using backtracking.
    Provide a 9x9 grid representing the puzzle with some numbers filled in and others left blank.
    Implement a backtracking algorithm to check for valid placements in empty cells, ensuring no row, column, or 3x3 subgrid contains duplicates.
    Solve the puzzle by filling in the remaining empty cells with valid numbers.

15. Text Editor with Basic Functionality:

    Create a simple text editor that allows the user to open, edit, and save text files.
    Implement basic functionality such as inserting, deleting, and copying text.
    Provide undo/redo functionality to allow users to reverse actions.
    Save the edited text to a file when the user chooses to save.

'''

#1.

def calculate_average(name, scores):
    average = sum(scores) / len(scores)
    result = "pass" if average >= 60 else "fail"
    print(f"{name}'s average score is {average}. Result: {result}")

students = [("Alice", [80, 70, 90]), ("Bob", [50, 60, 55]), ("Charlie", [40, 30, 35])]

for student in students:
    calculate_average(student[0], student[1])


#2.

import random

def guess_the_number(start, end, max_attempts):
    number = random.randint(start, end)
    attempts = 0

    while attempts < max_attempts:
        guess = int(input(f"Guess the number between {start} and {end}: "))
        attempts += 1
        
        if guess == number:
            print(f"Congratulations! You guessed the number {number} correctly in {attempts} attempts.")
            return
        elif guess < number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    
    print(f"Sorry, you've reached the maximum number of attempts. The correct number was {number}.")

guess_the_number(1, 100, 5)

#3.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def manage_shopping_cart(products):
    total = 0
    for product in products:
        total += product.price * product.quantity
        print(f"{product.name}: ${product.price} x {product.quantity}")

    print(f"Total: ${total}")

products = [Product("Laptop", 1000, 2), Product("Phone", 500, 1), Product("Tablet", 300, 3)]

manage_shopping_cart(products)

#4.

def analyze_text(file_name):
    try:
        with open(file_name, 'r') as file:
            words_count = {}
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    words_count[word] = words_count.get(word, 0) + 1

            sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
            print("Most frequent words:")
            for word, count in sorted_words[:10]:
                print(f"{word}: {count} occurrences")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

analyze_text("sample.txt")

#5.

class Item:
    def __init__(self, code, name, quantity, price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.code] = item

    def remove_item(self, code):
        if code in self.items:
            del self.items[code]

    def search_item(self, code):
        return self.items.get(code, None)

    def update_item(self, code, new_item):
        if code in self.items:
            self.items[code] = new_item

inventory = Inventory()
item1 = Item("001", "Laptop", 10, 1000)
item2 = Item("002", "Phone", 20, 500)
inventory.add_item(item1)
inventory.add_item(item2)
print(inventory.search_item("001").name)


#6.

import random
import string

def generate_password(length, lowercase=True, uppercase=True, numbers=True, symbols=True):
    characters = ""
    if lowercase:
        characters += string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not any([lowercase, uppercase, numbers, symbols]):
        raise ValueError("At least one character type must be enabled.")

    return ''.join(random.choice(characters) for _ in range(length))

password = generate_password(12)
print("Generated password:", password)


#7.

def int_to_roman(num):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    result = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while num >= value:
            result += numeral
            num -= value
    return result

print(int_to_roman(1994))  # Output: "MCMXCIV"


#8.

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

# Usage
atm = ATM(1000)
atm.check_balance()
atm.deposit(500)
atm.withdraw(200)


#9.

def caesar_cipher(text, shift, decrypt=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in text:
        if char.lower() in alphabet:
            shifted_index = (alphabet.index(char.lower()) - shift) if decrypt else (alphabet.index(char.lower()) + shift)
            shifted_index %= 26
            if char.isupper():
                result += alphabet[shifted_index].upper()
            else:
                result += alphabet[shifted_index]
        else:
            result += char
    return result

encrypted_text = caesar_cipher("Hello, World!", 3)
print("Encrypted text:", encrypted_text)
decrypted_text = caesar_cipher(encrypted_text, 3, decrypt=True)
print("Decrypted text:", decrypted_text)


#10.

def is_anagram(str1, str2):
    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')
    return sorted(str1) == sorted(str2)

str1 = "Listen"
str2 = "Silent"
print(f"{str1} and {str2} are anagrams: {is_anagram(str1, str2)}")


#11.

def word_search(grid, words):
    def dfs(i, j, word):
        if not word:
            return True
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[0]:
            return False
        temp, grid[i][j] = grid[i][j], '#'
        found = dfs(i + 1, j, word[1:]) or dfs(i - 1, j, word[1:]) or dfs(i, j + 1, word[1:]) or dfs(i, j - 1, word[1:])
        grid[i][j] = temp
        return found

    results = {}
    for word in words:
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j, word):
                    results[word] = (i, j)
                    found = True
                    break
            if found:
                break
    return results

grid = [
    ['h', 'e', 'l', 'l', 'o'],
    ['w', 'o', 'r', 'l', 'd'],
    ['l', 'o', 'r', 'l', 'd']
]
words = ["hello", "world", "foo", "bar"]
print(word_search(grid, words))


#12.

def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for i in range(num*num, limit + 1, num):
                sieve[i] = False
    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

print(sieve_of_eratosthenes(50))


#13.

import turtle

def draw_branch(branch_length, angle):
    if branch_length > 5:
        turtle.forward(branch_length)
        turtle.right(angle)
        draw_branch(branch_length - 15, angle)
        turtle.left(2 * angle)
        draw_branch(branch_length - 15, angle)
        turtle.right(angle)
        turtle.backward(branch_length)

def draw_tree(trunk_length, angle):
    turtle.left(90)
    turtle.up()
    turtle.backward(trunk_length)
    turtle.down()
    draw_branch(trunk_length, angle)
    turtle.exitonclick()

draw_tree(100, 30)


#14.

def is_valid_move(board, row, col, num):
   
    if num in board[row]:
        return False

    
    if num in [board[i][col] for i in range(9)]:
        return False

    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def print_board(board):
    for row in board:
        print(row)


#15.

class TextEditor:
    def __init__(self):
        self.text = ""

    def open_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.text = file.read()
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def save_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                file.write(self.text)
            print(f"Text saved to '{file_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def insert_text(self, text):
        self.text += text

    def delete_text(self):
        self.text = ""


'''
import random
import string
import turtle

# 1. School Grading System
def calculate_average(name, scores):
    avg = sum(scores) / len(scores)
    print(f"{name}: {'pass' if avg >= 60 else 'fail'}")

students = [("Alice", [80, 70, 90]), ("Bob", [50, 60, 55]), ("Charlie", [40, 30, 35])]
for name, scores in students:
    calculate_average(name, scores)

# 2. Guess the Number Game
def guess_number(start, end, attempts):
    number = random.randint(start, end)
    while attempts > 0:
        guess = int(input(f"Guess between {start}-{end}: "))
        if guess == number:
            print(f"Correct! Number is {number}.")
            return
        print("Too high" if guess > number else "Too low")
        attempts -= 1
    print(f"Out of attempts. Correct number was {number}.")

guess_number(1, 100, 5)

# 3. E-commerce Shopping Cart
class Product:
    def __init__(self, name, price, quantity):
        self.name, self.price, self.quantity = name, price, quantity

def manage_cart(products):
    total = sum(p.price * p.quantity for p in products)
    for p in products: print(f"{p.name}: ${p.price} x {p.quantity}")
    print(f"Total: ${total}")

products = [Product("Laptop", 1000, 2), Product("Phone", 500, 1), Product("Tablet", 300, 3)]
manage_cart(products)

# 4. Text Analysis
def analyze_text(file_name):
    try:
        words = open(file_name).read().lower().split()
        wc = {w: words.count(w) for w in set(words)}
        for w, c in sorted(wc.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"{w}: {c}")
    except FileNotFoundError: print(f"File '{file_name}' not found.")
    except Exception as e: print(f"An error occurred: {e}")

analyze_text("sample.txt")

# 5. Inventory Management System
class Item:
    def __init__(self, code, name, quantity, price):
        self.code, self.name, self.quantity, self.price = code, name, quantity, price

class Inventory:
    def __init__(self): self.items = {}

    def add_item(self, item): self.items[item.code] = item
    def remove_item(self, code): del self.items[code]
    def search_item(self, code): return self.items.get(code, None)
    def update_item(self, code, new_item): self.items[code] = new_item

inventory = Inventory()
inventory.add_item(Item("001", "Laptop", 10, 1000))
print(inventory.search_item("001").name)

# 6. Password Generator
def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

password = generate_password(12)
print("Generated password:", password)

# 7. Roman Numeral Conversion
def int_to_roman(num):
    roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ""
    for value, numeral in roman.items():
        while num >= value: res, num = res + numeral, num - value
    return res

print(int_to_roman(1994))

# 8. ATM Machine Simulator
class ATM:
    def __init__(self, balance): self.balance = balance
    def deposit(self, amount): self.balance += amount if amount > 0 else 0
    def withdraw(self, amount): self.balance -= amount if 0 < amount <= self.balance else 0
    def check_balance(self): print(f"Current balance: ${self.balance}")

# 9. Caesar Cipher Encryption/Decryption
def caesar_cipher(text, shift, decrypt=False):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alpha[shift % 26:] + alpha[:shift % 26]
    if decrypt: shifted = shifted[::-1]
    return ''.join(shifted[alpha.find(c)] if c in alpha else c for c in text.lower())

enc_text = caesar_cipher("Hello, World!", 3)
print("Encrypted:", enc_text)
print("Decrypted:", caesar_cipher(enc_text, 3, decrypt=True))

# 10. Anagram Checker
def is_anagram(s1, s2): return sorted(s1.lower().replace(' ', '')) == sorted(s2.lower().replace(' ', ''))

print(is_anagram("Listen", "Silent"))

# 11. Word Search Puzzle Solver
def word_search(grid, words):
    def dfs(i, j, word):
        if not word: return True
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != word[0]: return False
        temp, grid[i][j] = grid[i][j], '#'
        found = dfs(i+1,j,word[1:]) or dfs(i-1,j,word[1:]) or dfs(i,j+1,word[1:]) or dfs(i,j-1,word[1:])
        grid[i][j] = temp
        return found

    res = {}
    for word in words:
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(i, j, word):
                    res[word] = (i, j)
                    found = True
                    break
            if found: break
    return res

grid = [['h','e','l','l','o'], ['w','o','r','l','d'], ['l','o','r','l','d']]
print(word_search(grid, ["hello", "world"]))

# 12. Sieve of Eratosthenes Prime Number Generator
def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    primes = []
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]: primes.extend(num for num in range(num*num, limit + 1, num))
    return [num for num in range(2, limit + 1) if sieve[num]]

print(sieve_of_eratosthenes(50))

# 13. Fractal Tree Generator
def draw_tree(trunk_len, angle):
    def draw_branch(branch_len):
        if branch_len > 5:
            turtle.forward(branch_len)
            turtle.right(angle)
            draw_branch(branch_len - 15)
            turtle.left(2 * angle)
            draw_branch(branch_len - 15)
            turtle.right(angle)
            turtle.backward(branch_len)

    turtle.left(90)
    turtle.up()
    turtle.backward(trunk_len)
    turtle.down()
    draw_branch(trunk_len)
    turtle.exitonclick()

draw_tree(100, 30)

# 14. Sudoku Solver
def solve_sudoku(board):
    def is_valid_move(row, col, num):
        return all(num != board[row][i] for i in range(9)) and all(num != board[i][col] for i in range(9)) \
               and all(num != board[i//3*3 + row//3][j//3*3 + col//3] for i in range(3) for j in range(3))

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_move(i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board): return True
                        board[i][j] = 0
                return False
    return True

board = [[5,3,0,0,7,0,0,0,0], [6,0,0,1,9,5,0,0,0], [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3], [4,0,0,8,0,3,0,0,1], [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0], [0,0,0,4,1,9,0,0,5], [0,0,0,0,8,0,0,7,9]]

if solve_sudoku(board):
    print("Solved Sudoku:")
    for row in board: print(row)
else: print("No solution exists.")

# 15. Text Editor with Basic Functionality
class TextEditor:
    def __init__(self):
        self.text = ""

    def open_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.text = file.read()
                print(f"File '{file_name}' opened successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except Exception as e:
            print(f"An error occurred while opening the file: {e}")

    def edit_text(self, new_text):
        self.text = new_text

    def save_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                file.write(self.text)
                print(f"Text saved to file '{file_name}' successfully.")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")

'''