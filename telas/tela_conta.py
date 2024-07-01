import PySimpleGUI as sg
from conta import Conta
from bebida import Bebida
from prato import Prato

class TelaConta():
    def __init__(self):
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def init_opcoes_gerais(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Contas ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar conta', "RD1", key='1')],
            [sg.Radio('Listar contas ativas', "RD1", key='2')],
            [sg.Radio('Deletar conta ativa', "RD1", key='3')],
            [sg.Radio('Interagir com conta ativa', "RD1", key='4')],
            [sg.Radio('Mostrar contas pagas', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de contas').Layout(layout)

    #funcionando
    def tela_opcoes_gerais(self) -> any:
        self.init_opcoes_gerais()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button
    
    def init_opcoes_conta(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Contas ativas ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar um produto', "RD1", key='1')],
            [sg.Radio('Remover um produto', "RD1", key='2')],
            [sg.Radio('Listar produtos da conta', "RD1", key='3')],
            [sg.Radio('Pagar a conta', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de contas').Layout(layout)

    #funcionando
    def tela_opcoes_conta(self) -> any:
        self.init_opcoes_conta()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button

    def init_opcoes_produtos(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Produtos ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Prato', "RD1", key='1')],
            [sg.Radio('Bebida', "RD1", key='2')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de contas').Layout(layout)

    #funcionando
    def mostra_opcoes_produto(self) -> any:
        self.init_opcoes_produtos()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button
    
    def mostra_produto(self, produto):
        if isinstance(produto, Prato):
            string_dados = 'Nome do prato: ' + produto.nome + '\n'
            string_dados = string_dados + 'Preço do prato: ' + str(produto.preco) + '\n'
            string_dados = string_dados + 'Despesas do prato: ' + str(produto.despesa) + '\n'
            string_dados = string_dados + 'Código do prato: ' + str(produto.codigo)

            sg.Popup("", string_dados)

        elif isinstance(produto, Bebida):
            string_dados = 'Nome da bebida: ' + produto.nome + '\n'
            string_dados = string_dados + 'Preço da bebida: ' + str(produto.preco) + '\n'
            string_dados = string_dados + 'Despesas da bebida: ' + str(produto.despesa) + '\n'
            string_dados = string_dados + 'Código da bebida: ' + str(produto.codigo)

            sg.Popup("", string_dados)
    
    def mostra_conta(self, conta: Conta):
        string_dados = 'Código da conta: ' + str(conta.codigo_conta) + '\n'
        string_dados = string_dados + 'status de pagamento: ' + str(conta.pago) + '\n'
        string_dados = string_dados + 'Valor total: ' + str(conta.valor_total) + '\n'
        string_dados = string_dados + 'Despesas totais: ' + str(conta.despesa_total) + '\n'

        if conta.cliente is not None:
            string_dados = string_dados + 'Cliente: ' + str(conta.cliente.nome)

        else:
            string_dados = string_dados + 'Cliente: Não registrado'

        sg.Popup("", string_dados)

    #ainda tenho que ver se essa função é realmetne util
    def criar_conta(self) -> any:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- CRIAR CONTA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da conta que deseja criar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criar conta').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod, button
    
    def selecionar_conta(self) -> any:
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CONTA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da conta que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Criar conta').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod, button
    
    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o cpf ou cnpj do cliente que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Text('Utilize apenas números', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona cliente').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod, button
    
    def cadastro_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Fechamento da conta ----------', font=("Helvica", 25))],
            [sg.Text('O cliente tem cadastro?', font=("Helvica", 15))],
            [sg.Button('Sim'), sg.Cancel('Não')]
        ]
        self.__window = sg.Window('Sistema de contas').Layout(layout)

        botao = self.open()
        self.close()
        return botao
    
    def mostra_msg(self, msg):
        sg.Popup('', msg)

    
    