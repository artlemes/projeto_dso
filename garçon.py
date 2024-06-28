from pessoa import Pessoa
from mesa import Mesa


class Garçon(Pessoa):
    def __init__(self, nome: str, celular: str, email: str, cpf: str):
        super().__init__(nome, celular, email)
        self.__cpf = cpf
        self.__mesas = []
        self.__lista_de_comissao = []

    @property
    def mesas(self):
        return self.__mesas

    def atender_mesa(self, mesa):
        if isinstance(mesa, Mesa) and mesa not in self.mesas:
            self.mesas.append(mesa)

    def rm_mesa(self, mesa):
        if mesa in self.mesa:
            self.mesas.remove(mesa)

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, novo):
        self.__comissao = novo

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo):
        self.__cpf = novo

    @property
    def lista_de_comissao(self):
        return self.__lista_de_comissao
    
    @lista_de_comissao.setter
    def lista_de_comissao(self, nova):
        self.__lista_de_comissao = nova
    
    @property
    def comissao(self):
        soma = 0
        for conta in self.lista_de_comissao:
            soma += conta.comissao
        return soma