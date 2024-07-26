def modifica_valore(n: int) -> int:
    if n % 2 == 0:
        n+=10
    else:
        n-=5
    return n
#TEST
n1 = 8
print(modifica_valore(n1))

n2 = 7
print(modifica_valore(n2))

n3 = 0
print(modifica_valore(n3))

n4 = -4
print(modifica_valore(n4))

n5 = -5
print(modifica_valore(n5))