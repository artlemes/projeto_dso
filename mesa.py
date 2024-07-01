from conta import Conta


class Mesa():

    def __init__(self, numero_da_mesa):
        self.__garçon = None
        self.__numero_da_mesa = numero_da_mesa
        self.__contas = []
        self.__registro = []
 
    @property
    def garçon(self):
        return self.__garçon
    
    @garçon.setter
    def garçon(self, novo):
        self.__garçon = novo

    @property
    def numero_da_mesa(self):
        return self.__numero_da_mesa
    
    @numero_da_mesa.setter
    def numero_da_mesa(self, novo):
        self.numero_da_mesa = novo

    @property
    def contas(self):
        return self.__contas
    
    def add_conta(self, conta):
        if isinstance(conta, Conta):
            self.contas.append(conta)

    def remove_conta(self, conta):
        if isinstance(conta, Conta) and conta in self.contas:
            self.contas.remove(conta)
    
    @property
    def registro(self):
        return self.__registro
    
    @registro.setter
    def registro(self,novo: list):
        self.registro = novo