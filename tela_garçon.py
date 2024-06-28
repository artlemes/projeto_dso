#tela parece certa

class TelaGarçon():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self) -> any:
        print('-----Garçons-----')
        print('Opcoes:')
        print('1) Incluir garçon')
        print('2) Alterar garçon')
        print('3) Listar garçons')
        print('4) Excluir garçon')
        print('5) Mostrar comissão')
        print('6) zerar comissão')
        print('0) Retornar')
       
        opcao = input('Escolha uma opcao:')
        return opcao
   
    def pega_dados_garçon(self):
        print('-----Dados para garçons-----')
        nome = input('Nome: ')
        celular = input('Celular: ')
        email = input('Email: ')
        cpf = input('Cpf: ')

        return {'nome':nome, 'celular':celular,
                'email':email, 'cpf':cpf}
   
    def seleciona_garçon(self):
        cpf = input('Digite o cpf do garçon que quer selecionar: ')
        return cpf
    
    #terminar
    def seleciona_mesa(self):
        n_mesa = int(input('Digite o numero da mesa que quer selecionar: '))
        return n_mesa

    def mostra_garçon(self, dados, atendendo):
        if not atendendo:
            print('Nome do garçon: ', {dados['nome']})
            print('Celular do garçon: ', {dados['celular']})
            print('Email do garçon: ', {dados['email']})
            print('Cpf do garçon: ', {dados['cpf']})
            print('\n')
        else:
            print('Nome do garçon: ', {dados['nome']})
            print('Celular do garçon: ', {dados['celular']})
            print('Email do garçon: ', {dados['email']})
            print('Cpf do garçon: ', {dados['cpf']})
            self.mostra_mesas(dados['mesas'])
            print('\n')

    def mostra_mesas_atendidas(self, dados):
        print('O garçon está atendendo estas mesas: ', *dados)

    def mostra_msg(self, mensagem):
        print(mensagem)

    def espacamento(self):
        print()

    def mostra_comissao(self, comissao):
        print('A comissao deste Garçon é: ', comissao)