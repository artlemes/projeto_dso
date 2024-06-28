from produto import Produto

class Prato(Produto):
    def __init__(self, nome: str, preco: float, despesa: float, codigo: str) -> None:
        super().__init__(nome, preco, despesa, codigo)
