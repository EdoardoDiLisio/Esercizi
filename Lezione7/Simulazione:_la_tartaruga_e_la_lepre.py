import random

def display_positions(turtle_pos, rabbit_pos):
    positions = ['-'] * 70
    positions[turtle_pos] = 'T'
    positions[rabbit_pos] = 'H'
    if turtle_pos == rabbit_pos:
        positions[turtle_pos] = 'OUCH!!!'
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
    turtle_pos = 1
    rabbit_pos = 1
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        turtle_pos += Turtle_move()
        rabbit_pos += Rabbit_move()
        if turtle_pos >= 70 or rabbit_pos >= 70:
            if turtle_pos > rabbit_pos:
                print('TORTOISE WINS! || VAY!!!')
            elif rabbit_pos > turtle_pos:
                print('RABBIT WINS || YUCH!!!')
            else:
                print('IT\'S A TIE.')
            break
        if turtle_pos < 1:
            turtle_pos = 1
        if rabbit_pos < 1:
            rabbit_pos = 1
        display_positions(turtle_pos, rabbit_pos)
        

if __name__ == '__main__':
    Main()

print('\n\n\n\n\n\n\n')
##########################################  CON AGGIUNTA DELLE SFIDE  ##############################################################

import random

def display_positions(turtle_pos, rabbit_pos):
    # Crea una lista per rappresentare la pista con '-' come posizioni vuote
    positions = ['-'] * 70
    # Posiziona la tartaruga (T) e la lepre (H) sulle rispettive posizioni
    positions[turtle_pos] = 'T'
    positions[rabbit_pos] = 'H'
    # Se tartaruga e lepre si trovano sulla stessa posizione, stampa 'OUCH!!!'
    if turtle_pos == rabbit_pos:
        positions[turtle_pos] = 'OUCH!!!'
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

def change_weather(tick):
    # Cambia le condizioni meteorologiche ogni 10 tick
    if tick % 10 == 0:
        return random.choice(["sunny", "rainy"])
    else:
        return "unchanged"

def main():
    # Inizializza le posizioni di tartaruga e lepre
    turtle_pos = 1
    rabbit_pos = 1
    # Inizializza le condizioni meteorologiche come 'sunny' all'inizio
    weather = "sunny"
    # Inizializza il contatore di tick
    tick = 1
    # Stampa il messaggio di partenza della gara
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        # Calcola la nuova posizione della tartaruga e della lepre
        turtle_pos += turtle_move(weather)
        rabbit_pos += rabbit_move(weather)
        
        # Verifica se uno dei due contendenti ha vinto la gara
        if turtle_pos >= 70 or rabbit_pos >= 70:
            if turtle_pos > rabbit_pos:
                print('TORTOISE WINS! || VAY!!!')
            elif rabbit_pos > turtle_pos:
                print('RABBIT WINS || YUCH!!!')
            else:
                print('IT\'S A TIE.')
            break
        
        # Assicura che le posizioni non scendano al di sotto di 1
        if turtle_pos < 1:
            turtle_pos = 1
        if rabbit_pos < 1:
            rabbit_pos = 1
        
        # Mostra le posizioni attuali di tartaruga e lepre
        display_positions(turtle_pos, rabbit_pos)
        
        # Cambia le condizioni meteorologiche ogni 10 tick
        weather = change_weather(tick)
        if weather != "unchanged":
            print(f"The weather changed to: {weather.upper()}")
        
        # Incrementa il contatore di tick
        tick += 1

if __name__ == '__main__':
    main()


print('\n\n\n\n\n\n\n')  
##########################################  CON AGGIUNTA DELLE SFIDE  ##############################################################

import random

