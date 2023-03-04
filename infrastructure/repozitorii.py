
from domain.entities import carte, client, inchiriere
from domain.dtos import RentalDTO
class RepoCarti(object):
    def __init__(self):
        self._entities = {}
    
    def find_by_id(self,entity_id):
        """
        Functie care verifica dupa id, daca aceeasi carte nu a mai fost adaugata inca o data.
        param: entity_id, id-ul cartii
        return: True, daca exista deja 
                False, daca nu exista
        """
        
        for id in self._entities:
            if id == entity_id:
                return self._entities[id]
        return None
        
    def salveaza(self, entity):
        """
        Metoda care salveaza entitatea intr-o lista.
        return: - 
        """
        if self.find_by_id(entity.get_id()) is not None:
            raise Exception("Cartea exista deja in lista\n")
        self._entities[entity.get_id()] = entity
        return entity
    
    def modify(self, id_modify, c):
        """ 
        Nu se foloseste
        Metoda care modifica o entitate.
        param:id_modify - int
              nume - string
              cnp - string
        """
        if self.find_by_id(id_modify) is not None:
            self._entities[id_modify].set_autor(c.get_autor())
            self._entities[id_modify].set_titlu(c.get_titlu())
            self._entities[id_modify].set_descriere(c.get_descriere())
        else:
            raise Exception("Nu exista nicio entitate cu id-ul dat")
           
    def delete(self, id_del):
        """
        Metoda care sterge o entitate cu un id dat
        param: id_del, id-ul entitatii care trebuie stearsa
        raises: Id inexistent
        """
        if self.find_by_id(id_del) is not None:
            del self._entities[id_del]
        else:
            raise Exception("Id inexistent")
                
    
    def get_all_carti(self):
        """
        Metoda care returneaza dictionarul de carti
        """
        return self._entities.values()

    def min_autor(self):
        if self.size() == 0 :
            raise Exception("Nu exista carti, implicit nici autori")
        mini = len(self._entities[1].get_autor())
        strr = ""
        for key in self._entities:
            if len(self._entities[key].get_autor()) < mini:
                mini = len(self._entities[key].get_autor())
                strr = str(self._entities[key])
            elif len(self._entities[key].get_autor()) == mini:
                strr += str(self._entities[key])
        return strr
    
    def print_all(self):
        """
        Returneaza lista de carti
        """
        strr = ""
        for key in self._entities:
            strr += (str(self._entities[key]))
        return strr
    
    
    def size(self):
        """
        Metoda care returneaza numarul de entitati
        """
        return len(self._entities)

class RepoClienti(object):

    def __init__(self):
        self._entities = {}
        
    def find_by_id(self,entity_id):
        """
        Functie care verifica dupa id, daca acelasi client nu a mai fost adaugat inca o data.
        param: entity_id, id-ul clientul
        return: Entitatea, daca exista deja 
                None, daca nu exista
        """
        if entity_id in self._entities:
            return self._entities[entity_id]
        return None


    def salvare(self, entity):
        """
        Metoda care salveaza entitatea intr-o lista
        param: entity - entitate, client
        return: - 
        raises: "Exista un client cu id-ul dat"
        """
        if self.find_by_id(entity.get_id()) is not None: 
            raise Exception("Exista un client cu id-ul dat")
        self._entities[entity.get_id()] = entity
        
     
    def modify(self, id_modify, cl):
        """ 
        Nu se foloseste
        Metoda care modifica o entitate.
        param:id_modify - int
              nume - string
              cnp - string
        """

        if self.find_by_id(id_modify) is not None:
            self._entities[id_modify] = cl
        else:
            raise Exception("Nu exista nicio entitate cu id-ul dat")
    
    def delete(self,id_del):
        """
        Metoda care sterge o entitate cu id-ul dat.
        param: id_del, id-ul pentru care eliminam entitatea
        raises: Id inexistent
        """
        if self.find_by_id(id_del) is not None:
            del self._entities[id_del]
        else:
            raise Exception("Id inexistent")
     
    def get_all_clienti(self):
        """
        Metoda care returneaza lista de clienti
        """
        return self._entities.values()
    
    def size(self):
        """
        Functie care returneaza numarul de entitati
        """
        return len(self._entities)
    
    def print_all(self):
        """
        Returneaza lista de clienti
        """
        strr = ""
        for key in self._entities:
            strr += (str(self._entities[key]))
        return strr
    
