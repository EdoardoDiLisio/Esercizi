

def is_valid_parenthesis(s: str) -> bool:
    possible_parenthesis = {'(': ')', '[': ']', '{':'}'}
    parenthesis_stack = []
    for char in s:
        if char in possible_parenthesis:
            parenthesis_stack.append(char)
        else:
            val = parenthesis_stack.pop()
            if char != possible_parenthesis[val]:
                return False    
    return True


print(is_valid_parenthesis("()"))
print(is_valid_parenthesis("()[]{}"))
print(is_valid_parenthesis("(]"))
print(is_valid_parenthesis("([)]"))      # Output: False
print(is_valid_parenthesis("{[]}"))
print(is_valid_parenthesis(""))


