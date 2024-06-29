from DAOs.dao import DAO
from bebida import Bebida

#cada entidade terá uma classe dessa, implementação bem simples.
class BebidaDAO(DAO):
    def __init__(self):
        super().__init__('bebidas.pkl')

    def add(self, bebida: Bebida):
        if((bebida != None) and isinstance(bebida, Bebida) and isinstance(bebida.codigo, int)):
            super().add(bebida.codigo, bebida)

    def update(self, bebida: Bebida):
        if((bebida is not None) and isinstance(bebida, Bebida) and isinstance(bebida.codigo, int)):
            super().update(bebida.codigo, bebida)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)