import random

def display_positions(Turtle_pos, Rabbit_pos):
    positions = ['-'] * 70
    positions[Turtle_pos] = 'T'
    positions[Rabbit_pos] = 'H'
    if Turtle_pos == Rabbit_pos:
        positions[Turtle_pos] = 'OUCH!!!'
    print(''.join(positions))

def Turtle_move():
    r = random.randint(1,11)
    if 1 <= r <= 5:
        return 3
    elif 6 <= r <= 7:
        return -3
    else :
        return 1

def Rabbit_move():
    r = random.randint(1, 11)
    if 1 <= r <= 2:
        return 0
    elif 3 <= r <= 6:
        return 3
    elif 7 <= r <= 8:
        return -3
    elif 9 <= r <= 11:
        return -2
    else:
        return 1

def Main():
    Turtle_pos = 1
    Rabbit_pos = 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        Turtle_pos += Turtle_move()
        Rabbit_pos += Rabbit_move()
        if Turtle_pos >= 70 or Rabbit_pos >= 70:
            if Turtle_pos > Rabbit_pos:
                print('TORTOISE WINS! || VAY!!!')
            elif Rabbit_pos > Turtle_pos:
                print('HARE WINS || YUCH!!!')
            else:
                print('IT\'S A TIE.')
            break
        if Turtle_pos < 1:
            Turtle_pos = 1
        if Rabbit_pos < 1:
            Rabbit_pos = 1
        display_positions(Turtle_pos, Rabbit_pos)
        

if __name__ == '__main__':
    Main()