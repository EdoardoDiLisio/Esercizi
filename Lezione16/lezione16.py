# EDOARDO DI LISIO
# 05.06.24

#########  PARTE 1
'''
In questo progetto, dovrai scrivere il codice per un sistema di gestione e creazione dei corsi ITS.
Il sistema gestisce aule ed edifici (Parte 1), persone -studenti e docenti- in gruppi di studio (parte 2), e corsi (parte 3).
### Classe Room:
La classe Room rappresenta un'aula. Ogni aula ha un ID (id), un piano (floor), un numero di posti (seats) e un'area (area). 
L'area è calcolata come il doppio dei posti.
- Metodi:
    - get_id(): Restituisce l'ID dell'aula.
    - get_floor(): Restituisce il piano dell'aula.
    - get_seats(): Restituisce il numero di posti dell'aula.
    - get_area(): Restituisce l'area dell'aula.
### Classe Building:
La classe Building rappresenta un edificio. Ogni edificio ha un nome (name), un indirizzo (address), un intervallo di piani (floors), 
e una lista di aule (rooms).
- Metodi:
    - get_floors(): Restituisce l'intervallo di piani dell'edificio.
    - get_rooms(): Restituisce la lista delle aule nell'edificio.
    - add_room(room): Aggiunge un'aula all'edificio, solo se il piano dell'aula è compreso nell'intervallo di piani dell'edificio.
    - area(): Restituisce l'area totale dell'edificio sommando le aree di tutte le aule.
'''

class Room:
    def __init__(self, id, floor, seats):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self):
        return self.id

    def get_floor(self):
        return self.floor

    def get_seats(self):
        return self.seats

    def get_area(self):
        return self.area

class Building:
    def __init__(self, name, address, floors):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room):
        if room.get_floor() in range(self.floors[0], self.floors[1] + 1):
            if room.get_id() not in [r.get_id() for r in self.rooms]:
                self.rooms.append(room)
                return True
            else:
                
                return False
        else:
            return False

    def area(self):
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area

#########  TEST
'''
# Creazione di stanze
room1 = Room(id="Room1", floor=1, seats=15)
room2 = Room(id="Room2", floor=5, seats=20)
room3 = Room(id="Room3", floor=11, seats=10)  # Questo piano è fuori dal range

# Test classe Room
print("Test classe Room:")
print(f"ID: {room1.get_id()}, Atteso: Room1")
print(f"Piano: {room1.get_floor()}, Atteso: 1")
print(f"Posti: {room1.get_seats()}, Atteso: 15")
print(f"Area: {room1.get_area()}, Atteso: 30.0")

# Creazione di un edificio
building = Building(name="Test Building", address="123 Test St", floors=(1, 10))

# Test di inizializzazione Building
print("\nTest di inizializzazione Building:")
print(f"Nome: {building.name}, Atteso: Test Building")
print(f"Indirizzo: {building.address}, Atteso: 123 Test St")
print(f"Piani: {building.floors}, Atteso: (1, 10)")
print(f"Stanze iniziali: {building.get_rooms()}, Atteso: []")

# Test aggiunta stanza valida
building.add_room(room1)
print("\nDopo aggiunta Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza su piano non valido
building.add_room(room3)
print("\nDopo tentativo di aggiunta Room3 (piano non valido):")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test aggiunta stanza duplicata
building.add_room(room1)
print("\nDopo tentativo di aggiunta duplicato Room1:")
print(f"Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: [Room1]")

# Test calcolo area
building.add_room(room2)
print("\nDopo aggiunta Room2:")
print(f"Area totale: {building.area()}, Atteso: 70.0")

# Test rappresentazione in stringa Building
print("\nRappresentazione in stringa dell'edificio:")
print(f"Nome Edificio: {building.name}")
print(f"Indirizzo Edificio: {building.address}")
print(f"Piani Edificio: {building.get_floors()}")
print("Stanze nell'edificio:")
for room in building.get_rooms():
    print(f"ID Stanza: {room.get_id()}, Piano: {room.get_floor()}, Posti: {room.get_seats()}, Area: {room.get_area()}")
print(f"Area totale dell'edificio: {building.area()}m2")

# Verifica valori attesi
atteso_stanze = ["Room1", "Room2"]
atteso_area = 70.0
print(f"\nVerifica finale: Stanze: {[room.get_id() for room in building.get_rooms()]}, Atteso: {atteso_stanze}")
print(f"Verifica finale: Area totale: {building.area()}, Atteso: {atteso_area}")
print("\n\n\n")
'''
#########  PARTE 2
    
