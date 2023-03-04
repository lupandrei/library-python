from domain.entities import client, carte, inchiriere
import random,string,operator
from domain.dtos import RentalDTO, CartiClient, CarteInhchirieriDTO,\
    ClientInchirieriDTO
import copy
from copy import deepcopy
from sortari.sortare import InsertSort, CombSort

class ServiceCarti(object):
    
    
    def __init__(self, valid_carte, repo_carte):
        self.__valid_carte = valid_carte
        self.__repo_carte = repo_carte
    
    def min_autor(self):
        """
        Metoda care returneaza autorul cu cel mai scurt nume
        """
        return self.__repo_carte.min_autor()
    
    def adauga_carte(self, id_carte, titlu, descriere, autor):
        """
        Aceasta metoda adauga o carte.
        """
        c = carte(id_carte, titlu, descriere, autor)
        self.__valid_carte.valideaza_carte(c)
        self.__repo_carte.salveaza(c)
    
    
    def adauga_random(self,n):
        """
        Metoda care adauga random n entitati de tip carte.
        """
        if n == 0:
            return 
        else:
            id = random.randint(100,999999)
            autor_nume =  ''.join((random.choice(string.ascii_letters)) for x in range(6,10))  
            autor_prenume = ''.join((random.choice(string.ascii_letters)) for x in range(6,10))
            descriere = ''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            descriere +=" "+ ''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            titlu = ''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            titlu += " " +''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            autor = autor_nume+ " "+ autor_prenume
            c = carte(id,titlu,descriere,autor)
            self.__valid_carte.valideaza_carte(c)
            try:
                self.__repo_carte.salveaza(c)
                self.adauga_random(n-1)
            except Exception:
                self.adauga_random(n)
            
        
          
    def adauga_randomnotrec(self, n):
        """
        Metoda care adauga random n entitati de tip carte.
        """
        while n:
            id = random.randint(100,999999)
            autor_nume =  ''.join((random.choice(string.ascii_letters)) for x in range(6,10))  
            autor_prenume = ''.join((random.choice(string.ascii_letters)) for x in range(6,10))
            descriere = ''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            descriere +=" "+ ''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            titlu = ''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            titlu += " " +''.join((random.choice(string.ascii_letters)) for x in range(5,20))
            autor = autor_nume+ " "+ autor_prenume
            #n = n-1
            c = carte(id,titlu,descriere,autor)
            self.__valid_carte.valideaza_carte(c)
            try:
                self.__repo_carte.salveaza(c)
                n=n-1
            except Exception:
                continue
            
            
    def modify_book(self, id, titlu, descriere, autor):
        """
        Metoda care modifica datele unei carti
        """
        c = carte(id,titlu,descriere,autor)
        self.__valid_carte.valideaza_carte(c)
        val = self.__repo_carte.find_by_id(id)
        val.set_autor(c.get_autor())
        val.set_titlu(c.get_titlu())
        val.set_descriere(c.get_descriere())
        
    
    def search(self,id):
        """
        Metoda care cauta o carte dupa id
        """
        return self.__repo_carte.find_by_id(id)
    
    def delete_book(self, id_del):
        """
        Metoda care sterge o carte dupa id
        """
        self.__repo_carte.delete(id_del)
        
    def get_all_carti(self):
        """
        Metoda care returneaza toate cartile.
        """
        return self.__repo_carte.get_all_carti()

    def print_all(self):
        """
        Metoda care returneaza 
        """
        return self.__repo_carte.get_all()


class ServiceClienti(object):
    
    
    def __init__(self, valid_client, repo_client):
        self.__valid_client = valid_client
        self.__repo_client = repo_client
        
    def adauga_client(self, id_client, nume, cnp):
        """
        Aceasta metoda adauga un client.
        """
        cl = client(id_client,nume,cnp)
        self.__valid_client.valideaza_client(cl)
        self.__repo_client.salvare(cl)
            
            
    def delete_client(self,id_del):
        """
        Acesta metoda sterge clientul cu id-ul dat.
        """
        self.__repo_client.delete(id_del)
        
    def modify_client(self,id_modify,nume,cnp):
        """
        Metoda care modifica datele unui client.
        """
        cl = client(id_modify,nume,cnp)
        self.__valid_client.valideaza_client(cl)
        val = self.__repo_client.find_by_id(id_modify)
        val.set_name(cl.get_name())
        val.set_cnp(cl.get_cnp())
        
                 
    def search(self, id):
        """
        Aceasta metoda verifica daca exista un client cu id-ul dat
        """
        return self.__repo_client.find_by_id(id)
    
    def get_all_clienti(self):
        """
        Returneaza o lista cu toti clientii stocati
        """
        return self.__repo_client.get_all_clienti()
    
    def print_all(self):
        return self.__repo_client.print_all()

