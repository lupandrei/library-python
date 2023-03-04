class consola(object):
    
    def __init__(self,srv_client,srv_carte,srv_inchiriere):
        self.__commands = {1: self.__ui_add_book, 2:self.__ui__add_client, 3: self.__ui_delete_book, 4:self.__ui_delete_client,
                           5:self.__ui_modify_book, 6:self.__ui_modify_client, 7:self.__ui_search_book, 8:self.__ui_search_client,
                           9:self.__ui_cerinta_noua, 10:self.__ui_add_inchiriere, 11:self.__ui_set_returnare, 12:self.__ui_print_carti, 
                           13:self.__ui_print_clienti, 14:self.__ui_add_random_book,15:self.__ui_print_inchirieri,16:self.__ui_cele_mai_inchiriate,
                           17:self.__ui_clienti_cu_carti_inchiriate_nume, 18:self.__ui_clienti_cu_carti_inchiriate_numar, 19:self.__ui_clienti_activi,20:self.__ui_top3}
        self.__srv_client = srv_client
        self.__srv_carte = srv_carte
        self.__srv_inchiriere = srv_inchiriere
    
    def __ui_print_lista_rec(self,rezultate):
        if len(rezultate) == 0 :
            return
        self.__ui_print_lista_rec(rezultate[:-1])
        print(rezultate[len(rezultate)-1])
    
    def __ui_print_lista(self,rezultate):
        for rezultat in rezultate:
            print(rezultat)
            
    def __ui_top3(self):
        try:
            rezultate = []
            rezultate = self.__srv_inchiriere.raport_top3carti_inchiriate()
            self.__ui_print_lista_rec(rezultate)
            #self.__ui_print_lista(rezultate)
        except Exception as ex:
            print(ex)
            
    def __ui_clienti_activi(self):
        try:
            rezultate = self.__srv_inchiriere.raport_clienti_activi()
            self.__ui_print_lista_rec(rezultate)
        except Exception as ex:
            print(ex)
                
    def __ui_clienti_cu_carti_inchiriate_numar(self):
        try:
            rezultate = self.__srv_inchiriere.raport_client_cu_carti_numar()
            self.__ui_print_lista_rec(rezultate)
        except Exception as ex:
            print(ex)
                    
    def __ui_clienti_cu_carti_inchiriate_nume(self):
        try:
            rezultate = self.__srv_inchiriere.raport_client_cu_carti()
            self.__ui_print_lista_rec(rezultate)
        except Exception as ex:
            print(ex)
    
    def __ui_cele_mai_inchiriate(self):
        try:
            rezultate = self.__srv_inchiriere.raport_carti_inchiriate()
            self.__ui_print_lista_rec(rezultate)
        except Exception as ex:
            print(ex)
            
    def __ui_print_inchirieri(self):
        inchirieri = self.__srv_inchiriere.print_all_rentals()
        self.__ui_print_lista_rec(inchirieri)
            
    def __ui_add_random_client(self):
        try:
            n = int(input("Dati numarul de clienti aleatorii pe care doriti sa ii adaugati: "))
            try:
                self.__srv_client.adauga_random(n)
            except Exception as ex:
                print(ex)
        except Exception as ex:
            print(ex)
            
    def __ui_add_random_book(self):
        try:
            n = int(input("Dati numarul de carti aleatorii pe care doriti sa ii adaugati: "))
            try:
                self.__srv_carte.adauga_random(n)
            except Exception as ex:
                print(ex)
        except Exception as ex:
            print(ex)
            
    def __ui_print_carti(self):
        carti = list(self.__srv_carte.get_all_carti())
        self.__ui_print_lista_rec(carti)
        
    def __ui_print_clienti(self):
        clienti = list(self.__srv_client.get_all_clienti())
        self.__ui_print_lista_rec(clienti)
              
    def __ui_set_returnare(self):
        try:
            id = int(input("Dati id: "))
        except ValueError:
            print("Id-ul trebuie sa fie numar intreg")
        data = input("Dati data returnarii(format dd/mm/yyyy): ")
        try:
            self.__srv_inchiriere.seteaza_data_returnare(id,data)
        except Exception as ex:
            print(ex)
        
        
    def __ui_add_inchiriere(self):
        try:
            id_inchiriere = int(input("Dati id inchiriere: "))
        except ValueError:
            print("Id-ul este un numar intreg")
        try:
            id_cl = int(input("Dati id client: "))
        except ValueError:
            print("Id-ul este un numar intreg")
        try:
            id_carte = int(input("Dati id carte: "))
        except ValueError:
            print("Id-ul este un numar intreg")
        data = input("Dati data de inchiriere(format dd/mm/yyyy): ")
        try:
            self.__srv_inchiriere.adauga_inchiriere(id_inchiriere, id_cl, id_carte, data,"Cartea nu a fost returnata")
            print("succes")
        except Exception as ex:
            print(ex)
        
    
    
    def __ui_cerinta_noua(self):   
        try:
            print(self.__srv_carte.min_autor())
        except Exception as ex:
            print(ex)

    def __ui_search_book(self):
        try:
            id = int(input("dati id pentru cautare: "))
            try:
                print(self.__srv_carte.search(id))
            except Exception as ex:
                print(ex)
        except ValueError:
            print("Id-ul trebuie sa fie un numar intreg pozitiv")
    
    def __ui_search_client(self):
        try:
            id = int(input("dati id pentru cautare: "))
            try:
                print(self.__srv_client.search(id))
            except Exception as ex:
                print(ex)
        except ValueError:
            print("Id-ul trebuie sa fie numar intreg pozitiv")
    
    def __ui_modify_book(self):
        try:
            id = int(input("dati id pentru care doriti sa modificati: "))
            titlu = input("dati titlu nou: ")
            descriere = input("dati descriere noua: ")
            autor = input("dati autor: ")
            try:
                self.__srv_carte.modify_book(id,titlu,descriere,autor)
                print("Comanda realizata cu succes")
            except Exception as ex:
                print(ex)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv")
    
    def __ui_modify_client(self):
        try:
            id = int(input("dati id pentru care doriti sa modificati datele: "))
            nume = input("dati  noul nume: ")
            cnp = input("dati noul cnp: ")
            if len(cnp) != 13 or cnp.isdigit() ==  False:
                print("Cnp-ul este invalid\n")
                return
            try:
                self.__srv_client.modify_client(id,nume,cnp)
                print("Comanda realizata cu succes")
            except Exception as ex:
                print(ex)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg pozitiv")
    
    def __ui_delete_book(self):
        try:
            id = int(input("dati id: "))
            try:
                self.__srv_carte.delete_book(id)
            except Exception as ex:
                print(ex)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg")
        print("Comanda realizata cu succes")
            
    
    def __ui_delete_client(self):
        try:
            id = int(input("dati id: "))
            try:
                self.__srv_inchiriere.sterge_client(id)
            except Exception as ex:
                print(ex)
        except ValueError:
            print("id-ul trebuie sa fie numar intreg")
        print("Comanda realizata cu succes")
    
    def __ui__add_client(self):
        try:
            __id = int(input("Dati id client:"))
            __nume = input("Dati numele clientului: ")
        except ValueError:
            print("id-ul trebuie sa fie numar intreg\n")
        __cnp = input("Dati cnp client: ")
        if len(__cnp) != 13 or __cnp.isdigit() ==  False:
            print("Cnp-ul este invalid\n")
            return
        try:
            self.__srv_client.adauga_client(__id, __nume, __cnp)
            print("Comanda realizata cu succes")
        except Exception as ex:
            print(ex)
    
    def __ui_add_book(self):
        try:
            __id = int(input("Dati id carte: "))
            __titlu = input("Dati titlu carte: ")
            __descriere = input("dati descriere carte: ")
            __autor = input("dati autor carte: ")
        except ValueError:
            print("Id-ul trebuie sa fie numar intreg") 
        try:
            self.__srv_carte.adauga_carte(__id,__titlu,__descriere,__autor)
            print("Comanda realizata cu succes!")
        except Exception as ex:
            print(ex)
        
    
    def __print_menu(self):
        print("1. Adaugare carte                                2. Adaugare client")
        print("3. Sterge carte                                  4. Sterge client")
        print("5. Modifica carte                                6. Modifica client")
        print("7. Cauta carte                                   8. Cauta client")
        print("9. Minim")
        print("10. Adaugare inchiriere                          11. Setare data returnare")
        print("12. Lista carti                                  13. Lista Clienti")
        print("14. Adauga carte random                          15. lista Inchirieri")
        print("16. Cele mai inchiriate carti                    17. Clienti cu carti inchiriate(dupa nume)")
        print("18. Clienti cu carti inchiriate(dupa numar)      19. Cei mai activi clienti" )
        print("20. Top 3 carti inchiriate")

    def run(self):
        while True:
            self.__print_menu()
            try:
                cmd = int(input("Alegeti comanda operatia:"))
                if cmd in self.__commands:
                    self.__commands[cmd]()
                else:
                    print("Nu exista comanda data")
            except ValueError:
                print("Comanda invalida")
    



