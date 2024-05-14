'''
This module provides some classes and functions that are needed to manage a virtual zoo

Classes:
    Animal: represents an animal with a name, species, age, height, width, habitat and health
    Fence: represents an enclosure with a list of Animal, area, temperature and habitat
    ZooKeeper: represents a zookeeper with a name, surname and an id
    Zoo: represents a zoo with a list of Fence and a list of ZooKeeper

Functions:
    Fence.is_available: checks if an animal can be put in the fence
    ZooKeeper.add_animal: adds an animal to an enclosure
    ZooKeeper.remove_animal: remove an animal from an enclosure
    ZooKeeper.feed: feed an animal (increases health and size)
    ZooKeeper.clean: returns a float with the time needed to clean a fence
    Zoo.describe_zoo: shows every information inside of the zoo. (Zookeepers, fences and animals)

'''

class Animal:
    '''
    This class represents an animal with a name, species, age, height, width, habitat and health
    '''

    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.health: float = round(100 * (1 / age), 3)

class Fence:
    '''
    This class represents an enclosure with a list of Animal, area, temperature and habitat
    '''

    def __init__(self, area: float, temperature: float, habitat: str, animals: list[Animal] = []) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []
        self.animals = [animal for animal in animals if self.is_available(animal) and animal.preferred_habitat == habitat]

    def is_available(self, add_animal: Animal, feed: bool = False) -> bool:
        '''
        This method checks if the animal can be contained inside the fence.

        Args:
            add_animal(Animal): the animal to add to the fence.
            feed(bool)(optional): if the animal is being fed. Defaults to False.
        
        Returns:
            bool: if there is availabe area in the fence.
        '''
        available = self.area - sum(animal.width*animal.height for animal in self.animals if self.animals)
        if feed:
            return available-(add_animal.width*add_animal.height + (add_animal.width*2/100)*(add_animal.height*2/100)) > 0
        return available-add_animal.width*add_animal.height > 0

class ZooKeeper:
    '''
    This class represents a zookeeper with a name, surname and an id
    '''

    def __init__(self, name: str, surname: str, id: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: str = id
    
    def add_animal(self, animal: Animal, fence: Fence) -> None:
        '''
        This method adds an animal to a specified fence.
        
        Args:
            animal(Animal): the animal to add in the fence.
            fence(Fence): the fence that the animal needs to be added to.
        '''
        if animal.name not in [animal.name for animal in fence.animals]:
            if fence.habitat == animal.preferred_habitat:
                if fence.is_available(animal):
                    fence.animals.append(animal)
                else:
                    raise Exception(f"The animal {animal.name} cannot be contained in the specified fence.")
            else:
                raise Exception(f"The animal {animal.name}'s preferred habitat '{animal.preferred_habitat}' is not the same as the fence's '{fence.habitat}'.")
        else:
            raise Exception(f"The animal {animal.name} is already inside the fence.")

    def remove_animal(self, remove_animal: Animal, fence: Fence) -> None:
        '''
        This method removes an animal from a specified fence.

        Args:
            animal(Animal): the animal to remove from the fence.
            fence(Fence): the fence where the animal is in and need to be removed from.
        '''
        animals: list = fence.animals
        animals_names: list = [animal.name for animal in animals]
        if animals:
            if remove_animal.name in animals_names:
                index: int = animals_names.index(remove_animal.name)
                del animals[index]
            else:
                raise Exception(f"There is no animal by the name of {remove_animal.name} in the fence.")
        else:
            raise Exception("The fence is empty.")
    
    def feed(self, feed_animal: Animal, fence: Fence) -> None:
        '''
        This method feeds an animal.

        Args:
            feed_animal(Animal): animal to feed.
            fence(Fence): fence of the animal.
        '''
        animals: list = fence.animals
        animals_names: list = [animal.name for animal in animals]
        if animals:
            if feed_animal.name in animals_names:
                if fence.is_available(feed_animal, feed=True):
                    feed_animal.width += feed_animal.width*2/100
                    feed_animal.height += feed_animal.height*2/100
                    feed_animal.health += feed_animal.health/100
                else:
                    raise Exception("The animal will get too big if fed.")
            else:
                raise Exception(f"There is no animal by the name of {feed_animal.name} in the fence.")
        else:
            raise Exception("The fence is empty.")
    
    def clean(self, fence: Fence) -> float:
        '''
        This method returns the time that the zookeper needs to be able clean the enclosure

        Args:
            fence(Fence): fence to clean.
        '''
        animals: list = fence.animals
        occupied: float = sum(animal.width*animal.height for animal in animals)
        available: float = fence.area - occupied
        time: float = occupied if available == 0 else available/occupied
        return time

class Zoo:
    '''
    This class represents a zoo with a list of Fence and a list of ZooKeeper
    '''

    def __init__(self, fences: list[Fence], zoo_keepers: list[ZooKeeper]) -> None:
        self.fences: list[Fence] = fences
        self.zoo_keepers: list[ZooKeeper] = zoo_keepers

    def describe_zoo(self) -> None:
        '''This method shows every information about the zookeepers, the fences and the animals'''
        print("\n\nGuardians:")
        for keeper in self.zoo_keepers:
            print(f"\nZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})")
        print("\nFences:")
        for fence in self.fences:
            print(f"\nFence(area={fence.area}, temperature={fence.temperature}, habitat={fence.habitat})", end="\n\n")
            if fence.animals:
                print("with animals:\n")
                for animal in fence.animals:
                    print(f"Animal(name={animal.name}, species={animal.species}, age={animal.age})",end="\n\n")
            print("#"*30)
        print(end="\n\n")

#Example Test:
animal1: Animal = Animal("Harambe", "Western Gorilla", 17, 2.1, 0.5, "Tropical")
animal2: Animal = Animal("Fiona", "Common Hippopotamus", 20, 1.6, 1.2, "Savannah")
animal3: Animal = Animal("Diego", "Aldabra giant tortoise", 90, 0.8, 1.2, "Tropical")
animal4: Animal = Animal("Winter", "Hourglass Dolphin", 28, 0.2, 1.9, "Antarctic")
animal5: Animal = Animal("Pingu", "Emperor penguin", 8, 0.5, 0.18, "Antarctic")

animal_list = [animal1, animal2, animal3]

fence1: Fence = Fence(10000, 24, "Tropical", animal_list)
fence2: Fence = Fence(50000, -10, "Antarctic")

fence_list = [fence1,fence2]

zookeeper1: ZooKeeper = ZooKeeper("Giacomo","Belli","120D58A")
zookeeper2: ZooKeeper = ZooKeeper("Liliana","Fortuna","3982BL4")
zookeeper3: ZooKeeper = ZooKeeper("Priscilla","Perlana","032AA27")

zookeeper_list = [zookeeper1,zookeeper2,zookeeper3]

zoo1: Zoo = Zoo(fence_list, zookeeper_list)

zoo1.describe_zoo()

zookeeper1.add_animal(animal4, fence2)
zookeeper1.add_animal(animal2, fence2)
zookeeper1.remove_animal(animal1, fence1)
zookeeper1.remove_animal(animal5, fence2)
zookeeper1.add_animal(animal5, fence2)

zoo1.describe_zoo()

zookeeper2.feed(animal5, fence1)
zookeeper2.feed(animal3, fence1)

print(f"{zookeeper3.clean(fence2)}")
print(f"{zookeeper3.clean(fence1)}")