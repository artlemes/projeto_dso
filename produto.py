import abc
class Produto(abc.ABC):
    def __init__(self, nome: str, preco: float, despesa: float, codigo: str) -> None:
        self.__nome = nome
        self.__preco = preco
        self.__despesa = despesa
        self.__codigo = codigo
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        if isinstance(novo_nome, str):
            self.__nome = novo_nome

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float) -> None:
        if isinstance(novo_preco, float):
            self.__preco = novo_preco

    @property
    def despesa(self) -> float:
        return self.__despesa

    @despesa.setter
    def despesa(self, nova_despesa: float) -> None:
        if isinstance(nova_despesa, float):
            self.__despesa = nova_despesa

    @property
    def codigo(self) -> str:
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo: str) -> None:
        if isinstance(novo_codigo, float):
            self.__codigo = novo_codigo