class RepoInchiriere(object):
    def __init__(self):
        self._entities = {}
    
    def find_by_id(self,id):
        """
        Metoda care verifica daca exista deja o entitate cu id-ul dat.
        """
        for entity_id in self._entities:
            if entity_id == id:
                return self._entities[entity_id]
        return None
    
    def delete_by_id(self,id_del):
        del self._entities[id_del]
            

    def book_not_rented(self, id_carte):
        """
        Metoda care verifica daca o carte este inchiriata sau nu.
        """
        for id in self._entities:
            if self._entities[id].get_id_carte() == id_carte and self._entities[id].get_data_returnare() == "Cartea nu a fost returnata":
                return self._entities[id].get_id_carte()
        return None
            
    def adauga_inchiriere(self,incDTO):
        """
        Metoda care adauga o inchiriere
        """
        if self.find_by_id(incDTO.get_id_inchiriere()) is not None:
            raise Exception("Exista deja o inchiriere cu id-ul dat")
        if self.book_not_rented(incDTO.get_id_carte()) is None:
            self._entities[incDTO.get_id_inchiriere()] = incDTO
        else:
            raise Exception("Cartea nu a fost returnata")
            
    def get_all_rentals(self):
        """
        Metoda care returneaza toate entitatile din dictionar.
        """
        return self._entities
    
    def print_all(self):  
        """
        Returneaza lista de clienti
        """
        strr = ""
        for key in self._entities:
            strr += (str(self._entities[key]))
        return strr
    
    def __len__(self):
        return len(self._entities)
    
class RepoCartiFile(RepoCarti):
    def __init__(self,filepath):
        RepoCarti.__init__(self)
        self.__filepath = filepath
        
    def __read_all_from_file(self):
        self._entities = {}
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            start = 0
            stop = 3
            try:
                while len(lines[start]) > 0:
                    id_carte = int(lines[start].strip())
                    titlu = lines[start+1].strip()
                    descriere = lines[start+2].strip()
                    autor = lines[start+3].strip()
                    crt = carte(id_carte,titlu,descriere,autor)
                    self._entities[id_carte] = crt
                    start +=4
                    stop +=4
            except:
                pass
            
                    
    def __write_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for carte in self._Carti.values():
                f.write(f"{carte.get_id()}\n{carte.get_titlu()}\n{carte.get_descriere()}\n{carte.get_autor()}\n")
        
    def __append_to_file(self,carte):
        with open(self.__filepath, "a") as f:
            f.write(f"{carte.get_id()}\n{carte.get_titlu()}\n{carte.get_descriere()}\n{carte.get_autor()}\n")
            
    def salveaza(self, entity):
        """
        Metoda care adauga o noua carte in dictionarul de carti.
        """
        self.__read_all_from_file()
        RepoCarti.salveaza(self, entity)
        self.__append_to_file(entity)
    
    def delete(self, id_del):
        """
        Metoda care sterge o carte din lista dupa un id dat
        """
        self.__read_all_from_file()
        RepoCarti.delete(self, id_del)
        self.__write_all_to_file()
        
    def find_by_id(self, entity_id):
        """
        Metoda care cauta o carte dupa id-ul acesteia.
        """
        self.__read_all_from_file()
        return RepoCarti.find_by_id(self, entity_id)    
    
    def get_all_carti(self):
        """
        Metoda care returneaza toate cartile, sub forma unui dictionar de dtos.
        """
        self.__read_all_from_file()
        return RepoCarti.get_all_carti(self)
    
    def size(self):
        """
        Metoda care returneaza numarul de carti
        """
        self.__read_all_from_file()
        return RepoCarti.size(self)
    
    
