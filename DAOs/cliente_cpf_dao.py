from DAOs.dao import DAO
from cliente_cpf import ClienteCpf

#cada entidade terá uma classe dessa, implementação bem simples.
class ClienteCpfDAO(DAO):
    def __init__(self):
        super().__init__('clientes_cpf.pkl')

    def add(self, cliente_cpf: ClienteCpf):
        if((cliente_cpf != None) and isinstance(cliente_cpf, ClienteCpf) and isinstance(cliente_cpf.cpf, str)):
            super().add(cliente_cpf.cpf, cliente_cpf)

    def update(self, cliente_cpf: ClienteCpf):
        if((cliente_cpf is not None) and isinstance(cliente_cpf, ClienteCpf) and isinstance(cliente_cpf.cpf, str)):
            super().update(cliente_cpf.cpf, cliente_cpf)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if(isinstance(key, str)):
            return super().remove(key)