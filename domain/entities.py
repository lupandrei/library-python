class carte(object):
    
    def __init__(self, id_carte, titlu, descriere, autor):
        self.__id_carte = id_carte
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
    
    def get_id(self):
        return self.__id_carte
    
    def get_titlu(self):
        return self.__titlu
    
    def get_descriere(self):
        return self.__descriere
    
    def get_autor(self):
        return self.__autor
    
    def set_titlu(self, value):
        self.__titlu = value
    
    def set_descriere(self, descriere):
        self.__descriere = descriere
    
    def set_autor(self, autor):
        self.__autor = autor

    def __str__(self):
        return "[" + str(self.__id_carte) +"] " + str(self.__titlu) + " de " + str(self.__autor) +" "+ str(self.__descriere)+ "\n"
    
    def __eq__(self,other):
        return self.get_id() == other.get_id()
        
class client(object):
    def __init__(self, client_id, name, cnp):
        self.__client_id = client_id
        self.__name = name
        self.__cnp = cnp
    
    def get_id(self):
        return self.__client_id
    
    def get_name(self):
        return self.__name
    
    def get_cnp(self):
        return self.__cnp
    
    def set_name(self, value):
        self.__name = value
    
    def set_cnp(self,value):
        self.__cnp = value
        
    def __eq__(self,other):
        return self.__client_id == other.__client_id
    
    def __str__(self):
        return "[" + str(self.__client_id) + "] " + str(self.__name) +" " + str(self.__cnp)+ "\n"



class inchiriere(object):
    def __init__(self, id_inchiriere, client,carte, data_inchiriere, data_returnare):
        self.__id_inchiriere = id_inchiriere
        self.__client = client
        self.__carte = carte
        self.__data_inchiriere = data_inchiriere
        self.__data_returnare = data_returnare
    
    def get_id_inchiriere(self):
        return self.__id_inchiriere
    
    def get_client(self):
        return self.__client
    
    def set_client(self,other):
        self.__client = other
    
    def get_carte(self):
        return self.__carte
    
    def get_data_inchiriere(self):
        return self.__data_inchiriere
    
    def get_data_returnare(self):
        return self.__data_returnare
    
    def set_data_returnare(self, newdate):
        self.__data_returnare = newdate
    
    def __eq__(self, other):
        return self.__id_inchiriere == other.__id_inchiriere
    
    def __str__(self):
        return "Clientul: " + str(self.__client) + "Cartea: " + str(self.__carte) + "Data de inchiriere: " + str(self.__data_inchiriere) + "\n" + str(self.__data_returnare) + "\n\n"
        
    
