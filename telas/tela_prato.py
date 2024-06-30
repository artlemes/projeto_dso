#tela tudo ok
import PySimpleGUI as sg

class TelaPrato():
    def __init__(self) -> None:
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    #funcionando
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Pratos ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir prato', "RD1", key='1')],
            [sg.Radio('Alterar prato', "RD1", key='2')],
            [sg.Radio('Listar prato', "RD1", key='3')],
            [sg.Radio('Excluir prato', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de pratos').Layout(layout)

    #funcionando
    def tela_opcoes(self) -> any:
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button
   
   #testar
    def pega_dados_prato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS PRATO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Despesas:', size=(15, 1)), sg.InputText('', key='despesa')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de pratos').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        preco = values['preco']
        despesa = values['despesa']
        codigo = values['cod']

        self.close()

        return {'nome':nome, 'preco':preco,
                'despesa':despesa, 'codigo':codigo}, button
    
    def altera_dados_prato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS PRATO ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Despesas:', size=(15, 1)), sg.InputText('', key='despesa')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de pratos').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        preco = values['preco']
        despesa = values['despesa']

        self.close()

        return {'nome':nome, 'preco':preco,
                'despesa':despesa}, button
   
   #testar
    def seleciona_prato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR PRATO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do prato que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('COD:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona prato').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod, button

    #nao funciona
    #da pra fazer com popup mas tentei fazer assim e nao deu
    def mostra_prato(self, dados):

        string_dados_prato = 'Nome do prato: ' + dados['nome'] + '\n'
        string_dados_prato = string_dados_prato + 'Preço do prato: ' + str(dados['preco']) + '\n'
        string_dados_prato = string_dados_prato + 'Despesas do prato: ' + str(dados['despesa']) + '\n'
        string_dados_prato = string_dados_prato + 'Código do prato: ' + str(dados['codigo'])

        sg.Popup("", string_dados_prato)

    def mostra_msg(self, msg):
        sg.Popup("", msg)
