from DAOs.dao import DAO
from prato import Prato

#cada entidade terá uma classe dessa, implementação bem simples.
class PratoDAO(DAO):
    def __init__(self):
        super().__init__('pratos.pkl')

    def add(self, prato: Prato):
        if((prato != None) and isinstance(prato, Prato) and isinstance(prato.codigo, int)):
            super().add(prato.codigo, prato)

    def update(self, prato: Prato):
        if((prato is not None) and isinstance(prato, Prato) and isinstance(prato.codigo, int)):
            super().update(prato.codigo, prato)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)