# Scrivi una funzione che accetta una stringa come input, rimuove le parole non significative comuni stop_words e 
# restituisce un dizionario in cui le chiavi sono parole univoche nel testo rimanente (ignorando la distinzione tra maiuscole e 
# minuscole e la punteggiatura) e i valori sono le frequenze di quelle parole.

def word_frequency(text: str, stopwords: list[str]) -> dict[str, int]:
    
    cleaned_text = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text)
    words = cleaned_text.split()
    word_count = {}
    for word in words:
        if word not in stopwords:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count