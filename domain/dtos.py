class RentalDTO(object):
    def __init__(self,id_rental,id_client,id_carte,data_inchiriere,data_returnare):
        self.__id_rental = id_rental
        self.__id_client = id_client
        self.__id_carte = id_carte
        self.__data_inchiriere = data_inchiriere
        self.__data_returnare = data_returnare

    def get_id_inchiriere(self):
        return self.__id_rental


    def get_id_client(self):
        return self.__id_client


    def get_id_carte(self):
        return self.__id_carte


    def get_data_inchiriere(self):
        return self.__data_inchiriere


    def get_data_returnare(self):
        return self.__data_returnare


    def set_id_client(self, value):
        self.__id_client = value


    def set_id_carte(self, value):
        self.__id_carte = value


    def set_data_inchiriere(self, value):
        self.__data_inchiriere = value


    def set_data_returnare(self, value):
        self.__data_returnare = value

class CartiClient(object):
    def __init__(self,nume_client,lista_carti):
        self.__nume_client = nume_client
        self.__lista_carti = lista_carti
    
    def __str__(self):
        st = ""
        st += self.__nume_client +":\n"
        for carte in self.__lista_carti:
            st +="\t" + str(carte)
        return st

class CarteInhchirieriDTO(object):
    def __init__(self,titlu,numar_inchirieri):
        self.__titlu = titlu
        self.__numar_inchirieri = numar_inchirieri

    def get_titlu(self):
        return self.__titlu


    def get_numar_inchirieri(self):
        return self.__numar_inchirieri
    
    def __str__(self):
        return "Cartea " + str(self.__titlu) + " a fost inchiriata de " + str(self.__numar_inchirieri) + " ori"
    
class ClientInchirieriDTO(object):
    def __init__(self,nume,numar_inchirieri):
        self.__nume = nume
        self.__numar_inchirieri = numar_inchirieri

    def get_nume(self):
        return self.__nume


    def get_numar_inchirieri(self):
        return self.__numar_inchirieri
    
    def __str__(self):
        return "Clientul "  + str(self.__nume) + " a inchiriat " + str(self.__numar_inchirieri) + " carti"
    
        
    