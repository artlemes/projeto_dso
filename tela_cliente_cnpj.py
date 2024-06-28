#tela tudo ok

class TelaClienteCnpj():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self) -> any:
        print('-----Clientes cnpj-----')
        print('Opcoes:')
        print('1) Incluir cliente')
        print('2) Alterar cliente')
        print('3) Listar cliente')
        print('4) Excluir cliente')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
   
    def pega_dados_cliente_cnpj(self):
        print('-----Dados para cliente cnpj-----')
        nome = input('Nome: ')
        celular = input('Celular: ')
        email = input('Email: ')
        cnpj = input('Cnpj: ')

        return {'nome':nome, 'celular':celular,
                'email':email, 'cnpj':cnpj}
   
    def seleciona_cliente_cnpj(self):
        cnpj = input('Digite o cnpj do cliente que quer selecionar: ')
        return cnpj

    def mostra_cliente_cnpj(self, cliente):
        print('Nome do(a) cliente: ', cliente.nome)
        print('Celular do(a) cliente: ', cliente.contato.celular)
        print('Email do(a) cliente: ', cliente.contato.email)
        print('Cnpj do(a) cliente: ', cliente.cnpj)
        print('\n')

    def mostra_msg(self, mensagem):
        print(mensagem)

    def espacamento(self):
        print()