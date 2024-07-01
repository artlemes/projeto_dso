import PySimpleGUI as sg
from conta import Conta
from mesa import Mesa


class TelaMesa():
    def __init__(self):
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
            [sg.Text('-------- MESA ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar mesa', "RD1", key='1')],
            [sg.Radio('Listar mesas', "RD1", key='2')],
            [sg.Radio('Interação mesa', "RD1", key='3')],
            [sg.Radio('Excluir mesa', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de mesas').Layout(layout)

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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button
    
    def init_opcoes_alteraçoes(self, mesa):
        sg.ChangeLookAndFeel('DarkTeal4')

        print('Chegou até o menu alterações')

        num_contas = len(mesa.contas)

        if mesa.garçon == None:
            print('identificou que a mesa não tem garçon')
            layout = [
                [sg.Text('-------- Menu alterações ----------', font=("Helvica", 25))],
                [sg.Text('Não possui garçon', font=("Helvica", 15))],
                [sg.Text('número de contas: ',  font=("Helvica", 15)), sg.Text(num_contas)],
                [sg.Radio('Alterar garçon', "RD1", key='1')],
                [sg.Radio('Acessar contas', "RD1", key='2')],
                [sg.Radio('Encerrar turno de garçon', "RD1", key='3')],
                [sg.Radio('Retornar', "RD1", key='0')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de mesas').Layout(layout)
        else:
            layout = [
                [sg.Text('-------- Menu alterações ----------', font=("Helvica", 25))],
                [sg.Text('Garçon: ', key='mesa.garçon.nome', font=("Helvica", 15))],
                [sg.Text('número de contas: ',  font=("Helvica", 15)), sg.Text(num_contas)],
                [sg.Radio('Alterar garçon', "RD1", key='1')],
                [sg.Radio('Acessar contas', "RD1", key='2')],
                [sg.Radio('Encerrar turno de garçon', "RD1", key='3')],
                [sg.Radio('Retornar', "RD1", key='0')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Sistema de mesas').Layout(layout)

    def tela_opcoes_alteraçoes(self, mesa) -> any:
        self.init_opcoes_alteraçoes(mesa)
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button

    def mostra_mesa(self, mesa):
        string_dados = 'Número da mesa: ' + str(mesa.numero_da_mesa) + '\n'

        if mesa.garçon == None:
            string_dados = string_dados + 'A mesa ainda não possui garçon\n'
        else:
            string_dados = string_dados + 'Garçon: ' + str(mesa.garçon.nome)

        string_dados = string_dados + "numero de contas: " + str(len(mesa.contas))

        sg.Popup("", string_dados)

    def mostra_msg(self, msg):
        sg.Popup("", msg)

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
    
    def seleciona_conta(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CONTA ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da conta que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='cod')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona conta').Layout(layout)

        button, values = self.open()
        cod = values['cod']
        self.close()
        return cod, button