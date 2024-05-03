'''
Date due stringhe note e magazine, restituisci true se note può essere costruita utilizzando le lettere di magazine e false 
in caso contrario. Ogni lettera nella magazine può essere utilizzata solo una volta in note.
'''
def ransom(note: str, magazine: str) -> bool:
    letter_count = {}
    
    # Conta le occorrenze di ogni lettera nella magazine
    for char in magazine:
        letter_count[char] = letter_count.get(char, 0) + 1
    
    # Verifica se le lettere in note possono essere trovate nella magazine
    for char in note:
        if char not in letter_count or letter_count[char] == 0:
            return False
        letter_count[char] -= 1
    
    return True