'''
    ### Classi Person, Student e Lecturer:
La classe Person rappresenta una persona con un codice fiscale (cf), un nome (name), un cognome (surname), un'età (age).
Le classi Student e Lecturer ereditano da Person.
Uno studente è associato ad un gruppo di studio (group). Quindi, la classe Student ha il seguente metodo:
    - set_group(group): Associa un gruppo di studio allo studente
### Classe Group:
La classe Group rappresenta un gruppo di studio. Ogni gruppo ha un nome (name), un limite di studenti (limit), una lista di studenti 
(students) e una lista di docenti (lecturers).
- Metodi:
    - get_name(): Restituisce il nome del gruppo
    - get_limit(): Restituisce il limite di studenti nel gruppo
    - get_students(): Resituisce la lista di studenti nel gruppo
    - get_limit_lecturers(): Restituisce il limite di docenti nel gruppo. E' consentito 1 docente ogni 10 studenti. Il gruppo può avere 
      almeno 1 docente, anche se ci sono meno di 10 studenti.
    - add_student(student): Aggiunge uno studente al gruppo, solo se il limite per gli studenti non è stato raggiunto.
    - add_lecturer(lecturer): Aggiunge un docente al gruppo, solo se il limite per i docenti non è stato raggiunto.
    '''
    
class Person:
    def __init__(self, cf, name, surname, age):
        self.cf = cf
        self.name = name
        self.surname = surname
        self.age = age


class Student(Person):
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)
        self.group = None

    def set_group(self, group):
        self.group = group


class Lecturer(Person):
    pass


class Group:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.students = []
        self.lecturers = []

    def get_name(self):
        return self.name

    def get_limit(self):
        return self.limit

    def get_students(self):
        return self.students

    def get_limit_lecturers(self):
        min_lecturers = 1
        max_students_per_lecturer = 10
        num_students = len(self.students)
        num_lecturers = max(min_lecturers, num_students // max_students_per_lecturer)
        return num_lecturers

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)
            return True
        else:
            print("Errore: Limite di studenti nel gruppo raggiunto.")
            return False

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)
            return True
        else:
            print("Errore: Limite di docenti nel gruppo raggiunto.")
            return False

#########  TEST
'''
# Creazione delle persone
person1 = Person(cf="CF123", name="John", surname="Doe", age=30)
student1 = Student(cf="CF456", name="Jane", surname="Smith", age=20)
lecturer1 = Lecturer(cf="CF789", name="Dr. Emily", surname="Brown", age=45)

# Test della classe Person
print("Test della classe Person:")
print(f"CF: {person1.cf}, Atteso: CF123")
print(f"Nome: {person1.name}, Atteso: John")
print(f"Cognome: {person1.surname}, Atteso: Doe")
print(f"Età: {person1.age}, Atteso: 30")

# Test della classe Student
print("\nTest della classe Student:")
print(f"CF: {student1.cf}, Atteso: CF456")
print(f"Nome: {student1.name}, Atteso: Jane")
print(f"Cognome: {student1.surname}, Atteso: Smith")
print(f"Età: {student1.age}, Atteso: 20")
print(f"Gruppo iniziale: {student1.group}, Atteso: None")

# Test metodo set_group della classe Student
group1 = Group(name="Group A", limit=10)
student1.set_group(group1)
print("\nDopo set_group di student1:")
print(f"Gruppo di student1: {student1.group.get_name()}, Atteso: Group A")

# Test della classe Lecturer
print("\nTest della classe Lecturer:")
print(f"CF: {lecturer1.cf}, Atteso: CF789")
print(f"Nome: {lecturer1.name}, Atteso: Dr. Emily")
print(f"Cognome: {lecturer1.surname}, Atteso: Brown")
print(f"Età: {lecturer1.age}, Atteso: 45")

# Creazione di un gruppo e aggiunta di studenti e docenti
group2 = Group(name="Group B", limit=2)
group2.add_student(student1)
group2.add_lecturer(lecturer1)

print("\nDopo aggiunta di student1 e lecturer1 a group2:")
print(f"Studenti in group2: {[student.cf for student in group2.get_students()]}, Atteso: [CF456]")
print(f"Docenti in group2: {[lecturer.cf for lecturer in group2.lecturers]}, Atteso: [CF789]")
print("\n\n\n")
'''

