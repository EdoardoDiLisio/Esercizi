# Scrivi una funzione prime_factors(n: int) -> list[int] che trova i fattori primi di un numero n dato in input

def prime_factors(n: int) -> list[int]:
    
    fattori_primi = []

    while n % 2 == 0:
        fattori_primi.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            fattori_primi.append(i)
            n //= i
    if n > 2:
        fattori_primi.append(n)

    return fattori_primi