class ServiceInchiriere(object):
    def __init__(self,valid_inchiriere, repo_inchiriere, repo_carte, repo_client):
        self.__valid_inchiriere = valid_inchiriere
        self.__repo_inchiriere = repo_inchiriere
        self.__repo_carte = repo_carte
        self.__repo_client = repo_client

    def adauga_inchiriere(self,id_inchiriere,id_client,id_carte,data_inchiriere,data_returnare = "Cartea nu a fost returnata"):
        """
        Metoda care adauga o noua inchiriere in dictionarul de inchirieri.
        """
        cl = self.__repo_client.find_by_id(id_client)
        carte = self.__repo_carte.find_by_id(id_carte)
        if cl is not None and carte is not None:
            inc = RentalDTO(id_inchiriere, id_client, id_carte, data_inchiriere, data_returnare)
            self.__valid_inchiriere.valideaza_inchiriere(inc)
            self.__repo_inchiriere.adauga_inchiriere(inc)
        else:
            raise Exception("Nu exista client sau carte cu id-ul dat\n")
        
    def sterge_client(self,id_client):
        """
        Metoda care sterge un client dupa id, atat din dictionarul de clienti cat si toate inchirierile clientilor respectivi.
        """
        val = self.__repo_client.find_by_id(id_client)  
        self.__repo_client.delete(id_client)
        rentals = self.get_all_rentals()
        id_dels = []
        for key in list(rentals.items()):
            try:
                ok = key[1].get_client()
                if ok == val:
                    id_dels.append(key[0])
            except:
                id_dels.append(key[0])
        try:  
            for id_del in id_dels:    
                self.__repo_inchiriere.delete_by_id(id_del)
        except:
            pass
            
            
    def sterge_carte(self, id):
        """
        Metoda care sterge o carte, atat din dictionarul de carti cat si toate inchirierile cartii respective.
        """
        val = self.__repo_carte.find_by_id(id)
        self.__repo_carte.delete(id)
        rentals = self.get_all_rentals()
        id_dels = []
        for key in list(rentals.items()):
            try:
                ok = key[1].get_carte()
                if ok == val:
                    id_dels.append(key[0])
            except:
                id_dels.append(key[0])
        try:  
            for id_del in id_dels:    
                self.__repo_inchiriere.delete_by_id(id_del)
        except:
            pass
                          
    def seteaza_data_returnare(self, id, data):
        """
        Metoda care seteaza data de returnare a unei inchirieri.
        """
        self.__valid_inchiriere.valideaza_returnare(id,data)
        lista = self.get_all_rentals()
        if len(lista) == 0:
            raise Exception("Nu exista inchirieri\n")
        inc = self.__repo_inchiriere.find_by_id(id)
        id_client = copy.copy(inc.get_id_client())
        id_carte = copy.copy(inc.get_id_carte())
        data_inchiriere = copy.copy(inc.get_data_inchiriere())
        if inc.get_data_returnare() == "Cartea nu a fost returnata":   
            self.__repo_inchiriere.delete_by_id(id)
            incnew = RentalDTO(id,id_client,id_carte,data_inchiriere,data)
            self.__repo_inchiriere.adauga_inchiriere(incnew)
        else:
            raise Exception("Cartea a fost deja returnata\n")
         
    def raport_top3carti_inchiriate(self):
        """
        Metoda care returneaza un dictionar cu cele mai inchiriate 3 carti.
        """
        rentals = self.get_all_rentals()
        dict_carti = {}
        if len(rentals) == 0:
            raise Exception("Nu exista nicio carte inchiriata")
        for rental in rentals.values():
            if rental.get_carte().get_titlu() not in dict_carti:
                dict_carti[rental.get_carte().get_titlu()] = 1
            else:
                dict_carti[rental.get_carte().get_titlu()] += 1
        rezultate = []
        for dict_carte in dict_carti:
            titlu = dict_carte
            inchirieri = dict_carti[dict_carte]
            carteinchieri = CarteInhchirieriDTO(titlu,inchirieri)
            rezultate.append(carteinchieri)
        sorter = InsertSort()
        sorter.sort(rezultate,key=lambda x:x.get_numar_inchirieri(),reverse=True)
        rezultate = rezultate[:3]
        return rezultate 
        #dict_carti_final = dict(sorted(dict_carti.items(),key=operator.itemgetter(1),reverse=True))
        #lista_carti_final = list(dict_carti_final.items())[:3]
        #return lista_carti_final   
        
    def raport_carti_inchiriate(self):
        """
        Metoda care returneaza un dictionar cu cartile si numarul inchirierilor acestora.
        """
        rentals = self.get_all_rentals()
        dict_carti = {}
        if len(rentals) == 0:
            raise Exception("Nu exista nicio carte inchiriata")
        for rental in rentals.values():
            if rental.get_carte().get_titlu() not in dict_carti:
                dict_carti[rental.get_carte().get_titlu()] = 1
            else:
                dict_carti[rental.get_carte().get_titlu()] += 1
        rezultate = []
        for dict_carte in dict_carti:
            titlu = dict_carte
            inchirieri = dict_carti[dict_carte]
            carteinchirieri = CarteInhchirieriDTO(titlu,inchirieri)
            rezultate.append(carteinchirieri)
        sorter = InsertSort()
        sorter.sort(rezultate,key = lambda x:(x.get_numar_inchirieri(),x.get_titlu()),reverse = True)
        #rezultate = Sortare().insert_sort(rezultate)
        return rezultate
        #dict_carti_final = dict(sorted(dict_carti.items(),key=operator.itemgetter(1),reverse=True))
        #return dict_carti_final   
        
    
    def raport_client_cu_carti(self):
        """
        Metoda care returneaza un dictionar cu numele clientilor si numarul de carti inchiriate de acestia, ordanati dupa nume.
        """
        rentals = self.get_all_rentals()
        dict_clienti = {}
        if len(rentals) == 0:  
            raise Exception("Nu exista nicio inchiriere")
        for rental in rentals.values():
            if rental.get_client().get_name() not in dict_clienti:
                dict_clienti[rental.get_client().get_name()] = 1
            else:
                dict_clienti[rental.get_client().get_name()] += 1
        rezultate = []
        for dict_client  in dict_clienti:
            nume = dict_client
            inchirieri = dict_clienti[dict_client]
            clientinchirieri = ClientInchirieriDTO(nume,inchirieri)
            rezultate.append(clientinchirieri)
        sorter = CombSort()
        sorter.sort(rezultate,lambda x:x.get_nume())
        return rezultate
        #dict_sorted = dict(sorted(dict_clienti.items()))
        #return dict_sorted
    
    def raport_client_cu_carti_numar(self):
        """
        Metoda care returneaza un dictionar cu numele clientilor si numarul de carti inchiriate de acestia, ordonare realizata dupa numarul de inchirieri
        """
        rentals = self.get_all_rentals()
        dict_clienti = {}
        if len(rentals) == 0:  
            raise Exception("Nu exista nicio inchiriere")
        for rental in rentals.values():
            if rental.get_client().get_name() not in dict_clienti:
                dict_clienti[rental.get_client().get_name()] = 1
            else:
                dict_clienti[rental.get_client().get_name()] += 1
        rezultate = []
        for dict_client in dict_clienti:
            nume = dict_client
            inchirieri = dict_clienti[dict_client]
            clientinchirieri = ClientInchirieriDTO(nume,inchirieri)
            rezultate.append(clientinchirieri)
        sorter = InsertSort()
        sorter.sort(rezultate,key=lambda x:x.get_numar_inchirieri(),reverse = True)
        return rezultate
        #dict_sorted = dict(sorted(dict_clienti.items(),key=operator.itemgetter(1),reverse=True))
        #return dict_sorted
    
    def raport_clienti_activi(self):
        """
        Metoda care returneaza o lista formata din numele si numarul de carti ai celor mai activi 20% clienti.
        """
        rentals = self.get_all_rentals()
        dict_clienti = {}
        if len(rentals) == 0:  
            raise Exception("Nu exista nicio inchiriere")
        for rental in rentals.values():
            if rental.get_client().get_name() not in dict_clienti:
                dict_clienti[rental.get_client().get_name()] = 1
            else:
                dict_clienti[rental.get_client().get_name()] += 1
        rezultate = []
        for dict_client in dict_clienti:
            nume = dict_client
            inchirieri = dict_clienti[dict_client]
            clientinchiriere = ClientInchirieriDTO(nume,inchirieri)
            rezultate.append(clientinchiriere)
        sorter = CombSort()
        sorter.sort(rezultate,key = lambda x:x.get_numar_inchirieri(),reverse = True)
        #dict_sorted = dict(sorted(dict_clienti.items(),key=operator.itemgetter(1),reverse=True)) 
        final = int(len(rezultate)//5)+1
        #list_final = list(dict_sorted.items())[:final]   
        return rezultate[:final]
    
    def print_all_rentals(self):
        """
        Metoda care afiseaza clientii impreuna cu cartile inchiriate de acestia.
        """
        rentals = self.get_all_rentals()
        clients_book = {}
        for rental in rentals.values():
            if rental.get_client().get_name() not in clients_book:
                clients_book[rental.get_client().get_name()] = []
            clients_book[rental.get_client().get_name()].append(rental.get_carte())
        rezultat = []
        for client_book in clients_book:
            nume_client = client_book
            carti_client = clients_book[client_book]
            client_carti_dto = CartiClient(nume_client,carti_client)
            rezultat.append(client_carti_dto)
        return rezultat
        
    def get_all_rentals(self):
        """
        Metoda care reconstruieste lista de inchirieri din file, formand dintr-un dictionar de dtos, un dictionar de inchirieri.
        return : rentals - dictionar de inchirieri
        """
        rentals = {}
        rentalDTOS = self.__repo_inchiriere.get_all_rentals()
        for key in rentalDTOS:
            id_rental = key
            client = self.__repo_client.find_by_id(rentalDTOS[key].get_id_client())
            carte = self.__repo_carte.find_by_id(rentalDTOS[key].get_id_carte())
            data_inchiriere = rentalDTOS[key].get_data_inchiriere()
            data_returnare = rentalDTOS[key].get_data_returnare()
            rental = inchiriere(id_rental,client,carte,data_inchiriere,data_returnare)
            rentals[id_rental] = rental
        return rentals
            