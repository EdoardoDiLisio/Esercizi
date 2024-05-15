'''
Dato un numero intero, restituisce una stringa che ne rappresenta la rappresentazione esadecimale. 
Per gli interi negativi viene utilizzato il metodo del complemento a due.

Tutte le lettere nella stringa di risposta dovrebbero essere caratteri minuscoli e non dovrebbero esserci z
eri iniziali nella risposta tranne lo zero stesso.

Nota: non è consentito utilizzare alcun metodo di libreria integrato per risolvere direttamente questo problema.
'''
def to_hex(num: int) -> str:
    if num == 0:
        return "0"
    
    hex_chars = "0123456789abcdef"
    result = ""
    
    if num < 0:
        num += 2 ** 32
    
    while num > 0:
        digit = num % 16
        result = hex_chars[digit] + result
        num //= 16
    
    return result