##############  EDOARDO DI LISIO  ##############

'''
-Question 1

Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola 
o frase diversa, in genere utilizzando tutte le lettere originali esattamente una volta.
'''
print("Question 1\n")
def anagram(s: str, t: str) -> bool:
    # Converte entrambe le stringhe in minuscolo e poi le ordina
    # Confronta le versioni ordinate delle due stringhe
    # Ritorna True se sono uguali, False altrimenti
    return sorted(s.lower()) == sorted(t.lower())

#test
print(anagram("anagram","nagaram"))
print(anagram("rat", "car"))
print(anagram("silent","listen"))
print(anagram("NeurIPS","UniReps"))
print("\n")
'''
Question 2

'''
print("Question 2\n")
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Inizializza un nodo dell'albero binario con un valore, un figlio sinistro e un figlio destro
        self.val = val
        self.left = left
        self.right = right

def symmetric(tree: list[int]) -> bool:
    # Controlla se la lista è vuota. Un albero vuoto è considerato simmetrico.
    if not tree:
        return True

    def list_to_tree(nodes):
        # Converte una lista in un albero binario
        if not nodes:
            return None

        def helper(index):
            # Funzione ricorsiva per creare l'albero binario
            if index >= len(nodes) or nodes[index] is None:
                return None
            # Crea un nuovo nodo con il valore corrente
            node = TreeNode(nodes[index])
            # Imposta il figlio sinistro e destro usando la ricorsione
            node.left = helper(2 * index + 1)
            node.right = helper(2 * (index + 1))
            return node

        # Inizia la costruzione dell'albero a partire dalla radice (indice 0)
        return helper(0)

    def is_symmetric(root):
        # Verifica se l'albero è simmetrico
        if not root:
            return True

        def is_mirror(left, right):
            # Controlla se due alberi sono specchi l'uno dell'altro
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))

        # Avvia la verifica simmetrica sui figli sinistro e destro della radice
        return is_mirror(root.left, root.right)

    # Converte la lista in un albero binario
    root = list_to_tree(tree)
    # Verifica se l'albero binario è simmetrico
    return is_symmetric(root)

# Test
print(symmetric([1, 2, 2, 3, 4, 4, 3]))  # Output: True
print(symmetric([1, 2, 2, None, 3, None, 3]))  # Output: False
print("\n")

'''
Question 3

Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True se l'albero è simmetrico; False altrimenti.
La lista di interi è formata così:
L'elemento in posizione 0 corrisponde alla radice
Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti, significa che il nodo che 
corrisponde a quell'indice è una foglia.
Potete utilizzare la classe TreeNode per crearvi prima l'albero - anziché usare la lista tree - e poi visitare l'albero sfruttando 
gli oggetti di tipo TreeNode.
'''
print("Question 3\n")

def valid_sudoku(board: list[list[str]]) -> bool:
    # Funzione di supporto per verificare se un'unità (riga, colonna o sottogruppo 3x3) è valida
    def is_valid_unit(unit):
        # Filtra i numeri per rimuovere i punti ('.') che rappresentano celle vuote
        unit = [num for num in unit if num != '.']
        # Controlla se ci sono duplicati confrontando la lunghezza dell'unità con la lunghezza del set dell'unità
        return len(unit) == len(set(unit))

    # Controlla tutte le righe
    for row in board:
        # Se una riga non è valida, ritorna False
        if not is_valid_unit(row):
            return False

    # Controlla tutte le colonne
    for col in range(9):
        # Costruisce una lista degli elementi della colonna corrente
        column = [board[row][col] for row in range(9)]
        # Se una colonna non è valida, ritorna False
        if not is_valid_unit(column):
            return False

    # Controlla tutti i sottogruppi 3x3
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            # Costruisce una lista degli elementi del sottogruppo 3x3 corrente
            box = [
                board[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            # Se un sottogruppo 3x3 non è valido, ritorna False
            if not is_valid_unit(box):
                return False

    # Se tutte le righe, colonne e sottogruppi 3x3 sono validi, ritorna True
    return True

# Test con esempi
board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board1))  # Output: True

board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku(board2))  # Output: False
print("\n")

'''
Question 4

Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato in una sequenza 
separata da spazi di una o più parole del dizionario; False altrimenti.
Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.
'''
print("Question 4\n")

