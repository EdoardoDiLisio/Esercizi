'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti 
e aggrega i voti per studente in un nuovo dizionario.
'''
def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    aggregated_grades = {}
    for student in voti:
        name = student["nome"]
        grade = student["voto"]
        if name not in aggregated_grades:
            aggregated_grades[name] = []
        aggregated_grades[name].append(grade)
    return aggregated_grades