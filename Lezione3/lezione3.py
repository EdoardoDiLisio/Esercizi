# 4.1 Pizzas

pizzas = ['Margherita', 'Patate', 'Funghi']
for pizza in pizzas:
	print("I like " + pizza)
print("I really love pizza!")
print('\n\n\n\n')
# 4.2 Animals

animals = ['gorilla', 'zebra', 'giraffe']

for animal in animals:
	print('You can find a ' + animal + " in the zoo!")
print('All of these animals belong in the zoo.')
print('\n\n\n\n')

# 4.3 Counting to twenty

for value in range(1,21):
	print(value)
print('\n\n\n\n')

# 4.4 One Million

one_million = list(range(1,1000001))
print('\n\n\n\n')

# 4.5 Summing a million

print(min(one_million))
print(max(one_million))
print(sum(one_million))
print('\n\n\n\n')

# 4.6 Odd Numbers

odds = list(range(1,21,2))
for value in odds:
	print(value)
print('\n\n\n\n')

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

three = list(range(3,31,3))
for value in three:
    print(value)

print('\n\n\n\n')

# 4.8 Cubes

cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
	print(cube)

print('\n\n\n\n')
# 4.9 Cube Comprehension

cubes_list = [value**3 for value in range(1,11)]
print(cubes_list)

print('\n\n\n\n')

## 4.10 Slices

print(cubes[:3])

print(cubes[2:5])

print(cubes[-3:])

print('\n\n\n\n')

# 4.11

friend_pizzas = pizzas[:]
pizzas.append('supreme')
friend_pizzas.append('Diavola')
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
print('\n\n\n\n')

#5-3. Alien Colors 1:

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
print('\n\n')

#FAILING VERSION

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")

print('\n\n\n\n')

#5-4. Alien Colors 2:

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
print('\n') 
alien_color = 'yellow'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
print('\n\n\n\n')

#5-5. Alien Colors 3:

alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")
print('\n\n\n\n')

# 5-6. Stages of life:
'''

age = int(input("How old are you? \n"))

if age <= 2:
    print("You're a baby!")
elif age <= 4:
    print("You're a toddler!")
elif age <= 13:
    print("You're a kid!")
elif age <= 20:
    print("You're a teenager!")
elif age <= 65:
    print("Mr, you're an adult!")
else:
    print("Sir, you're an elder!")

print('\n\n\n\n')
'''
#5-7. Favourite fruit

favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")

print("\n\n\n\n")
#5-8. Hello Admin:

usernames = ["jack", "mat", "dadda", "lalla", "rob", "admin"]
for username in usernames:
	if username == "admin":
		print("Hello admin, would you like to see a status report? :)")
	else:
		print(f"Hello {username}, thank you for loggin in again!")
'''
user_input: str = input("inserisci un nome utente ")
if user_input == "admin":
    print("Hello admin, would you like to see a status report? :)")
else:
    print(f"Hello {user_input}, thank you for loggin in again!")
'''
print("\n\n\n\n")

#5-9. No Users:

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report? :)")
        else:
            print(f"Hello {username}, thank you for loggin in again!")
else:
    print("We need to find some users!")
print("\n\n\n\n")
#5-10: Checking Usernames

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is still available.")
print("\n\n\n\n")

#5-11. Ordinal Numbers:

numbers = list(range(1,8))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
print("\n\n\n\n")