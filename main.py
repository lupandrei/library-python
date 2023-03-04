
from prezentare.user_interface import consola
from business.servicii import ServiceCarti, ServiceClienti, ServiceInchiriere
from infrastructure.repozitorii import RepoCarti, RepoClienti, RepoInchiriere, RepoCartiFile, RepoClientiFile, RepoInchirieriFile
from validare.validatori import ValidatorCarte, ValidatorClient, ValidatorInchiriere
from testare.teste import Teste

if __name__ == '__main__':
    valid_inchiriere = ValidatorInchiriere()
    valid_carte = ValidatorCarte()
    valid_client = ValidatorClient()
    repo_inchiriere = RepoInchiriere()
    repo_carte = RepoCarti()
    repo_client = RepoClienti()
    repo_carte_file = RepoCartiFile("carti.txt")
    repo_clienti_file = RepoClientiFile("clienti.txt")
    repo_inchirieri_file = RepoInchirieriFile("rentals.txt")
    srv_client = ServiceClienti(valid_client, repo_clienti_file)
    srv_carte = ServiceCarti(valid_carte, repo_carte_file)
    srv_inchiriere = ServiceInchiriere(valid_inchiriere, repo_inchirieri_file, repo_carte_file, repo_clienti_file)
    test = Teste()
    test.run_tests()
    ui = consola(srv_client, srv_carte, srv_inchiriere)
    ui.run()