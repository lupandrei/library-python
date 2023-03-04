import re
class ValidatorCarte(object):

        
        
    def valideaza_carte(self, carte):
        strr = ""
        if carte.get_id() < 0:
            strr += "Id-ul trebuie sa fie numar intreg pozitiv\n"
        if len(carte.get_titlu()) == 0:
            strr += "Cartea trebuie sa aiba un titlu\n"
        if len(carte.get_autor()) == 0:
            strr += "Autorul trebuie sa aiba un nume\n"
        if len(strr) > 0:
            raise Exception(strr)
        

class ValidatorClient(object):
    
    def __valideaza_cnp(self, cnp):
        strr = ""
        zi = int(cnp[5])*10 + int(cnp[6])
        luna = int(cnp[3])*10 + int(cnp[4])
        if zi > 31 or zi > 28 and luna == 2:
            strr += "Zi invalida cnp\n"
        if luna > 12:
            strr += "Luna invalida cnp\n"
        if len(strr) > 0:
            raise Exception(strr)
            
        
    def valideaza_client(self, client):
        strr = ""
        if client.get_id() < 0:
            strr += "Id-ul trebuie sa fie numar intreg pozitiv\n"
        if len(client.get_name()) == 0:
            strr += "Clientul trebuie sa aiba un nume\n"
        try:
            self.__valideaza_cnp(client.get_cnp())
        except Exception as ex:
            strr += str(ex)
        if len(strr) > 0:
            raise Exception(strr)
        
    def valideaza_client_random(self, client):
        strr = ""
        if client.get_id() < 0:
            strr += "Id-ul trebuie sa fie numar intreg pozitiv\n"
        if len(client.get_name()) == 0:
            strr += "Clientul trebuie sa aiba un nume\n"
        if len(client.get_cnp()) != 13:
            strr += "Clientul trebuie sa aiba un cnp din 13 cifre\n"    
        if len(strr) > 0:
            raise Exception(strr)
    

class ValidatorInchiriere(object):
    def __valideaza_data(self,x):
        """
        Metoda care valideaza corectitudinea unei date data de catre utilizator
        """
        year = int(x[6:])
        month = int(x[3])*10+int(x[4])
        day = int(x[0])*10+int(x[1])
        strr = ""
        if day > 31:
            strr += "O luna nu are mai mult de 31 de zile\n"
        if month > 12:
            strr += "Un an nu are mai mult de 12 luni\n"
        if month not in {1, 3, 5, 7, 8, 10, 12} and day == 31:
            strr += "Luna data nu are 31 de zile\n"
        if month == 2 and day > 29:
            strr += "Luna februarie nu are mai mult de 29 de zile\n"
        elif month == 2:
            if year % 400 != 0 and year % 4 != 0 and day > 28:
                strr += "Anul nu este bisect\n"
        if len(strr) > 0:
            raise Exception(strr)
        
    def __valid_date_format(self,x):
        """
        Functie care valideaza formatul unei date.
        :param x: string
        :return: True - daca formatul este "dd/mm/yyyy"
                 False - altfel
        """
        matched = re.match("[0-3][0-9][/][0-1][0-9][/][0-9][0-9][0-9][0-9]", x)
        return matched
    
    def valideaza_inchiriere(self, inchiriere):
        """
        Metoda care valideaza corectitudiena datelor unei inchirieri.
        """
        strr = ""
        if inchiriere.get_id_inchiriere() < 0:
            strr += "Id-ul trebuie sa fie numar intreg pozitiv\n"
        if not self.__valid_date_format(inchiriere.get_data_inchiriere()):
                strr += "Formatul datei este invalid\n"
        else:
            try:
                self.__valideaza_data(inchiriere.get_data_inchiriere())
            except Exception as ex:
                    strr += str(ex)
        if len(strr) > 0:
            raise Exception(strr)
    
    def valideaza_inchiriere_random(self, inchiriere):
        """
        Metoda care valideaza corectitudiena datelor unei inchirieri.
        """
        strr = ""
        if inchiriere.get_id_inchiriere() < 0:
            strr += "Id-ul trebuie sa fie numar intreg pozitiv\n"
        if not self.__valid_date_format(inchiriere.get_data_inchiriere()):
                strr += "Formatul datei este invalid\n"
        if len(strr) > 0:
            raise Exception(strr)


    def valideaza_returnare(self,id,data):
        """
        Metoda care valideaza corectitudinea unei returnari.
        """
        strr = ""
        if id < 0:
            strr += "Id-ul trebuei sa fie numar intreg pozitiv\n"
        if not self.__valid_date_format(data):
            strr += "Formatul datei este invalid\n"
        else:
            try:
                self.__valideaza_data(data)
            except Exception as ex:
                strr += str(ex)
        if len(strr) > 0:
            raise Exception(strr)