

class DadosInsuficientesException(Exception):

    def __init__(self):
        self.mensagem = 'Preencha todos os campos corretamente'
        super().__init__(self.mensagem)