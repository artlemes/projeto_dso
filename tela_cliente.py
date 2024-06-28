class TelaCliente():
    def __init__(self):
        pass

    def tela_opcoes(self) -> any:
        print('-----Cliente-----')
        print('Opcoes:')
        print('1) Cadastro de cliente cnpj')
        print('2) Cadastro de cliente cpf')
        print('0) Retornar')
        opcao = input('Escolha uma opcao:')
        return opcao
    
    def mostra_msg(self, mensagem):
        print(mensagem)