#########  PARTE 3 FINALE (PARTE 1 + 2 + AGGIUNTA ULTIMA CLASSE)

'''
Classe Course:
La classe Course rappresenta un corso accademico. Ogni corso ha un nome (name) e una lista di gruppi (groups).
- Metodi:
    - register(student): Registra uno studente nel primo gruppo disponibile che non ha ancora raggiunto il limite di studenti.
    - get_groups(): Restituisce la lista dei gruppi nel corso.
    - add_group(group): Aggiunge un gruppo al corso.

'''

class Course:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def register(self, student):
        for group in self.groups:
            if len(group.get_students()) < group.get_limit() and student not in group.get_students():
                group.add_student(student)
                return
        print("Errore: Nessun gruppo disponibile o tutti i gruppi hanno raggiunto il limite di studenti.")

    def get_groups(self):
        return self.groups

    def add_group(self, group):
        self.groups.append(group)

#########  TEST
'''
# Creazione degli edifici
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=(-2, 3))
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=(0, 4))

# Aggiunta delle stanze all'edificio smi
smi.add_room(Room(id="123", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
smi.add_room(Room(id="111", floor=-1, seats=32))

# Aggiunta delle stanze all'edificio smi
armellini.add_room(Room(id="567", floor=3, seats=22))
armellini.add_room(Room(id="888", floor=0, seats=32))
armellini.add_room(Room(id="999", floor=6, seats=22))  # Questa stanza non viene aggiunta perché è fuori dal range dei piani
armellini.add_room(Room(id="999", floor=2, seats=22))

# Output dei risultati
print("### SMI ###")
print(f"Stanze nell'edificio SMI: {[room.get_id() for room in smi.get_rooms()]}")
print(f"Area totale dell'edificio SMI: {smi.area()} m²")
print("### ARMELLINI ###")
print(f"Stanze nell'edificio ITIS: {[room.get_id() for room in armellini.get_rooms()]}")
print(f"Area totale dell'edificio ITIS: {armellini.area()} m²")


# Creazione dei gruppi
fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="Cloud", limit=10)
cyber = Group(name="Cyber", limit=10)

# Creazione di un corso e aggiunta dei gruppi al corso
course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)

# Registrazione degli studenti al corso
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="9101", name="Luca", surname="Bianchi", age=25))
course.register(Student(cf="2345", name="Marco", surname="Rossi", age=32))
course.register(Student(cf="6789", name="Paolo", surname="Verdi", age=38))
course.register(Student(cf="1011", name="Giulia", surname="Neri", age=21))
course.register(Student(cf="3456", name="Anna", surname="Gialli", age=27))
course.register(Student(cf="7890", name="Maria", surname="Blu", age=35))
course.register(Student(cf="1112", name="Sara", surname="Viola", age=23))
course.register(Student(cf="4567", name="Giovanni", surname="Arancione", age=31))
course.register(Student(cf="8901", name="Andrea", surname="Rosa", age=24))
course.register(Student(cf="1123", name="Matteo", surname="Marrone", age=30))
course.register(Student(cf="5678", name="Toni", surname="Mancini", age=46))

print("### COURSE DETAILS ###")
print(f"Studenti nel gruppo Fullstack: {[student.cf for student in fullstack.get_students()]}")
print(f"Studenti nel gruppo Cloud: {[student.cf for student in cloud.get_students()]}")
print(f"Studenti nel gruppo Cyber: {[student.cf for student in cyber.get_students()]}")
'''

# CODICE COMMENTATO

