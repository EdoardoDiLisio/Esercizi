'''
Scrivi una funzione che riceve un numero e stampa un conto alla rovescia da quel numero a zero.
'''

def countdown(n: int) -> int:
    if n < 0:
        print("Inserire un numero positivo.")
        return
    
    for i in range(n, -1, -1):
        print(i)