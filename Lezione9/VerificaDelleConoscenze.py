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