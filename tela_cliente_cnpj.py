#tela tudo ok
import PySimpleGUI as sg


class TelaClienteCnpj():
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
            [sg.Text('-------- Cliente cnpj ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir cliente', "RD1", key='1')],
            [sg.Radio('Alterar cliente', "RD1", key='2')],
            [sg.Radio('Listar cliente', "RD1", key='3')],
            [sg.Radio('Excluir cliente', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de clientes cnpj').Layout(layout)

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
   
    def pega_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CLIENTE CNPJ ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Celular:', size=(15, 1)), sg.InputText('', key='celular')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Text('Não use pontos, apenas os números', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de cliente cnpj').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        celular = values['celular']
        email = values['email']
        cnpj = values['cnpj']

        self.close()

        return {'nome':nome, 'celular':celular,
                'email':email, 'cnpj':cnpj}, button
    
    def altera_dados_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Celular:', size=(15, 1)), sg.InputText('', key='celular')],
            [sg.Text('Email:', size=(15, 1)), sg.InputText('', key='email')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de cliente cnpj').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        celular = values['celular']
        email = values['email']

        self.close()

        return {'nome':nome, 'celular':celular,
                'email':email}, button
   
    def seleciona_cliente(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR CLIENTE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o cnpj do cliente que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('CNPJ:', size=(15, 1)), sg.InputText('', key='cnpj')],
            [sg.Text('Não use pontos, apenas os números', font=("Helvica", 15))],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona cliente').Layout(layout)

        button, values = self.open()
        cnpj = values['cnpj']
        self.close()
        return cnpj, button

    def mostra_cliente(self, cliente):

        string_dados_cliente = 'Nome do cliente: ' + str(cliente.nome) + '\n'
        string_dados_cliente = string_dados_cliente + 'Celular do cliente: ' + str(cliente.contato.celular) + '\n'
        string_dados_cliente = string_dados_cliente + 'Email do cliente: ' + str(cliente.contato.email) + '\n'
        string_dados_cliente = string_dados_cliente + 'Cnpj do cliente: ' + str(cliente.cnpj)

        sg.Popup("", string_dados_cliente)

    def mostra_msg(self, msg):
        sg.Popup("", msg)
