# 4.1 Pizzas

pizzas = ['Margherita', 'Patate', 'Funghi']
for pizza in pizzas:
	print("I like " + pizza)
print("I really love pizza!")
print('\n\n')
# 4.2 Animals

animals = ['gorilla', 'zebra', 'giraffe']

for animal in animals:
	print('You can find a ' + animal + " in the zoo!")
print('All of these animals belong in the zoo.')
print('\n\n')

# 4.3 Counting to twenty

for value in range(1,21):
	print(value)
print('\n\n')

# 4.4 One Million

one_million = list(range(1,1000001))
print('\n\n')

# 4.5 Summing a million

print(min(one_million))
print(max(one_million))
print(sum(one_million))
print('\n\n')

# 4.6 Odd Numbers

odds = list(range(1,21,2))
for value in odds:
	print(value)
print('\n\n')

#4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

three = list(range(3,31,3))
for value in three:
    print(value)
print('\n\n')

# 4.8 Cubes

cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
	print(cube)
print('\n\n')
# 4.9 Cube Comprehension

cubes_list = [value**3 for value in range(1,11)]
print(cubes_list)
print('\n\n')
## 4.10 Slices

print(cubes[:3])

print(cubes[2:5])

print(cubes[-3:])
print('\n\n')
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
print('\n\n')
