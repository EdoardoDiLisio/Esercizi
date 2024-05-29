nome_variabile: int = 10     #-----------intero
nome_variabile: float = 10.0 #-----------float
nome_variabile: bool = False #-----------booleano
nome_variabile: str = "Ciao" #-----------stringa

nome_variabile: float = 10.0
nome_variabile = nome_variabile + 5.5
nome_variabile += 5.5 #----------------- dal punto di vista semantico è la stessa cosa della riga superiore

variabile_float: float = 0.0
variabile_float = 5.0 + 10.0

variabile_int: int = 0
variabile_int = 10 + 5

print(nome_variabile)

lunghezza_lista: int = 7

import math #----------------------------libreria che contiene funzio cos sin ecc ecc
punto_di_mezzo: float = 3.2
print(math.ceil(punto_di_mezzo))

var_1: bool = True
var_2: bool = False

print(var_1 and var_2)
print(var_1 or var_2)
print(not var_1 )

x: int = 1000

lista: list = [1, 2, 5, 3]
i: int = 0

a: bool = True
b: bool = False

            #  0  1  2  3
lista: list = [1, 2, 3, 5]

for numero in lista:
   
    print(f"x^2: {numero**2}")

if a and b:
    
    print(f"sono nel primo if")

elif a or b:
    
    print(f"sono nel primo elif")

else:
    
    print(f"sono nell'else")






for x in range(10):    
    print(f"x: {x}")