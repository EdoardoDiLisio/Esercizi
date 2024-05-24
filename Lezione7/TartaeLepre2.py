'''
This module provides several functions to simulate a race between the turtle and the hare
'''

# Gioele Amendola
# 14/05/2024

from random import choices
from random import randint


def turtle_walk_speed(t_token, t_energy, weather: bool = False) -> int:
    '''
    This function returns the walking speed of the turtle based on probability.

    Returns:
        int: [3, 1, -6]
    '''
    walking_speed: list[int] = [3, 1, -6]
    weight: list[float] = [0.5, 0.3, 0.2]
    chosen: int = choices(walking_speed, weight)[0]
    index: int = walking_speed.index(chosen)

    if index == 0:
        t_energy -= 5
    elif index == 1:
        t_energy -= 3
    else:
        t_energy -= 10
    if t_energy < 0:
        t_energy = 10
    else:
        t_token += chosen - 1 if weather else chosen

    return t_token, t_energy

def hare_walk_speed(h_token, h_energy, weather: bool = False) -> int:
    '''
    This function returns the walking speed of the hare based on probability

    Returns:
        int: [0, 9, -12, 1, -2]
    '''
    walking_speed: list[int] = [0, 9, -12, 1, -2]
    weight: float = [0.2, 0.2, 0.1, 0.3, 0.2]
    chosen: int = choices(walking_speed, weight)[0]
    index: int = walking_speed.index(chosen)
    temp: int = h_energy
    if index == 0:
        h_energy += 10
        if h_energy > 100:
            h_energy = 100
    elif index == 1:
        temp -= 15
    elif index == 2:
        temp -= 20
    elif index == 3:
        temp -= 5
    elif index == 4:
        temp -=8
    if temp >= 0:
        h_token += chosen -2 if weather and chosen != 0 else chosen
        h_energy = temp

    return h_token, h_energy

def show_route(route: list[str]) -> None:
    '''
    This function shows the current progression of the turtle and the hare 
    '''
    for char in route:
        print(f"{char}",end="")
    print(end="\n\n")

def start_simulation() -> None:
    '''
    This function starts the simulation
    '''
    route: list[str] = ["_"]*randint(25,100)
    max_len: int = len(route) -1
    i: int = 1
    weather: bool = False
    t_token: int = 0
    t_energy: int = 100
    h_token: int = 0
    h_energy: int = 100
    prev_t: int = 0
    prev_h: int = 0
    print("\nBANG !!!!! AND THEY'RE OFF !!!!!\n")
    while True:
        route[t_token], route[h_token] = "_", "_"
        if (i-1)% 10 == 0:
            weather = choices([True,False],[0.5,0.5])[0]
        prev_t, prev_h = t_token, h_token
        t_token, t_energy = turtle_walk_speed(t_token, t_energy, weather)
        h_token, h_energy = hare_walk_speed(h_token, h_energy, weather)
        if t_token >= max_len and h_token >= max_len:
            route[-1] = "X"
            print(f"Last Round: {i}")
            print("It's raining ☂" if weather else "It's sunny ☀︎")
            show_route(route)
            print("\nIT'S A TIE.")
            break
        elif t_token >= max_len:
            route[h_token if h_token >= 0 else 0] = "H"
            route[-1] = "T"
            print(f"Last Round: {i}")
            show_route(route)
            print("\nTORTOISE WINS! || VAY!!!")
            break
        elif h_token >= max_len:
            route[t_token if t_token >= 0 else 0] = "T"
            route[-1] = "H"
            print(f"Last Round: {i}")
            show_route(route)
            print("\nHARE WINS || YUCH!!!")
            break
        if t_token < 0:
            t_token = 0
        if h_token < 0:
            h_token = 0
        if t_token == h_token:
            route[t_token] = 'X'
        else:
            route[t_token] = 'T'
            route[h_token] = 'H'
        print(f"Round: {i}",end=" ")
        if i%3 == 0:
            print("- It's raining ☂" if weather else "- It's sunny ☀︎")
        else:
            print()
        i += 1
        show_route(route)
        print(f"Tortoise moved: {t_token-prev_t}, Tortoise position: {t_token}, Tortoise energy: {t_energy}")
        print(f"Hare moved: {h_token-prev_h}, Hare position: {h_token}, Hare energy: {h_energy}")
        print("\n")

start_simulation()