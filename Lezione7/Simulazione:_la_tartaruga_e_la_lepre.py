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

##########################################  CON AGGIUNTA DELLE SFIDE  ##############################################################

import random

def display_positions(Turtle_pos, Rabbit_pos):
    # Crea una lista per rappresentare la pista con '-' come posizioni vuote
    positions = ['-'] * 70
    # Posiziona la tartaruga (T) e la lepre (H) sulle rispettive posizioni
    positions[Turtle_pos] = 'T'
    positions[Rabbit_pos] = 'H'
    # Se tartaruga e lepre si trovano sulla stessa posizione, stampa 'OUCH!!!'
    if Turtle_pos == Rabbit_pos:
        positions[Turtle_pos] = 'OUCH!!!'
    # Stampa la pista con le posizioni attuali di tartaruga e lepre
    print(''.join(positions))

def turtle_move(weather):
    # Genera un numero casuale per decidere la mossa della tartaruga
    r = random.randint(1, 11)
    # Assegna una mossa in base al numero casuale generato
    if 1 <= r <= 5:
        move = 3
    elif 6 <= r <= 7:
        move = -3
    else:
        move = 1
    # Modifica la mossa in base alle condizioni meteorologiche (pioggia)
    if weather == "rainy":
        move -= 1
    return move

def rabbit_move(weather):
    # Genera un numero casuale per decidere la mossa della lepre
    r = random.randint(1, 11)
    # Assegna una mossa in base al numero casuale generato
    if 1 <= r <= 2:
        move = 0
    elif 3 <= r <= 6:
        move = 3
    elif 7 <= r <= 8:
        move = -3
    elif 9 <= r <= 11:
        move = -2
    else:
        move = 1
    # Modifica la mossa in base alle condizioni meteorologiche (pioggia)
    if weather == "rainy":
        move -= 2
    return move

def change_weather():
    # Cambia dinamicamente le condizioni meteorologiche ogni 10 tick
    return random.choice(["sunny", "rainy"])

def main():
    # Inizializza le posizioni di tartaruga e lepre
    Turtle_pos = 1
    Rabbit_pos = 1
    # Inizializza le condizioni meteorologiche come 'sunny' all'inizio
    weather = "sunny"
    # Inizializza il contatore di tick
    tick = 1
    # Stampa il messaggio di partenza della gara
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        # Calcola la nuova posizione della tartaruga e della lepre
        Turtle_pos += turtle_move(weather)
        Rabbit_pos += rabbit_move(weather)
        
        # Verifica se uno dei due contendenti ha vinto la gara
        if Turtle_pos >= 70 or Rabbit_pos >= 70:
            if Turtle_pos > Rabbit_pos:
                print('TORTOISE WINS! || VAY!!!')
            elif Rabbit_pos > Turtle_pos:
                print('HARE WINS || YUCH!!!')
            else:
                print('IT\'S A TIE.')
            break
        
        # Assicura che le posizioni non scendano al di sotto di 1
        if Turtle_pos < 1:
            Turtle_pos = 1
        if Rabbit_pos < 1:
            Rabbit_pos = 1
        
        # Mostra le posizioni attuali di tartaruga e lepre
        display_positions(Turtle_pos, Rabbit_pos)
        
        # Ogni 10 tick, cambia le condizioni meteorologiche
        if tick % 10 == 0:
            weather = change_weather()
            print(f"The weather changed to: {weather.upper()}")
        
        # Incrementa il contatore di tick
        tick += 1

if __name__ == '__main__':
    main()