'''
class Room:
    # Inizializza un oggetto di tipo Room con gli attributi id, floor, seats
    def __init__(self, id, floor, seats):
        self.id = id  # Imposta l'ID dell'aula
        self.floor = floor  # Imposta il piano dell'aula
        self.seats = seats  # Imposta il numero di posti dell'aula
        self.area = seats * 2  # Calcola e imposta l'area dell'aula

    def get_id(self):
        return self.id  # Restituisce l'ID dell'aula

    def get_floor(self):
        return self.floor  # Restituisce il piano dell'aula

    def get_seats(self):
        return self.seats  # Restituisce il numero di posti dell'aula

    def get_area(self):
        return self.area  # Restituisce l'area dell'aula

class Building:
    # Inizializza un oggetto di tipo Building con gli attributi name, address, floors
    def __init__(self, name, address, floors):
        self.name = name  # Imposta il nome dell'edificio
        self.address = address  # Imposta l'indirizzo dell'edificio
        self.floors = floors  # Imposta l'intervallo di piani dell'edificio
        self.rooms = []  # Inizializza una lista vuota di stanze all'interno dell'edificio

    def get_floors(self):
        return self.floors  # Restituisce l'intervallo di piani dell'edificio

    def get_rooms(self):
        return self.rooms  # Restituisce la lista delle stanze presenti nell'edificio

    def add_room(self, room):
        # Controlla se il piano dell'aula è compreso nell'intervallo di piani dell'edificio
        if room.get_floor() in range(self.floors[0], self.floors[1] + 1):
            # Controlla se l'ID dell'aula è unico all'interno dell'edificio
            if room.get_id() not in [r.get_id() for r in self.rooms]:
                self.rooms.append(room)  # Aggiunge l'aula all'edificio
                return True
            else:
                return False  # Restituisce False se l'aula è duplicata
        else:
            return False  # Restituisce False se il piano dell'aula non è valido

    def area(self):
        # Calcola e restituisce l'area totale dell'edificio sommando le aree di tutte le stanze
        total_area = sum(room.get_area() for room in self.rooms)
        return total_area

class Person:
    # Inizializza un oggetto di tipo Person con gli attributi cf, name, surname, age
    def __init__(self, cf, name, surname, age):
        self.cf = cf  # Imposta il codice fiscale della persona
        self.name = name  # Imposta il nome della persona
        self.surname = surname  # Imposta il cognome della persona
        self.age = age  # Imposta l'età della persona

class Student(Person):
    # Inizializza un oggetto di tipo Student ereditando gli attributi di Person e aggiungendo l'attributo group
    def __init__(self, cf, name, surname, age):
        super().__init__(cf, name, surname, age)  # Chiama il costruttore della classe madre
        self.group = None  # Inizializza l'attributo group come None

    def set_group(self, group):
        self.group = group  # Imposta il gruppo dello studente

class Lecturer(Person):
    pass  # La classe Lecturer eredita gli attributi di Person senza aggiungere nuovi metodi o attributi

class Group:
    # Inizializza un oggetto di tipo Group con gli attributi name, limit
    def __init__(self, name, limit):
        self.name = name  # Imposta il nome del gruppo
        self.limit = limit  # Imposta il limite di studenti del gruppo
        self.students = []  # Inizializza una lista vuota di studenti nel gruppo
        self.lecturers = []  # Inizializza una lista vuota di docenti nel gruppo

    def get_name(self):
        return self.name  # Restituisce il nome del gruppo

    def get_limit(self):
        return self.limit  # Restituisce il limite di studenti del gruppo

    def get_students(self):
        return self.students  # Restituisce la lista degli studenti nel gruppo

    def get_limit_lecturers(self):
        # Calcola il numero minimo di docenti richiesti per il gruppo
        min_lecturers = 1
        max_students_per_lecturer = 10
        num_students = len(self.students)
        num_lecturers = max(min_lecturers, num_students // max_students_per_lecturer)
        return num_lecturers  # Restituisce il numero minimo di docenti richiesti per il gruppo

    def add_student(self, student):
        if len(self.students) < self.limit:
            self.students.append(student)  # Aggiunge lo studente al gruppo se il limite non è stato raggiunto
            return True
        else:
            return False  # Restituisce False se il limite di studenti è stato raggiunto

    def add_lecturer(self, lecturer):
        if len(self.lecturers) < self.get_limit_lecturers():
            self.lecturers.append(lecturer)  # Aggiunge il docente al gruppo se il limite non è stato raggiunto
            return True
        else:
            return False  # Restituisce False se il limite di docenti è stato raggiunto

class Course:
    # Inizializza un oggetto di tipo Course con l'attributo name
    def __init__(self, name):
        self.name = name  # Imposta il nome del corso
        self.groups = []  # Inizializza una lista vuota di gruppi nel corso

    def register(self, student):
        # Itera attraverso tutti i gruppi nel corso
        for group in self.groups:
            # Controlla se il gruppo ha ancora posti disponibili e se lo studente non è già nel gruppo
            if len(group.get_students()) < group.get_limit() and student not in group.get_students():
                group.add_student(student)  # Registra lo studente nel gruppo
                return  # Esce dalla funzione dopo aver registrato lo studente
        print("Errore: Nessun gruppo disponibile o tutti i gruppi hanno raggiunto il limite di studenti.")
'''