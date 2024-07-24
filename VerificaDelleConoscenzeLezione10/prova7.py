'''
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
'''

def countdown(n: int) -> None:
    for i in range(n, -1, -1):
        print(i)

countdown(99)  #metti numero