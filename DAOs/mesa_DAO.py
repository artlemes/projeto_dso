from DAOs.dao import DAO
from mesa import Mesa

#cada entidade terá uma classe dessa, implementação bem simples.
class MesaDAO(DAO):
    def __init__(self):
        super().__init__('mesas.pkl')

    def add(self, mesa: Mesa):
        if((mesa != None) and isinstance(mesa, Mesa) and isinstance(mesa.numero_da_mesa, int)):
            super().add(mesa.numero_da_mesa, mesa)

    def update(self, mesa: Mesa):
        if((mesa is not None) and isinstance(mesa, Mesa) and isinstance(mesa.numero_da_mesa, int)):
            super().update(mesa.numero_da_mesa, mesa)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)