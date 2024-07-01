import PySimpleGUI as sg


class TelaSistema():
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
            [sg.Text('-------- Sistema de cadastro do restaurante ----------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Produtos', "RD1", key='1')],
            [sg.Radio('Contatos', "RD1", key='2')],
            [sg.Radio('Garçons', "RD1", key='3')],
            [sg.Radio('Mesas', "RD1", key='4')],
            [sg.Radio('Clientes', "RD1", key='5')],
            [sg.Radio('Contas', "RD1", key='6')],
            [sg.Radio('Desligar o sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de pratos').Layout(layout)

    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
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
    # cobre os casos de Retornar, fechar janela, ou clicar cancelar
    #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao, button
    
    def mostra_msg(self, msg):
        sg.Popup('', msg)
