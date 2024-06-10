from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

# Creazione di due dottori con specializzazione e parcella
dottore_1 = Dottore("Mario", "Rossi", "Pediatra", 29)
dottore_1.setAge(45)  # Imposta l'età del primo dottore

dottore_2 = Dottore("Luca", "Bianchi", "Ostetrico", 75.0)
dottore_2.setAge(50)  # Imposta l'età del secondo dottore

# Presentazione dei dottori con saluto
dottore_1.doctorGreet()
print("\n")
dottore_2.doctorGreet()
print("\n")

# Creazione di liste di pazienti
paziente_1 = Paziente("Giulia", "Verdi", "P001")
paziente_2 = Paziente("Marco", "Neri", "P002")
paziente_3 = Paziente("Anna", "Gialli", "P003")
lista_pazienti_1 = [paziente_1, paziente_2, paziente_3]  # Lista di pazienti per il primo dottore

paziente_4 = Paziente("Elena", "Blu", "P004")
lista_pazienti_2 = [paziente_4]  # Lista di pazienti per il secondo dottore

# Creazione delle fatture per i due dottori
fattura_1 = Fattura(lista_pazienti_1, dottore_1)
fattura_2 = Fattura(lista_pazienti_2, dottore_2)

# Stampa dei salari dei dottori
print(f"Salario Dottore1: {fattura_1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura_2.getSalary()} euro!")

# Rimozione di un paziente dalla lista del primo dottore e aggiunta di un paziente alla lista del secondo dottore
fattura_1.removePatient("P001")
fattura_2.addPatient(paziente_1)

# Stampa dei salari aggiornati
print(f"Salario Dottore1: {fattura_1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura_2.getSalary()} euro!")

# Calcolo e stampa del guadagno totale dell'ospedale
guadagno_totale = fattura_1.getSalary() + fattura_2.getSalary()
print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")
