from contato import Contato

class Pessoa():
    #arrumei o construtor, agora sim é composicao
    def __init__(self, nome: str, celular: str, email: str):
        self.__nome = nome
        self.__contato = Contato(celular, email)

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo):
        if isinstance(novo, str):
            self.__nome = novo
    
    @property
    def contato(self):
        return self.__contato
    
    
    @contato.setter
    def contato(self, celular, email):
        if isinstance(celular, str) and isinstance(email, str):
            self.__contato.celular = celular
            self.__contato.email = email