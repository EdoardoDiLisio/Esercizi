##############  EDOARDO DI LISIO  ##############

# ESERCIZIO 1

# Write a function to find all numbers divisible by 7, not a multiple of 5, 
# between 2000 and 3200 (both included). The numbers should be stored in a list and returned as output.
'''
def find_numbers():
    result = []
    for num in range(2000, 3201):
        if num % 7 == 0 and num % 5!= 0:
            result.append(num)
    return result

print(find_numbers())
'''
print("\n\n")

#ESERCIZIO 2

# Write a function to calculate the factorial of a number given as input. The number should be returned as output. 
# For example: Input: 8 --- Output: 40320

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
'''
print("\n\n")

#ESERCIZIO 3

# Use the function implemented in Exercise 2 to compute all factorial numbers of a list of numbers. 
# The list is given as input to the function. All factorials should be returned as output. For example:
# Input: [2, 5, 8, 10]
# Output: [2, 120, 40320, 3628800]

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def compute_factorials(numbers):
    return [factorial(num) for num in numbers]

numbers = [7, 14, 17, 21]
print("Factorials of", numbers, "are", compute_factorials(numbers))
'''
print("\n\n")

#ESERCIZIO 4

# Given an integer n as input, write a function to generate a dictionary that contains (i, i*i) as (key, value) 
# pairs such that i is an integer between 1 and n (both included). The function should return the dictionary as output. 
# For example:
# Input: 8
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''
def generate_dict(n):
    return {i: i*i for i in range(1, n+1)}

n = 7
print(generate_dict(n))
'''
print("\n\n")

#ESERCIZIO 5

# Write a function that accepts a string with a comma-separated sequence of words as input and prints the words as a 
# comma-separated sequence after sorting them alphabetically. For example:
# Input: without,hello,bag,world
# Output: bag,hello,without,world

'''
def sort_words(input_str):
    words = input_str.split(',')
    words.sort()
    output_str = ','.join(words)
    print(output_str)

input_str = "without,hello,bag,world"
sort_words(input_str)
'''
print("\n\n")

#ESERCIZIO 6

# Write a function that accepts a list of sentences (string) as input and returns each line as output after capitalising 
# all sentence characters. For example:
# Input: Practice makes perfect
# Output: PRACTICE MAKES PERFECT
'''
words: str = "Practice make perfect"
def maiuscolo():
    output: str = words.upper()
    return output
print(maiuscolo())
'''
print("\n\n")

#ESERCIZIO 7

# Write a function accepting an input string defined with whitespace-separated words and returning it after removing 
# all duplicates and sorting each word alphanumerically. For example:
# Input: hello world and practice makes perfect and hello world again
# Output: again and hello makes perfect practice world

'''
def remove_duplicates(input_str):
    words = input_str.split()
    words = list(set(words))
    words.sort()
    output_str = ' '.join(words)
    print(output_str)

input_str = "hello world and practice makes perfect and hello world again"
remove_duplicates(input_str)
'''