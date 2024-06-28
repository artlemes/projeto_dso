from abc import ABC
from pessoa import Pessoa

#é abstrato?
class Cliente(Pessoa):

    def __init__(self, nome: str, celular: str, email: str):
        super().__init__(nome, celular, email)