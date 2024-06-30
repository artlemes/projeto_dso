from DAOs.dao import DAO
from garçon import Garçon

#cada entidade terá uma classe dessa, implementação bem simples.
class garçonDAO(DAO):
    def __init__(self):
        super().__init__('garçons.pkl')

    def add(self, garçon: Garçon):
        if((garçon != None) and isinstance(garçon, Garçon) and isinstance(garçon.cpf, str)):
            super().add(garçon.cpf, garçon)

    def update(self, garçon: Garçon):
        if((garçon is not None) and isinstance(garçon, Garçon) and isinstance(garçon.cpf, str)):
            super().update(garçon.cpf, garçon)

    def get(self, key):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key):
        if(isinstance(key, str)):
            return super().remove(key)