class RepoInchirieriFile(RepoInchiriere):
    def __init__(self,filepath):
        RepoInchiriere.__init__(self)
        self.__filepath = filepath
    
    def __read_all_from_file(self):
        self._entities = {}
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            start = 0
            stop = 4
            try:
                while len(lines[start]) > 0:
                    id_inc = int(lines[start].strip())
                    id_client = int(lines[start+1].strip())
                    id_carte = int(lines[start+2].strip())
                    data_inchiriere = lines[start+3].strip()
                    data_returnare = lines[stop].strip()
                    rental = RentalDTO(id_inc,id_client,id_carte,data_inchiriere,data_returnare)
                    self._entities[id_inc] = rental
                    start += 5 
                    stop += 5
            except:
                pass
            
    def __write_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for inchiriere in self._entities.values():
                try:
                    f.write(f"{inchiriere.get_id_inchiriere()}\n{inchiriere.get_id_client()}\n{inchiriere.get_id_carte()}\n{inchiriere.get_data_inchiriere()}\n{inchiriere.get_data_returnare()}\n")
                except:
                    pass
                          
    def __append_to_file(self, inchiriere):
        with open(self.__filepath, "a") as f:
            f.write(f"{inchiriere.get_id_inchiriere()}\n{inchiriere.get_id_client()}\n{inchiriere.get_id_carte()}\n{inchiriere.get_data_inchiriere()}\n{inchiriere.get_data_returnare()}\n")
        
    def adauga_inchiriere(self, incDTO):
        """
        Metoda care adauga o noua inchiriere in dictionarul de inchirieri.
        """
        self.__read_all_from_file()
        RepoInchiriere.adauga_inchiriere(self, incDTO)
        self.__append_to_file(incDTO)
            
    def find_by_id(self, id):
        """
        Metoda care cauta o inchiriere dupa un id dat.
        """
        self.__read_all_from_file()
        return RepoInchiriere.find_by_id(self, id)
        
    def get_all_rentals(self):
        """
        Metoda care returneaza toate inchirierile.
        """
        self.__read_all_from_file()
        return RepoInchiriere.get_all_rentals(self)
        
    
    def delete_by_id(self, id_del):
        """
        Metoda care sterge o inchiriere dupa un id dat.
        """
        RepoInchiriere.delete_by_id(self, id_del)  
        self.__write_all_to_file()
          
    def __len__(self):
        """
        Metoda care returneaza numarul de inchirieri.
        """
        return RepoInchiriere.__len__(self)
                           
class RepoClientiFile(RepoClienti):
        def __init__(self,filepath):
            RepoClienti.__init__(self)
            self.__filepath = filepath
        
        def __read_all_from_file(self):
            self._entities = {}
            with open(self.__filepath, "r") as f:
                lines = f.readlines()
                start = 0
                stop = 2
                try:
                    while len(lines[start]) > 0 :
                        line1 = lines[start].strip()
                        line2 = lines[start+1].strip()
                        line3 = lines[stop].strip()                  
                        id_cl = int(line1)
                        nume = line2
                        cnp = line3
                        clnt = client(id_cl, nume,cnp)
                        self._entities[id_cl] = clnt
                        stop += 3
                        start += 3
                except:
                    pass
        
        def __write_all_to_file(self):
            with open(self.__filepath, "w") as f:
                for client in self._entities.values():
                    f.write(f"{client.get_id()}\n{client.get_name()}\n{client.get_cnp()}\n")
                              
        def __append_to_file(self,client):
            with open(self.__filepath, "a") as f:        
                f.write(f"{client.get_id()}\n{client.get_name()}\n{client.get_cnp()}\n")
        
        def salvare(self, entity):
            self.__read_all_from_file()
            RepoClienti.salvare(self, entity)
            self.__append_to_file(entity)
        
        def delete(self, id_del):
            self.__read_all_from_file()
            RepoClienti.delete(self, id_del)
            self.__write_all_to_file()
        
        def find_by_id(self, entity_id):
            self.__read_all_from_file()
            return RepoClienti.find_by_id(self, entity_id)
        
        def get_all_clienti(self):
            self.__read_all_from_file()
            return RepoClienti.get_all_clienti(self)    
        
        def print_all(self):
            self.__read_all_from_file()
            return RepoClienti.print_all(self)
        
        def size(self):
            self.__read_all_from_file()
            return RepoClienti.size(self)