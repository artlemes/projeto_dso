from conta import Conta
from bebida import Bebida
from prato import Prato

class TelaConta():
    def __init__(self):
        pass

    def tela_opcoes_gerais(self) -> any:
        print('-----Conta-----')
        print('Opcoes:')
        print('1) Criar conta')
        print('2) Listar contas ativas')
        print('3) Deletar conta ativa') 
        print('4) Interagir com conta ativa')
        print('5) Mostrar contas pagas')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    def tela_opcoes_conta(self) -> any:
        print('1) Adicionar um produto') #listar os produtos disponiveis antes de adicionar
        print('2) Remover um produto')
        print('3) Listar produtos da conta')
        print('4) Pagar a conta')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    def mostra_opcoes_produto(self) -> any:
        print('1) prato')
        print('2) bebida')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    def mostra_produto(self, dados_produto, produto):

        if isinstance(produto, Prato):
            print('Nome do prato: ', {dados_produto['nome']})
            print('Preço do prato: ', {dados_produto['preco']})
            print('Despesa do prato: ', {dados_produto['despesa']})
            print('Código do prato: ', {dados_produto['codigo']})
            print('\n')

        elif isinstance(produto, Bebida):
            print('Nome da bebida: ', {dados_produto['nome']})
            print('Preço da bebida: ', {dados_produto['preco']})
            print('Despesa da bebida: ', {dados_produto['despesa']})
            print('Código da bebida: ', {dados_produto['codigo']})
            print('\n')
    
    def mostra_conta(self, conta: Conta):
        print('Código da conta:', {conta.codigo_conta})
        print('status de pagamento:', {conta.pago})
        print('Valor total: ', {conta.valor_total})
        print('Despesas totais: ', {conta.despesa_total})

        if conta.cliente is not None:
            print('Cliente: ', conta.cliente.nome)

        else:
            print('Cliente: Não registrado')
        print('\n')

    def pedir_dado(self, mensagem: str = "") -> any:
        return input(mensagem)
    
    def seleciona_cliente(self):
        cod = input('Digite o cpf ou cnpj do cliente: ')
        return cod
    
    def mostra_msg(self, msg):
        print(msg)

    
    