def word_break(s: str, wordDict: list[str]) -> bool:
    # Convertiamo il wordDict in un set per accesso O(1) durante le ricerche
    word_set = set(wordDict)
    
    # Creiamo un array dp della lunghezza di s + 1, inizialmente tutto False
    dp = [False] * (len(s) + 1)
    
    # La stringa vuota è sempre segmentabile
    dp[0] = True
    
    # Iteriamo su tutta la stringa dalla posizione 1 alla fine
    for i in range(1, len(s) + 1):
        # Controlliamo tutte le sottostringhe s[j:i]
        for j in range(i):
            # Se dp[j] è True e la sottostringa s[j:i] è nel set delle parole
            if dp[j] and s[j:i] in word_set:
                # Impostiamo dp[i] a True e usciamo dal loop interno
                dp[i] = True
                break
    
    # Restituiamo l'ultimo elemento di dp, che ci dice se l'intera stringa può essere segmentata
    return dp[len(s)]

# Esempi di test
print(word_break("leetcode", ["leet", "code"]))  # Output: True
print(word_break("applepenapple", ["apple", "pen"]))  # Output: True
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
print("\n")

'''
Question 5

Data l'inizio di una lista concatenata, invertire la lista e restituire la lista invertita.
'''
print("Question 5\n")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    # Costruiamo la lista invertita
    result = []
    while prev is not None:
        result.append(prev.val)
        prev = prev.next

    return result

# Esempio di utilizzo
head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
print(reverse_list(head))
print("\n")

'''
Question 6

Progettare un semplice sistema bancario con i seguenti requisiti:

    Classe del Account:
        Attributi:
            account_id: str - identificatore univoco per l'account.
            balance: float - il saldo attuale del conto.
        Metodi:
            deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
            get_balance(): restituisce il saldo corrente del conto.
    Classe Bank:
        Attributi:
            accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
        Metodi:
            create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
            deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
            get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
'''

print("Question 6\n")

class Account:
    def __init__(self, account_id: str):
        # Inizializza un nuovo account con l'ID specificato e un saldo iniziale di 0.0
        self.account_id = account_id
        self.balance = 0.0

    def deposit(self, amount: float):
        # Aggiunge l'importo specificato al saldo dell'account
        self.balance += amount

    def get_balance(self) -> float:
        # Restituisce il saldo attuale dell'account
        return self.balance


class Bank:
    def __init__(self):
        # Inizializza un nuovo oggetto Bank con un dizionario vuoto per memorizzare gli account
        self.accounts = {}

    def create_account(self, account_id: str) -> Account:
        # Crea un nuovo account con l'ID specificato e lo aggiunge al dizionario degli account
        if account_id not in self.accounts:
            new_account = Account(account_id)
            self.accounts[account_id] = new_account
            return new_account
        else:
            print("Account ID already exists.")
            return None

    def deposit(self, account_id: str, amount: float):
        # Deposita l'importo specificato sull'account con l'ID fornito
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
        else:
            print("Account ID does not exist.")

    def get_balance(self, account_id: str) -> float:
        # Restituisce il saldo dell'account con l'ID specificato
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        else:
            print("Account ID does not exist.")
            return None

# Esempi di utilizzo
bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())

bank = Bank()
account1 = bank.create_account("123")
bank.deposit("123", 100)
print(bank.get_balance("123"))

bank = Bank()
account2 = bank.create_account("456")
bank.deposit("456", 200)
print(bank.get_balance("456"))

bank = Bank()
account1 = bank.create_account("123")
try:
    bank.create_account("123")
except ValueError as e:
    print(e)

bank = Bank()
try:
    bank.get_balance("456")
except ValueError as e:
    print(e)
print("\n")

'''
Question 7

Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

    Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Metodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro.
'''
print("Question 7\n")

class Book:
    def __init__(self, book_id, title, author):
        # Inizializzazione degli attributi di un libro
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False  # All'inizio il libro non è preso in prestito

    def borrow(self):
        # Metodo per contrassegnare il libro come preso in prestito
        if not self.is_borrowed:
            self.is_borrowed = True  # Se il libro non è già preso in prestito, lo contrassegna come preso
        else:
            raise ValueError("Book is already borrowed")  # Solleva un'eccezione se il libro è già in prestito

    def return_book(self):
        # Metodo per contrassegnare il libro come restituito
        if self.is_borrowed:
            self.is_borrowed = False  # Se il libro è in prestito, lo contrassegna come restituito
        else:
            raise ValueError("Book is not borrowed")  # Solleva un'eccezione se il libro non è in prestito


