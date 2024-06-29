#tela tudo ok
import PySimpleGUI as sg


class TelaContato():
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
            [sg.Text('-------- Contatos ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir contato', "RD1", key='1')],
            [sg.Radio('Alterar contato', "RD1", key='2')],
            [sg.Radio('Listar contatos', "RD1", key='3')],
            [sg.Radio('Excluir contato', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de contatos').Layout(layout)

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
        print(opcao)
        return opcao, button
    
    def pega_dados_contato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CONTATO ----------', font=("Helvica", 25))],
            [sg.Text('Numero:', size=(15, 1)), sg.InputText('', key='celular')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('OBS: o numero deve seguir o padrao "99 99999-9999"', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de contatos').Layout(layout)

        button, values = self.open()
        celular = values['celular']
        email = values['email']
        print(f'numero: "{celular}", email: "{email}"')

        self.close()

        return {'celular':celular, 'email':email}, button
   
   
    def seleciona_contato(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CONTATO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o número do contato que deseja selecionar', font=("Helvica", 15))],
            [sg.Text('Número:', size=(15, 1)), sg.InputText('', key='num')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona contato').Layout(layout)

        button, values = self.open()
        num = values['num']
        self.close()
        return num, button

    def mostra_contato(self, dados):
        string_dados_contato = 'Número do contato: ' + str(dados['celular']) + '\n'
        string_dados_contato = string_dados_contato + 'Email do contato: ' + str(dados['email']) + '\n'

        sg.Popup("", string_dados_contato)

    def mostra_msg(self, mensagem):
        sg.Popup("", mensagem)

