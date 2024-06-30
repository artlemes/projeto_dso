#tela parece certa
import PySimpleGUI as sg


class TelaGarçon():
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
            [sg.Text('-------- Garçons ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir garçon', "RD1", key='1')],
            [sg.Radio('Alterar garçon', "RD1", key='2')],
            [sg.Radio('Listar garçons', "RD1", key='3')],
            [sg.Radio('Excluir garçon', "RD1", key='4')],
            [sg.Radio('Mostrar comissão', "RD1", key='5')],
            [sg.Radio('Zerar comissão', "RD1", key='6')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de garçons').Layout(layout)

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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button
   
    def pega_dados_garçon(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS GARÇON ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Celular:', size=(15, 1)), sg.InputText('', key='celular')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Não use pontos, apenas os números', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de garçons').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        celular = values['celular']
        email = values['email']
        cpf = values['cpf']

        self.close()

        return {'nome':nome, 'celular':celular,
                'email':email, 'cpf':cpf}, button
    
    def altera_dados_garçon(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS GARÇON ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Celular:', size=(15, 1)), sg.InputText('', key='celular')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de garçons').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        celular = values['celular']
        email = values['email']

        self.close()

        return {'nome':nome, 'celular':celular,
                'email':email}, button
   
    def seleciona_garçon(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR GARÇON ----------', font=("Helvica", 25))],
            [sg.Text('Digite o cpf do garçon que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Não use pontos, apenas os números', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona garçon').Layout(layout)

        button, values = self.open()
        cpf = values['cpf']
        self.close()
        return cpf, button
    
    #terminar
    def seleciona_mesa(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR MESA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o número da mesa que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='num')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona mesa').Layout(layout)

        button, values = self.open()
        num = values['num']
        self.close()
        return num, button

    def mostra_garçon(self, dados, atendendo):

        string_dados = 'Nome do garçon: ' + str(dados['nome']) + '\n'
        string_dados = string_dados + 'Celular do garçon: ' + str(dados['celular']) + '\n'
        string_dados = string_dados + 'Email do garçon: ' + str(dados['email']) + '\n'
        string_dados = string_dados + 'CPF do garçon: ' + str(dados['cpf'])

        if atendendo:
            mesas = dados['mesas']
            string_dados = string_dados + 'O garçon está atendendo estas mesas: ' + str(mesas)

        sg.Popup("", string_dados)


    def mostra_msg(self, mensagem):
        sg.Popup("", mensagem)

    def mostra_comissao(self, comissao):
        sg.Popup("A comissão desse garçon é: ", comissao)