

class CodigoSemCaracteresMinimosException(Exception):

    def __init__(self):
        self.mensagem = 'O código não contém a quantidade correta de caracteres'
        super().__init__(self.mensagem)