class Member:
    def __init__(self, member_id, name):
        # Inizializzazione degli attributi di un membro
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # All'inizio il membro non ha libri in prestito

    def borrow_book(self, book):
        # Metodo per aggiungere un libro nella lista dei libri presi in prestito dal membro
        if book not in self.borrowed_books:
            book.borrow()  # Contrassegna il libro come preso in prestito
            self.borrowed_books.append(book)  # Aggiunge il libro alla lista dei libri presi in prestito
        else:
            raise ValueError("Book is already borrowed by the member.")  # Solleva un'eccezione se il libro è già preso in prestito dal membro

    def return_book(self, book):
        # Metodo per rimuovere un libro dalla lista dei libri presi in prestito dal membro
        if book in self.borrowed_books:
            book.return_book()  # Contrassegna il libro come restituito
            self.borrowed_books.remove(book)  # Rimuove il libro dalla lista dei libri presi in prestito
        else:
            raise ValueError("Book not borrowed by this member")  # Solleva un'eccezione se il libro non è preso in prestito dal membro


class Library:
    def __init__(self):
        # Inizializzazione dei dizionari per memorizzare i libri e i membri della biblioteca
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        # Metodo per aggiungere un nuovo libro nella biblioteca
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)  # Crea un nuovo oggetto Book e lo aggiunge al dizionario dei libri
        else:
            raise ValueError("Book ID already exists")  # Solleva un'eccezione se l'ID del libro già esiste

    def register_member(self, member_id, name):
        # Metodo per iscrivere un nuovo membro nella biblioteca
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)  # Crea un nuovo oggetto Member e lo aggiunge al dizionario dei membri
        else:
            raise ValueError("Member ID already exists")  # Solleva un'eccezione se l'ID del membro già esiste

    def borrow_book(self, member_id, book_id):
        # Metodo per permettere a un membro di prendere in prestito un libro
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)  # Chiama il metodo borrow_book del membro per prendere in prestito il libro
        elif member_id not in self.members:
            raise ValueError("Member not found")  # Solleva un'eccezione se il membro non esiste
        else:
            raise ValueError("Book not found")  # Solleva un'eccezione se il libro non esiste

    def return_book(self, member_id, book_id):
        # Metodo per permettere a un membro di restituire un libro
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)  # Chiama il metodo return_book del membro per restituire il libro
        else:
            raise ValueError("Member or book does not exist")  # Solleva un'eccezione se il membro o il libro non esistono

    def get_borrowed_books(self, member_id):
        # Metodo per restituire la lista dei libri presi in prestito da un membro
        if member_id in self.members:
            member = self.members[member_id]
            return [book.title for book in member.borrowed_books]  # Restituisce una lista dei titoli dei libri presi in prestito dal membro
        else:
            raise ValueError("Member does not exist")  # Solleva un'eccezione se il membro non esiste

#Test 1

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

#test 2

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Check borrowed books after returning
print(library.get_borrowed_books("M001"))
print(library.get_borrowed_books("M002"))

#test 3

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

library.borrow_book("M001", "B001")
try:
    library.borrow_book("M002", "B001")
except ValueError as e:
    print(e)

#test 4

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")

# Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Edge case - trying to return a book that is not borrowed
try:
    library.return_book("M001", "B003")
except ValueError as e:
    print(e)

#test 5

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")


 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")


# Edge case - trying to borrow a book by a non-existent member
try:
    library.borrow_book("M004", "B001")
except ValueError as e:
    print(e)

#test 6

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")


 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")


# Edge case - trying to borrow a non-existent book
try:
    library.borrow_book("M001", "B004")
except ValueError as e:
    print(e)

#test 7

library = Library()

library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")

# Register members
library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

# Borrow books
library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")


 # Return books
library.return_book("M001", "B001")
library.return_book("M002", "B002")

# Complex Test Case 1: Multiple members borrow and return books
# Alice borrows "1984" and "To Kill a Mockingbird"
library.borrow_book("M001", "B002")
library.borrow_book("M001", "B003")

# Bob tries to borrow "1984" (already borrowed by Alice)
try:
    library.borrow_book("M002", "B002")
except ValueError as e:
    print(e)