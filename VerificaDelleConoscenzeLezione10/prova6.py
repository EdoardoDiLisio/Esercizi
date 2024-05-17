'''
Definire una funzione chiamata hypotenuse che calcoli la lunghezza dell'ipotenusa di un triangolo rettangolo. La funzione deve ricevere due argomenti di tipo float (corrispondenti ai due lati del triangolo) e restituire l'ipotenusa come un float.


Per calcolare l'ipotenusa, si può ricorrere al teorema di Pitagora.
'''

def hypotenuse(side1: float, side2: float) -> float:
    # Calcolo dell'ipotenusa utilizzando il teorema di Pitagora
    hypotenuse_length = (side1 ** 2 + side2 ** 2) ** 0.5
    return hypotenuse_length

print(hypotenuse(3.0, 4.0))

print(hypotenuse(8.0, 15.0))

	

