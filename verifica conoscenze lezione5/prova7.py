'''
Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, 
cioè per ogni parentesi che apre c'è la corrispondente parentesi che chiude.
'''
def check_parentheses(expression: str) -> bool:
    stack = []
    
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0
