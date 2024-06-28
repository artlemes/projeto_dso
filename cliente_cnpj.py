from cliente import Cliente

class ClienteCnpj(Cliente):

    def __init__(self, nome: str, celular: str, email: str, cnpj: str):
        super().__init__(nome, celular, email)
        self.__cnpj = cnpj
        self.__desconto = 0.1

    @property
    def desconto(self):
        return self.__desconto

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, novo):
        self.__cnpj = novo