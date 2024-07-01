from DAOs.dao import DAO
from conta import Conta

#cada entidade terá uma classe dessa, implementação bem simples.
class ContaDAO(DAO):
    def __init__(self):
        super().__init__('contas.pkl')

    def add(self, conta: Conta):
        if((conta != None) and isinstance(conta, Conta) and isinstance(conta.codigo_conta, int)):
            super().add(conta.codigo_conta, conta)

    def update(self, conta: Conta):
        if((conta is not None) and isinstance(conta, Conta) and isinstance(conta.codigo_conta, int)):
            super().update(conta.codigo_conta, conta)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)