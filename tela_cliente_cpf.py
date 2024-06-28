#tela tudo ok

class TelaClienteCpf():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self) -> any:
        print('-----Clientes cpf-----')
        print('Opcoes:')
        print('1) Incluir cliente')
        print('2) Alterar cliente')
        print('3) Listar cliente')
        print('4) Excluir cliente')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
   
    def pega_dados_cliente_cpf(self):
        print('-----Dados para cliente cpf-----')
        nome = input('Nome: ')
        celular = input('Celular: ')
        email = input('Email: ')
        cpf = input('cpf: ')

        return {'nome':nome, 'celular':celular,
                'email':email, 'cpf':cpf}
   
    def seleciona_cliente_cpf(self):
        cpf = input('Digite o cpf do cliente que quer selecionar: ')
        return cpf

    def mostra_cliente_cpf(self, cliente):
        print('Nome do(a) cliente: ', cliente.nome)
        print('Celular do(a) cliente: ', cliente.contato.celular)
        print('Email do(a) cliente: ', cliente.contato.email)
        print('Cpf do(a) cliente: ', cliente.cpf)
        print('\n')

    def mostra_msg(self, mensagem):
        print(mensagem)

    def espacamento(self):
        print()