#  EDOARDO DI LISIO
#  28.06.2024

'''
1.

The Number of Beautiful Subsets: write a function with an array nums of positive integers and a positive integer k given as inputs. 
A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k. Return the number of non-empty 
beautiful subsets of the array nums. A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. 
Two subsets are different if and only if the chosen indices to delete are different.

Example 1:
Input: nums = [2,4,6], k = 2
Output: 4

Example 2:
Input: nums = [1], k = 1
Output: 1

2.

Combinations: given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the 
answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

3.

Generate Parentheses: Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

# Esercizio 1: Numero di Sottoinsiemi Bellissimi
def count_beautiful_subsets(nums, k):
    from itertools import combinations  # Importiamo la funzione combinations dalla libreria itertools
    
    # Funzione che verifica se un sottoinsieme è "bellissimo"
    def is_beautiful(subset):
        for i in range(len(subset)):  # Iteriamo su ogni elemento del sottoinsieme
            for j in range(i + 1, len(subset)):  # Confrontiamo ogni elemento con gli altri nel sottoinsieme
                if abs(subset[i] - subset[j]) == k:  # Controlliamo se la differenza assoluta è uguale a k
                    return False  # Se sì, il sottoinsieme non è bellissimo
        return True  # Se nessuna coppia ha differenza assoluta k, il sottoinsieme è bellissimo
    
    n = len(nums)  # Lunghezza dell'array nums
    beautiful_count = 0  # Contatore per i sottoinsiemi bellissimi
    
    # Generiamo tutti i sottoinsiemi non vuoti di nums
    for i in range(1, n + 1):
        for subset in combinations(nums, i):  # Generiamo i sottoinsiemi di lunghezza i
            if is_beautiful(subset):  # Verifichiamo se il sottoinsieme è bellissimo
                beautiful_count += 1  # Incrementiamo il contatore se il sottoinsieme è bellissimo
    
    return beautiful_count  # Restituiamo il numero totale di sottoinsiemi bellissimi

# Esempi per Esercizio 1
print(count_beautiful_subsets([2, 4, 6], 2))  # Output: 4
print(count_beautiful_subsets([1], 1))  # Output: 1


# Esercizio 2: Combinazioni
def combine(n, k):
    from itertools import combinations  # Importiamo la funzione combinations dalla libreria itertools
    
    return list(combinations(range(1, n + 1), k))  # Generiamo e restituiamo tutte le combinazioni di k elementi da 1 a n

# Esempi per Esercizio 2
print(combine(4, 2))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(combine(1, 1))  # Output: [(1)]


# Esercizio 3: Generazione di Parentesi
def generate_parenthesis(n):
    # Funzione di backtracking per generare tutte le combinazioni di parentesi bilanciate
    def backtrack(s = '', left = 0, right = 0):
        if len(s) == 2 * n:  # Se la lunghezza della stringa s è uguale a 2n, abbiamo una combinazione valida
            res.append(s)  # Aggiungiamo la combinazione alla lista dei risultati
            return
        if left < n:  # Se possiamo ancora aggiungere una parentesi aperta
            backtrack(s + '(', left + 1, right)  # Aggiungiamo una parentesi aperta e continuiamo
        if right < left:  # Se possiamo ancora aggiungere una parentesi chiusa
            backtrack(s + ')', left, right + 1)  # Aggiungiamo una parentesi chiusa e continuiamo
    
    res = []  # Lista per memorizzare le combinazioni di parentesi ben formate
    backtrack()  # Iniziamo il processo di backtracking
    return res  # Restituiamo tutte le combinazioni generate

# Esempi per Esercizio 3
print(generate_parenthesis(3))  # Output: ["((()))","(()())","(())()","()(())","()()()"]
print(generate_parenthesis(1))  # Output: ["()"]
