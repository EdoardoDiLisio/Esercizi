'''
PARTE 1
Scrivi una funzione chiamata create_contact() che accetta il nome e cognome, e-mail (facoltativo) e numero di telefono 
(facoltativo). La funzione dovrebbe restituire un dizionario con i dettagli del contatto.
 
PARTE 2
Scrivi una funzione chiamata update_contact() che accetta il dizionario creato, il nome e cognome del contatto da aggiornare, 
e il dettaglio facoltativo da aggiornare. Questa funzione dovrebbe aggiornare il dizionario del contatto.

'''
#PARTE 1

def create_contact(name: str, email: str=None, telefono: int=None) -> dict:
    
    contact = {"name": name, "email": email, "telefono": telefono}
    return contact


#PARTE 2

def update_contact(dictionary: dict, name: str, email: str =None, telefono: int=None) -> dict:
    
    for contact in dictionary.values():
        if contact["name"] == name:
            if email is not None:
                contact["email"] = email
            if telefono is not None:
                contact["telefono"] = telefono
            break
    return dictionary

################################ERRATO!!!!!!!!!!#########################################
