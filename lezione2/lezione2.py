#Edoardo Di Lisio
#17/04/24

print("hello world!")

#  2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person. 
#       Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

name: str = "mario"
message: str = f"Ciao {name}, ti va di imparare un po' di python insieme?"
print(message)

# 2-4. Name Cases: Use a variable to represent a person’s name, 
# and then print that person’s name in lowercase, uppercase, and title case.

nome1: str = "andre"
print(str.lower(nome1))
print(str.upper(nome1))
print(str.title(nome1))

# 2-5/2-6. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks: 
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

author_name : str = 'Albert Einstein'
quote : str = "A person who never made a mistake never tried anything new."
output : str = f"Once {author_name} said: \'{quote}\'"
print(output)

# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). 
# Assign the value 'python_notes.txt' to a variable called filename. 
# Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename : str = "python_notes.txt"
nosuffix : str = filename.removesuffix(".txt")
print(nosuffix)

# 3-1. Names: Store the names of a few of your friends in a list called names. 
# Print each person’s name by accessing each element in the list, one at a time.

names = ["ilaria", "veronica", "alessio"]
print(names[0])
print(names[1])
print(names[2])

# 3-2. Greetings: Start with the list you used in Exercise 3-1, 
# but instead of just printing each person’s name, print a message to them. 
# The text of each message should be the same, but each message should be personalized with the person’s name.

message1 : str = f"hello {names[0]}!!"
message2 : str = f"hello {names[1]}!!"
message3 : str = f"hello {names[2]}!!"
print(message1)
print(message2)
print(message3)

# 3-3. Your Own List: Think of your favorite mode of transportation, 
# such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

brand = ["Ferrari", "Bugatti", "lamborghini", "Audi"]
print(f"I would like to own a {brand[0]}")
print(f"I would like to own a {brand[1]}")
print(f"I would like to own a {brand[2]}")
print(f"I would like to own a {brand[3]}")

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

invites = ["Ilaria", "Alessio", "Veronica", "Stefano"]
print(f"hi {invites[0]}, i would like to inite you for a dinner")
print(f"hi {invites[1]}, i would like to inite you for a dinner")
print(f"hi {invites[2]}, i would like to inite you for a dinner")
print(f"hi {invites[3]}, i would like to inite you for a dinner")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
# stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

print(f"hi{invites}, Stefano can't come")
invites.remove("Stefano")
invites.append("Eleonora")
print(f"hi {invites[0]}, i would like to inite you for a dinner")
print(f"hi {invites[1]}, i would like to inite you for a dinner")
print(f"hi {invites[2]}, i would like to inite you for a dinner")
print(f"hi {invites[3]}, i would like to inite you for a dinner")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# Start with your program from Exercise 3-4 or 3-5.
# Add a print() call to the end of your program, informing people that you found a bigger table.
# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

