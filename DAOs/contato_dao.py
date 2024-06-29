from DAOs.dao import DAO
from contato import Contato

#cada entidade terá uma classe dessa, implementação bem simples.
class ContatoDAO(DAO):
    def __init__(self):
        super().__init__('contatos.pkl')

    def add(self, contato: Contato):
        if((contato != None) and isinstance(contato, Contato) and isinstance(contato.celular, str)):
            super().add(contato.celular, contato)

    def update(self, contato: Contato):
        if((contato is not None) and isinstance(contato, Contato) and isinstance(contato.celular, str)):
            super().update(contato.celular, contato)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if(isinstance(key, str)):
            return super().remove(key)