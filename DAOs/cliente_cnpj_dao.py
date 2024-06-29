from DAOs.dao import DAO
from cliente_cnpj import ClienteCnpj

#cada entidade terá uma classe dessa, implementação bem simples.
class ClienteCnpjDAO(DAO):
    def __init__(self):
        super().__init__('clientes_cnpj.pkl')

    def add(self, cliente_cnpj: ClienteCnpj):
        if((cliente_cnpj != None) and isinstance(cliente_cnpj, ClienteCnpj) and isinstance(cliente_cnpj.cnpj, str)):
            super().add(cliente_cnpj.cnpj, cliente_cnpj)

    def update(self, cliente_cnpj: ClienteCnpj):
        if((cliente_cnpj is not None) and isinstance(cliente_cnpj, ClienteCnpj) and isinstance(cliente_cnpj.cnpj, str)):
            super().update(cliente_cnpj.cnpj, cliente_cnpj)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if(isinstance(key, str)):
            return super().remove(key)