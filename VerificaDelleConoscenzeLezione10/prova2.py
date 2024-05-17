'''
Scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
- se x è pari, deve essere diviso per 2;
- se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.
'''

def transform(x: int) -> int:
    if x % 2 == 0:
        # x è pari, dividi per 2
        return x // 2
    else:
        # x è dispari, moltiplica per 3 e sottrai 1
        return x * 3 - 1
    
# Test case 1:
input_1 = 4
output_1_expected = 2
output_1_actual = transform(input_1)
print(f"Input: {input_1}, Expected Output: {output_1_expected}, Actual Output: {output_1_actual}")

# Test case 2: Numero dispari
input_2 = 5
output_2_expected = 14
output_2_actual = transform(input_2)
print(f"Input: {input_2}, Expected Output: {output_2_expected}, Actual Output: {output_2_actual}")

# Test case 3: Numero zero
input_3 = 0
output_3_expected = 0
output_3_actual = transform(input_3)
print(f"Input: {input_3}, Expected Output: {output_3_expected}, Actual Output: {output_3_actual}")

