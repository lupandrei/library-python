from domain.entities import carte, client, inchiriere
from validare.validatori import ValidatorCarte, ValidatorClient,ValidatorInchiriere
from infrastructure.repozitorii import RepoCarti, RepoClienti, RepoInchiriere,RepoClientiFile,RepoCartiFile,RepoInchirieriFile
from business.servicii import ServiceCarti, ServiceClienti, ServiceInchiriere
from domain.dtos import RentalDTO
import unittest
from sortari.sortare import InsertSort, CombSort
import random

class Teste(unittest.TestCase):
     
    def __test_valideaza_carte(self):
        c = carte(1,"titlu", "ok", "Ion Creanga")
        valid_carte = ValidatorCarte()
        valid_carte.valideaza_carte(c)
        self.assertTrue
        c = carte(1,"", "ok", "Ion Creanga")
        try:
            valid_carte.valideaza_carte(c)
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Cartea trebuie sa aiba un titlu\n")
        c = carte(1,"titlu", "ok", "")
        try:
            valid_carte.valideaza_carte(c)
            assert False
        except Exception as ex:
            self.assertTrue(str(ex) == "Autorul trebuie sa aiba un nume\n")
        c = carte(-1,"titlu", "ok", "Ion Creanga")
        try:
            valid_carte.valideaza_carte(c)
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Id-ul trebuie sa fie numar intreg pozitiv\n")
        c = carte(-1,"", "ok", "Ion Creanga")
        try:
            valid_carte.valideaza_carte(c)
            self.assertFalse
        except Exception:
            self.assertTrue
        c = carte(-1,"titlu", "ok", "")    
        try:
            valid_carte.valideaza_carte(c)
            self.assertFalse
        except Exception:
            self.assertTrue
        c = carte(1,"", "ok", "")
        try:
            valid_carte.valideaza_carte(c)
            self.assertFalse
        except Exception:
            self.assertTrue
        c = carte(-10,"", "ok", "")
        try:
            valid_carte.valideaza_carte(c)
            self.assertFalse
        except Exception:
            self.assertTrue
            
    def __test_valideaza_inchiriere(self):
        v = ValidatorInchiriere()
        c = carte(1,"Ana", "ok", "Dan")
        cl = client(1, "Dorel", "5020503012652")
        inc = inchiriere(1,cl,c,"02/10/2005", "Cartea nu a fost inchiriata")
        v.valideaza_inchiriere(inc)
        self.assertTrue
        inc = inchiriere(-1,cl,c,"02/10/2005", "Cartea nu a fost inchiriata")
        try:
            v.valideaza_inchiriere(inc)
            self.assertFalse
        except Exception:
            self.assertTrue
        inc = inchiriere(1,cl,c,"02/20/2005", "Cartea nu a fost inchiriata") 
        try:
            v.valideaza_inchiriere(inc)
            self.assertFalse
        except Exception:
            self.assertTrue
        inc = inchiriere(1,cl,c,"dataintrodusa", "Cartea nu a fost inchiriata")  
        try:
            v.valideaza_inchiriere(inc)
            self.assertFalse
        except Exception:
            self.assertTrue
            
    def __test_valideaza_returnare(self):
        v = ValidatorInchiriere()
        v.valideaza_returnare(1, "10/10/2005")
        self.assertTrue
        try:
            v.valideaza_returnare(-11, "10/10/2005")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            v.valideaza_returnare(-11, "fasdaf")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            v.valideaza_returnare(11, "2005/10/2004")
            self.assertFalse
        except Exception:
            self.assertTrue
      
    def __test_valideaza_client(self):
        v = ValidatorClient()
        cl = client(1,"Andrei", "5020503012652")
        v.valideaza_client(cl)
        self.assertTrue
        cl = client(-11,"Andrei", "5020503012652")
        try:
            v.valideaza_client(cl)
            self.assertFalse
        except Exception as ex:
            assert str(ex) == "Id-ul trebuie sa fie numar intreg pozitiv\n"
        cl = client(1,"", "5020503012652")
        try:
            v.valideaza_client(cl)
            self.assertFalse
        except Exception as ex:
            assert str(ex) == "Clientul trebuie sa aiba un nume\n"
        cl = client(1,"Andrei", "5021503012652")
        try:
            v.valideaza_client(cl)
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Luna invalida cnp\n")
        cl = client(1,"Andrei", "5020543012652")
        try:
            v.valideaza_client(cl)
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Zi invalida cnp\n")
        cl = client(-1,"", "5020503012652")
        try:
            v.valideaza_client(cl)
            self.assertFalse
        except Exception:
            self.assertTrue
        cl = client(-1,"", "5023503012652")
        try:
            v.valideaza_client(cl)
            self.assertFalse
        except Exception:
            self.assertTrue
    
    def __test_repo_adaug_carte(self):
        rep = RepoCarti()
        c = carte(1,"ana", "ok" , "Dan")
        rep.salveaza(c)
        self.assertTrue(rep.size() == 1)
        c = carte(2,"an", "bun" , "Daniel")
        rep.salveaza(c)
        self.assertTrue(rep.size() == 2)
        c = carte(1,"an", "bun" , "Daniel")
        try:
            rep.salveaza(c)
            self.assertFalse
        except Exception:
            self.assertTrue
            
    def __test_repo_inchiriere_adaugare(self):
        repcl = RepoClienti()
        cl = client(1, "andrei", "5020503012652")
        repcl.salvare(cl)
        self.assertTrue 
        repc = RepoCarti()
        c = carte(1,"ana", "ok" , "Dan")
        repc.salveaza(c)
        rep = RepoInchiriere()   
        inc = RentalDTO(1,1,1,"05/03/2001", "Cartea nu a fost returnata")
        rep.adauga_inchiriere(inc)
        self.assertTrue   
        inc = RentalDTO(1,1,1,"05/03/2001", "Cartea nu a fost returnata")
        try:
            rep.adauga_inchiriere(inc)
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Exista deja o inchiriere cu id-ul dat")
        cl = client(2, "dan", "5020503012653")
        repcl.salvare(cl)
        inc = RentalDTO(2,2,1,"05/03/2001", "Cartea nu a fost returnata")
        try:
            rep.adauga_inchiriere(inc)
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Cartea nu a fost returnata")
        
    
    def __test_repo_adaug_client(self):
        with open("testare/testcarti.txt","w") as f:
            f.write("")
        rep = RepoClientiFile("testare/testcarti.txt")
        vld = ValidatorClient()
        srv = ServiceClienti(vld,rep)
        cl = client(1, "andrei", "5020503012652")
        rep.salvare(cl)
        self.assertTrue(rep.size() == 1)
        cl = client(2, "dan", "5020503012552")
        rep.salvare(cl)
        self.assertTrue(rep.size() == 2)
        cl = client(1, "dan", "5030502012652")
        try:
            srv.adauga_client(1, "dan", "5030502012652")
            self.assertFalse
        except Exception:
            self.assertTrue    
        cl = client(3, "dan", "5030502012")
        try:
            srv.adauga_client(3, "dan", "5030502012652")
            self.assertFalse
        except Exception:
            self.assertTrue
        cl = client(3, "", "5030502012652")
        try:
            srv.adauga_client(3, "", "5030502012652")
            self.assertFalse
        except Exception:
            self.assertTrue
    
    def __test_repo_sterg_carte(self):
        rep = RepoCarti()
        c = carte(1,"ana", "bun", "Dan")
        rep.salveaza(c)
        self.assertTrue(rep.size() == 1)
        rep.delete(1) 
        self.assertTrue(rep.size() == 0)
        c = carte(1,"ana", "bun", "Dan")
        rep.salveaza(c)
        try:
            rep.delete(2)
            self.assertFalse
        except Exception:
            self.assertTrue
    
    def __test_repo_sterg_client(self):
        rep = RepoClienti()
        cl = client(1, "andrei", "5020503012652")
        rep.salvare(cl)
        self.assertTrue(rep.size() == 1)
        rep.delete(1)
        self.assertTrue(rep.size() == 0)
        cl = client(1, "andrei", "5020503012652")
        rep.salvare(cl)
        try:
            rep.delete(2)
            self.assertFalse
        except Exception:
            self.assertTrue
        
    def __test_repo_modify_carte(self):
        rep = RepoCarti()
        c = carte(1, "ana", "ok", "Dan")
        rep.salveaza(c)
        rep.modify(1, c)
        self.assertTrue
        c = carte(1, "ana", "ok", "")
        try: 
            rep.modify(2, c)
            self.assertFalse
        except Exception:
            self.assertTrue
        c = carte(1, "", "ok", "Dan")
        try:
            rep.modify(1, c)
            self.assertFalse
        except Exception:
            self.assertTrue
        c = carte(5, "ana", "ok", "")
        try:
            rep.modify(1, c)
            self.assertFalse
        except Exception:
            self.assertTrue
            
    def __test_repo_modify_client(self):
        rep = RepoClienti()
        cl = client(1, "andrei", "5020503012652")
        rep.salvare(cl)
        cl2 = client(1, "dan", "5020503012652")
        rep.modify(1, cl2)
        self.assertTrue
        try:
            rep.modify(2,cl2)
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            cl_invalid = client(1,"", "5020503012652")
            rep.modify(1,cl_invalid)
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            cl_invalid = client(1,"dan","502")
            rep.modify(1,cl_invalid)
            self.assertFalse
        except Exception:
            self.assertTrue
    
    def __test_repo_minim(self):
        rep = RepoCarti()
        c = carte(1, "The Dead Zone", "ok", "Stephen")
        rep.salveaza(c)
        self.assertTrue(rep.min_autor() == "[1] The Dead Zone de Stephen ok\n")
       
        
    def __test_repo_find_by_id_client(self):
        rep = RepoClienti()
        cl = client(1, "andrei", "5020503012652")
        rep.salvare(cl)
        rep.find_by_id(1)
        self.assertTrue
        try:
            rep.find_by_id(2)
            self.assertFalse
        except Exception:
            self.assertTrue
    
    def __test_repo_find_by_id_carte(self):
        rep = RepoCarti()
        c = carte(1, "ana", "ok", "Dan")   
        rep.salveaza(c)
        rep.find_by_id(1)
        self.assertTrue
        try:
            rep.find_by_id(2)
            self.assertFalse
        except Exception:
            self.assertTrue 
    
    def __test_repo_print_all_client(self):
        rep = RepoClienti()
        cl = client(1, "andrei", "5020503012652")
        rep.salvare(cl)
        strr = rep.print_all()
        self.assertTrue(len(strr) > 0)
        rep.delete(1)
        strr = rep.print_all()
        self.assertTrue(len(strr) == 0)
        
    def __test_repo_print_all_carte(self):
        rep = RepoCarti()
        c = carte(1, "ana", "ok", "Dan")   
        rep.salveaza(c)
        strr = rep.print_all()
        self.assertTrue(len(strr) > 0)
        rep.delete(1)
        strr = rep.print_all()
        self.assertTrue(len(strr) == 0)
    
    def __test_srv_adaugare_client(self):
        v = ValidatorClient()
        rep = RepoClienti()
        srv = ServiceClienti(v, rep)
        srv.adauga_client(1, "Andrei", "5020503012652")
        a = rep.get_all_clienti()
        self.assertTrue(len(a) == 1)
        try:
            srv.adauga_client(1, "Andrei", "5020503012652")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_client(2, "", "5020503012652")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_client(3, "Andrei", "5020503012")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_client(2, "Andrei", "5021503012652")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_client(2, "Andrei", "5020543012652")
            self.assertFalse
        except Exception:
            self.assertTrue
            
    def __test_srv_adauga_carte(self):
        v = ValidatorCarte()
        rep = RepoCarti()
        srv = ServiceCarti(v,rep)
        srv.adauga_carte(1, "ana", "ok", "titlu")
        a = rep.get_all_carti()
        self.assertTrue(len(a) == 1)
        try:
            srv.adauga_carte(-1, "ana", "ok", "titlu")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_carte(1, "dan", "ok", "titlu")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_carte(2, "", "ok", "titlu")
            self.assertFalse
        except Exception:
            self.assertTrue
        try:
            srv.adauga_carte(3, "dan", "ok", "")
            self.assertFalse
        except Exception:
            self.assertTrue
    
    def __test_creaza_repo_client_vid(self):
        with open("testare/testclient.txt","w") as f:
            f.write("")
    
    def __test_creaza_repo_carte_vid(self):
        with open("testare/testcarti.txt","w") as f:
            f.write("")
    
    def __test_creaza_repo_inchiriere_vid(self):
        with open("testare/testinchiriere.txt","w") as f:
            f.write("")
                    
    def __test_srv_inchiriere_adaugare(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        self.__test_creaza_repo_carte_vid()
        self.__test_creaza_repo_client_vid()
        self.__test_creaza_repo_inchiriere_vid()
        repc = RepoCartiFile("testare/testcarti.txt")
        repcl = RepoClientiFile("testare/testclient.txt")
        repinc = RepoInchirieriFile("testare/testinchiriere.txt")
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")  
        srvinc.adauga_inchiriere(1, 1, 1, "05/10/2002", "Cartea nu a fost returnata")
        a = repinc.get_all_rentals()
        #self.assertTrue(len(a) == 1)
        srvc.adauga_carte(2, "dan", "descriere", "autor")
        try:
            srvinc.adauga_inchiriere(1, 1, 2, "05/10/2002", "Cartea nu a fost returnata")
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Exista deja o inchiriere cu id-ul dat") 
        try:
            srvinc.adauga_inchiriere(2,1,1,"05/10/2002", "Cartea nu a fost returnata")
            self.assertFalse
        except Exception as ex:
            self.assertTrue(str(ex) == "Cartea nu a fost returnata")

          
    def __test_srv_inchiriere_returnare(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "dan", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        try:
            srvinc.seteaza_data_returnare(1,"22/10/2002")
            self.assertFalse
        except Exception:
            self.assertTrue  
        srvinc.adauga_inchiriere(1, 1, 1, "05/10/2002", "Cartea nu a fost returnata")
        srvinc.seteaza_data_returnare(1, "25/10/2004")
        self.assertTrue(repinc.find_by_id(1).get_data_returnare() == "25/10/2004")
        try:
            srvinc.seteaza_data_returnare(1,"25/10/2002")
            self.assertFalse
        except Exception:
            self.assertTrue
        srvinc.adauga_inchiriere(2, 1, 2, "05/10/2002", "Cartea nu a fost returnata")
        try:
            srvinc.seteaza_data_returnare(2,"234123421")
            self.assertFalse
        except Exception:
            self.assertTrue
        srvinc.seteaza_data_returnare(2,"23/11/2005")
        self.assertTrue(repinc.find_by_id(2).get_data_returnare() == "23/11/2005")
        
        
    def __srv_sterge_client(self):   
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "dan", "descriere", "autor")
        srvc.adauga_carte(3, "ok", "descriere", "autor")
        srvc.adauga_carte(4, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Alin", "5020503012651")
        srvinc.adauga_inchiriere(1, 1, 1, "21/10/2005", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "21/10/2005", "Cartea nu a fost returnata")
        a = repcl.get_all_clienti()
        a2 = srvinc.get_all_rentals()
        self.assertTrue(len(a) == 2)
        self.assertTrue(len(a2) == 2)
        srvinc.sterge_client(1)
        a = repcl.get_all_clienti()
        a2 = repinc.get_all_rentals()
        self.assertTrue(len(a) == 1)
        self.assertTrue(len(a2) == 1)
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvinc.adauga_inchiriere(4, 1, 3, "21/10/2005", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(5, 2, 4, "21/10/2005", "Cartea nu a fost returnata")
        self.assertTrue(len(a2) == 3)
        self.assertTrue(len(a) == 2)
        srvinc.sterge_client(2)
        self.assertTrue(len(a) == 1)
        try:
            srvinc.sterge_client(1)
            self.assertFalse
        except Exception:
            self.assertTrue
            
    def __srv_sterge_carte(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "dan", "descriere", "autor")
        srvc.adauga_carte(3, "ok", "descriere", "autor")
        srvc.adauga_carte(4, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Alin", "5020503012651")
        srvinc.adauga_inchiriere(1, 1, 1, "21/10/2005", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "21/10/2005", "Cartea nu a fost returnata")
        a = repc.get_all_carti()
        a2 = repinc.get_all_rentals()
        self.assertTrue(len(a) == 4)
        self.assertTrue(len(a2) == 2)
        srvinc.sterge_carte(2)
        self.assertTrue(len(a) == 3)
        self.assertTrue(len(a2) == 1)
     
    def __srv_test_modify_client(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "dan", "descriere", "autor")
        srvc.adauga_carte(3, "ok", "descriere", "autor")
        srvc.adauga_carte(4, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Alin", "5020503012651")
        srvinc.adauga_inchiriere(1, 1, 1, "21/10/2005", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "21/10/2005", "Cartea nu a fost returnata")
        srvcl.modify_client(1, "nume_nou", "50205003012662")
        self.assertTrue(repcl.find_by_id(1).get_name() == "nume_nou")
        all_rentals = srvinc.get_all_rentals()
        self.assertTrue(all_rentals[1].get_client().get_name() == "nume_nou")
        
    def __srv_test_modify_carte(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "dan", "descriere", "autor")
        srvc.adauga_carte(3, "ok", "descriere", "autor")
        srvc.adauga_carte(4, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Alin", "5020503012651")
        srvinc.adauga_inchiriere(1, 1, 1, "21/10/2005", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "21/10/2005", "Cartea nu a fost returnata")       
        srvc.modify_book(1, "titlu", "desc", "at")
        self.assertTrue(repc.find_by_id(1).get_titlu() == "titlu")
        self.assertTrue(repc.find_by_id(1).get_descriere() == "desc")
        self.assertTrue(repc.find_by_id(1).get_autor() == "at")
        all_rentals = srvinc.get_all_rentals()
        self.assertTrue(all_rentals[1].get_carte().get_titlu() == "titlu")
        self.assertTrue(all_rentals[1].get_carte().get_descriere() == "desc")
        self.assertTrue(all_rentals[1].get_carte().get_autor() == "at")
    
    def __srv_test_rapoarte_carti_inchiriate(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "ana", "descriere", "autor")
        srvc.adauga_carte(3, "ana", "descriere", "autor")
        srvc.adauga_carte(4, "ok", "descriere", "autor")
        srvc.adauga_carte(5, "ok", "descriere", "autor")
        srvc.adauga_carte(6, "dan", "descriere", "autor")
        srvc.adauga_carte(7, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Alin", "5020503012651")
        srvinc.adauga_inchiriere(1, 1, 1, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 1, 2, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(3, 1, 3, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(4, 1, 4, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(5, 1, 5, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(6, 1, 6, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(7, 1, 7, "24/10/2001", "Cartea nu a fost returnata")
        val = srvinc.raport_carti_inchiriate()
        assert len(val) == 4
        assert val[0].get_titlu() == "ana"
        assert val[0].get_numar_inchirieri() == 3
        assert val[1].get_titlu() == "ok"
        assert val[1].get_numar_inchirieri() == 2
        #assert val["ok"] == 2
        assert val[2].get_titlu() == "dan"
        assert val[2].get_numar_inchirieri() == 1
        #assert val["dan"] == 1
        assert val[3].get_titlu() == "altacarte"
        assert val[3].get_numar_inchirieri() == 1
        #assert val["altacarte"] == 1
    
    def __test_srv_rapoarte_top3clienti(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "ana", "descriere", "autor")
        srvc.adauga_carte(3, "ana", "descriere", "autor")
        srvc.adauga_carte(4, "ok", "descriere", "autor")
        srvc.adauga_carte(5, "ok", "descriere", "autor")
        srvc.adauga_carte(6, "dan", "descriere", "autor")
        srvc.adauga_carte(7, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Alin", "5020503012651")
        self.assertRaises(Exception,lambda :srvinc.raport_top3carti_inchiriate())
        srvinc.adauga_inchiriere(1, 1, 1, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 1, 2, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(3, 1, 3, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(4, 1, 4, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(5, 1, 5, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(6, 1, 6, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(7, 1, 7, "24/10/2001", "Cartea nu a fost returnata")
        val = srvinc.raport_top3carti_inchiriate()
        self.assertTrue(len(val) == 3)
        self.assertTrue(val[0].get_titlu() == "ana")
        self.assertTrue(val[0].get_numar_inchirieri() == 3)
        #assert val[0][1] == 3
        self.assertTrue(val[1].get_titlu() == "ok")
        self.assertTrue(val[1].get_numar_inchirieri() == 2)
        #assert val[1][1] == 2
        self.assertTrue(val[2].get_numar_inchirieri() == 1)
        #assert val[2][1] ==1
            

    def __test_srv_rapoarte_clienti_nume(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "ana", "descriere", "autor")
        srvc.adauga_carte(3, "ana", "descriere", "autor")
        srvc.adauga_carte(4, "ok", "descriere", "autor")
        srvc.adauga_carte(5, "ok", "descriere", "autor")
        srvc.adauga_carte(6, "dan", "descriere", "autor")
        srvc.adauga_carte(7, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Dan", "5020503012651")
        self.assertRaises(Exception,lambda :srvinc.raport_client_cu_carti())
        srvinc.adauga_inchiriere(1, 2, 1, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(3, 1, 3, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(4, 1, 4, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(5, 1, 5, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(6, 1, 6, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(7, 1, 7, "24/10/2001", "Cartea nu a fost returnata")
        val = srvinc.raport_client_cu_carti()
        self.assertTrue(len(val) == 2)
        self.assertTrue(val[0].get_nume() == "Andrei")
        #assert val["Andrei"] == 5
        self.assertTrue(val[1].get_nume() == "Dan")
        #assert val["Dan"] == 2
        
    def __test_srv_raport_client_numar(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "ana", "descriere", "autor")
        srvc.adauga_carte(3, "ana", "descriere", "autor")
        srvc.adauga_carte(4, "ok", "descriere", "autor")
        srvc.adauga_carte(5, "ok", "descriere", "autor")
        srvc.adauga_carte(6, "dan", "descriere", "autor")
        srvc.adauga_carte(7, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Dan", "5020503012651")
        self.assertRaises(Exception,lambda :srvinc.raport_client_cu_carti())
        srvinc.adauga_inchiriere(1, 2, 1, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(3, 1, 3, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(4, 1, 4, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(5, 1, 5, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(6, 1, 6, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(7, 1, 7, "24/10/2001", "Cartea nu a fost returnata")
        val = srvinc.raport_client_cu_carti_numar()
        self.assertTrue(len(val) == 2)
        self.assertTrue(val[0].get_nume() == "Andrei")
        #val["Andrei"] == 5
        self.assertTrue(val[1].get_nume() == "Dan")
        #assert val["Dan"] == 2
        
    def __test_srv_raport_clienti_activi(self):
        vc = ValidatorCarte()
        vcl = ValidatorClient()
        vinc = ValidatorInchiriere()
        repc = RepoCarti()
        repcl = RepoClienti()
        repinc = RepoInchiriere()
        srvc = ServiceCarti(vc,repc)
        srvcl = ServiceClienti(vcl,repcl)
        srvinc = ServiceInchiriere(vinc,repinc,repc,repcl)
        srvc.adauga_carte(1, "ana", "descriere", "autor")
        srvc.adauga_carte(2, "ana", "descriere", "autor")
        srvc.adauga_carte(3, "ana", "descriere", "autor")
        srvc.adauga_carte(4, "ok", "descriere", "autor")
        srvc.adauga_carte(5, "ok", "descriere", "autor")
        srvc.adauga_carte(6, "dan", "descriere", "autor")
        srvc.adauga_carte(7, "altacarte", "descriere", "autor")
        srvcl.adauga_client(1, "Andrei", "5020503012652")
        srvcl.adauga_client(2, "Dan", "5020503012651")
        srvinc.adauga_inchiriere(1, 2, 1, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(2, 2, 2, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(3, 1, 3, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(4, 1, 4, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(5, 1, 5, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(6, 1, 6, "24/10/2001", "Cartea nu a fost returnata")
        srvinc.adauga_inchiriere(7, 1, 7, "24/10/2001", "Cartea nu a fost returnata")
        val = srvinc.raport_clienti_activi()
        self.assertTrue(len(val) == 1)
        self.assertTrue(val[0].get_nume() == "Andrei")
                
    def __test_srv_adauga_random(self):
        val = ValidatorClient()
        rep = RepoClienti()
        srv = ServiceClienti(val,rep)
        srv.adauga_random(2)
        
    def __test_srv_adauga_inchiriere_random(self):
        valcl = ValidatorClient()
        repcl = RepoClienti()
        srvcl = ServiceClienti(valcl,repcl)
        srvcl.adauga_random(10)
        valc = ValidatorCarte()
        repc = RepoCarti()
        srvc = ServiceCarti(valc,repc)
        srvc.adauga_random(10)
        valinc = ValidatorInchiriere()
        repinc = RepoInchiriere()
        srvinc = ServiceInchiriere(valinc,repinc,repc,repcl)
        srvinc.adauga_inchiriere_random(3)
    

    def __test_sorter_list_int(self, sorter):
        vect = [0,1,2,3,4,5,6,7]
        random.shuffle(vect)
        sorter.sort(vect)
        assert vect == [0,1,2,3,4,5,6,7]
        random.shuffle(vect)
        sorter.sort(vect,reverse=True)
        assert vect == [7,6,5,4,3,2,1,0]
    
    
    def __test_all_sorts(self):
        sorter = InsertSort()
        self.__test_sorter_list_int(sorter)
        sorter = CombSort()
        self.__test_sorter_list_int(sorter)
        
                
    def run_tests(self):
        print("start teste")
        self.__test_valideaza_carte()
        self.__test_valideaza_client()
        self.__test_valideaza_inchiriere()
        self.__test_valideaza_returnare()
        self.__test_repo_adaug_carte()
        self.__test_repo_adaug_client()
        self.__test_repo_inchiriere_adaugare()
        self.__test_repo_sterg_carte()
        self.__test_repo_sterg_client()
        self.__test_repo_modify_carte()
        self.__test_repo_modify_client()
        self.__test_repo_find_by_id_client()
        self.__test_repo_find_by_id_carte()
        self.__test_repo_print_all_carte()
        self.__test_repo_print_all_client()
        self.__test_repo_minim()
        self.__test_srv_adaugare_client()
        self.__test_srv_adauga_carte()
        self.__test_srv_inchiriere_adaugare()
        self.__test_srv_inchiriere_returnare()
        self.__srv_sterge_client()
        self.__srv_sterge_carte()
        self.__srv_test_modify_client()
        self.__srv_test_modify_carte()
        self.__srv_test_rapoarte_carti_inchiriate()
        self.__test_srv_rapoarte_clienti_nume()
        self.__test_srv_raport_client_numar()
        self.__test_srv_raport_clienti_activi()
        self.__test_srv_rapoarte_top3clienti()
        self.__test_all_sorts()
        #self.__test_srv_adauga_random()
        #self.__test_srv_adauga_inchiriere_random()
        print("end tests")
    



