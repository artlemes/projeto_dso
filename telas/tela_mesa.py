from conta import Conta


class TelaMesa():
    def __init__(self):
        pass

    def tela_opcoes(self) -> any:
        print('-----Mesa-----')
        print('Opcoes:')
        print('1) Criar mesa')
        print('2) Listar mesas')
        print('3) Interação mesa') 
        print('4) Excluir mesa')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    def tela_opcoes_alteraçoes(self, mesa):
        print('---Menu interaçoes---')
        if mesa.garçon == None:
            print("Garçon: ", {mesa.garçon})
        else: 
            print("Garçon: ", {mesa.garçon.nome})

        print("numero de contas: ", {len(mesa.contas)})
        print('Opcoes:')
        print('1) Alterar garçon')
        print('2) Acessar contas') #abre tela controlador de contas mesa
        print('3) Encerrar turno de garçon')
        print('0) Retornar')
        print("")
        opcao = input('Escolha uma opcao: ')
        return opcao

    def mostra_mesa(self, mesa):
        print('Número da mesa: ', mesa.numero_da_mesa)
        if mesa.garçon == None:
            print("garçon: ", mesa.garçon)
        else:
            print("garçon: ", mesa.garçon.nome)
        print("numero de contas: ", len(mesa.contas))
        print('\n')

    def mostra_msg(self, msg):
        print(msg)

    def espacamento(self):
        print('\n')

    def seleciona_mesa(self):
        n_mesa = input('Digite o numero da mesa que quer selecionar: ')
        return n_mesa
    
    def cria_mesa(self):
        n_mesa = int(input('Digite o numero da mesa que quer selecionar: '))
        return n_mesa
    
    def seleciona_garçon(self):
        cpf = input('Digite o cpf do garçon que quer selecionar: ')
        return cpf
    
    def seleciona_conta(self):
        cod = int(input('Digite o codigo da conta que quer selecionar: '))

        return cod