def display_positions(turtle_pos, rabbit_pos):
    # Crea una lista per rappresentare la pista con '-' come posizioni vuote
    positions = ['-'] * 70
    # Posiziona la tartaruga (T) e la lepre (H) sulle rispettive posizioni
    positions[turtle_pos] = 'T'
    positions[rabbit_pos] = 'H'
    # Se tartaruga e lepre si trovano sulla stessa posizione, stampa 'OUCH!!!'
    if turtle_pos == rabbit_pos:
        positions[turtle_pos] = 'OUCH!!!'
    # Stampa la pista con le posizioni attuali di tartaruga e lepre
    print(''.join(positions))

def turtle_move(energy, weather):
    # Genera un numero casuale per decidere la mossa della tartaruga
    r = random.randint(1, 10)
    
    # Se il numero casuale è 1 o 2, la tartaruga recupera 10 di energia (fino al massimo di 100)
    if r <= 2:
        energy += 10
        if energy > 100:
            energy = 100
    
    # Assegna una mossa in base al numero casuale generato
    if 3 <= r <= 7:
        move = 3
        energy -= 5
    elif 8 <= r <= 9:
        move = -6
        energy -= 10
    else:
        move = 1
        energy -= 3
    
    # Modifica la mossa in base alle condizioni meteorologiche (pioggia)
    if weather == "rainy":
        move -= 1
    return move, energy

def rabbit_move(energy, weather):
    # Genera un numero casuale per decidere la mossa della lepre
    r = random.randint(1, 10)
    
    # Se il numero casuale è 1 o 2, la lepre recupera 10 di energia (fino al massimo di 100)
    if r <= 2:
        energy += 10
        if energy > 100:
            energy = 100
    
    # Assegna una mossa in base al numero casuale generato
    if r <= 2:
        move = 0
        energy += 10
        if energy > 100:
            energy = 100
    elif 3 <= r <= 5:
        move = 9
    elif r == 6:
        move = -12
    elif 7 <= r <= 8:
        move = 1
    else:
        move = -2
    
    # Modifica la mossa in base alle condizioni meteorologiche (pioggia)
    if weather == "rainy":
        move -= 2
    return move, energy

def change_weather(tick):
    # Cambia le condizioni meteorologiche ogni 10 tick
    if tick % 10 == 0:
        return random.choice(["sunny", "rainy"])
    else:
        return "unchanged"

def main():
    # Inizializza le posizioni di tartaruga e lepre
    turtle_pos = 1
    rabbit_pos = 1
    # Inizializza le condizioni meteorologiche come 'sunny' all'inizio
    weather = "sunny"
    # Inizializza l'energia iniziale per entrambi gli animali a 100
    turtle_energy = 100
    rabbit_energy = 100
    # Inizializza il contatore di tick
    tick = 1
    # Stampa il messaggio di partenza della gara
    print("BANG !!!!! AND THEY'RE OFF !!!!!")
    while True:
        # Calcola la nuova posizione della tartaruga e della lepre
        turtle_move_result, turtle_energy = turtle_move(turtle_energy, weather)
        rabbit_move_result, rabbit_energy = rabbit_move(rabbit_energy, weather)
        turtle_pos += turtle_move_result
        rabbit_pos += rabbit_move_result
        
        # Verifica se uno dei due contendenti ha vinto la gara
        if turtle_pos >= 70 or rabbit_pos >= 70:
            if turtle_pos > rabbit_pos:
                print('TORTOISE WINS! || VAY!!!')
            elif rabbit_pos > turtle_pos:
                print('HARE WINS || YUCH!!!')
            else:
                print('IT\'S A TIE.')
            break
        
        # Assicura che le posizioni non scendano al di sotto di 1
        if turtle_pos < 1:
            turtle_pos = 1
        if rabbit_pos < 1:
            rabbit_pos = 1
        
        # Mostra le posizioni attuali di tartaruga e lepre
        display_positions(turtle_pos, rabbit_pos)
        
        # Cambia le condizioni meteorologiche ogni 10 tick
        weather = change_weather(tick)
        if weather != "unchanged":
            print(f"The weather changed to: {weather.upper()}")
        
        # Incrementa il contatore di tick
        tick += 1

if __name__ == '__main__':
    main()

