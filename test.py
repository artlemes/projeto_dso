import PySimpleGUI as sg

from controlador_sistema import ControladorSistema
c2 = ControladorSistema()

c2.iniciar_sistema()


a = [1,234,5,2,65,3456,242]
b = 'akfjalkdsfj' + a
sg.Popup('lista kldsjaflajsdçlfkjds', b)
