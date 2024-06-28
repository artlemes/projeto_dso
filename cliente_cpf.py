from cliente import Cliente

class ClienteCpf(Cliente):

    def __init__(self, nome: str, celular: str, email: str, cpf: str):
        super().__init__(nome, celular, email)
        self.__cpf = cpf
        self.__quantidade_pratos = 0

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo):
        self.__cpf = novo

    @property
    def quantidade_pratos(self):
        return self.__quantidade_pratos
    
    @quantidade_pratos.setter
    def quantidade_pratos(self, novo):
        self.quantidade_pratos = novo


    