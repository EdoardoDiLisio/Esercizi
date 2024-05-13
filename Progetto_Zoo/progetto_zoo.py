class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

class Animal:
    def __init__(self, name, species, age, height, width, health, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        intial_health = round(100 * (1 / age), 3)
        self.width = width
        self.health = health
        self.preferred_habitat = preferred_habitat
        self.fence = None
    
    def __str__(self):
        return f'Animal(name={self.name}, species={self.species}, age={self.age}, height={self.height}, width={self.width}, preferred_habitat={self.preferred_habitat}, health={self.health})'

class Fence:
    def __init__()