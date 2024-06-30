#tela tudo ok
import PySimpleGUI as sg

class TelaBebida():
    def __init__(self) -> None:
        self.__window = None

    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Bebidas ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir bebida', "RD1", key='1')],
            [sg.Radio('Alterar bebida', "RD1", key='2')],
            [sg.Radio('Listar bebida', "RD1", key='3')],
            [sg.Radio('Excluir bebida', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de bebidas').Layout(layout)

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
   
    def pega_dados_bebida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS BEBIDA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Despesas:', size=(15, 1)), sg.InputText('', key='despesa')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de bebidas').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        preco = values['preco']
        despesa = values['despesa']
        codigo = values['cod']

        self.close()

        return {'nome':nome, 'preco':preco,
                'despesa':despesa, 'codigo':codigo}, button
    
    def altera_dados_bebida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- ALTERA DADOS BEBIDA ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Despesas:', size=(15, 1)), sg.InputText('', key='despesa')],
            [sg.Text('Preço:', size=(15, 1)), sg.InputText('', key='preco')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de bebidas').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        preco = values['preco']
        despesa = values['despesa']

        self.close()

        return {'nome':nome, 'preco':preco,
                'despesa':despesa}, button
   
    def seleciona_bebida(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR BEBIDA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código do bebida que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('COD:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona bebida').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod, button

    def mostra_bebida(self, dados):
        string_dados_bebida = 'Nome da bebida: ' + dados['nome'] + '\n'
        string_dados_bebida = string_dados_bebida + 'Preço da bebida: ' + str(dados['preco']) + '\n'
        string_dados_bebida = string_dados_bebida + 'Despesas da bebida: ' + str(dados['despesa']) + '\n'
        string_dados_bebida = string_dados_bebida + 'Código da bebida: ' + str(dados['codigo'])

        sg.Popup("", string_dados_bebida)

    def mostra_msg(self, msg):
        sg.Popup("", msg)
