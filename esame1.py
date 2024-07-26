class ContactManager:
    def __init__(self):
        self.contacts = {}
        
    def create_contact (self, name:str, phone_numbers: list[str]):
        if name in self.contacts:
            return "Errore: il contatto esiste già."
        self.contacts[name] = phone_numbers
        return {name: phone_numbers}
    
    def add_phone_number (self, contact_name:str, phone_number:str):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number in self.contacts[contact_name]:
            return "Errore: il numero di telefono esiste già."
        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number (self, contact_name: str, phone_number: str):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        if phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}
    
    def update_phone_number (self, contact_name: str, old_phone_number: str, new_phone_number: str):
        if contact_name not in self.contacts:
            return "Errore: il contatto il contatto non esiste."
        if old_phone_number not in self.contacts[contact_name]:
            return "Errore: il numero di telefono non è presente."
        self.contacts[contact_name].remove(old_phone_number)
        self.contacts[contact_name].append(new_phone_number)
        return {contact_name: self.contacts[contact_name]} 
        
    def list_contacts (self):
        return list(self.contacts.keys())
        
    def list_phone_numbers (self, contact_name):
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."
        return self.contacts[contact_name]
        
    def search_contact_by_phone_number (self, contact_name: str):
        lista=[]
        for k,v in self.contacts.items():
            if contact_name in v:
                lista.append(k)
        return lista
        if contact_name not in self.contacts:
            return "Errore: il contatto non esiste."