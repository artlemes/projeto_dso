from tela_sistema import TelaSistema
from controlador_produto import ControladorProduto
from controlador_cliente import ControladorCliente
from controlador_contato import ControladorContato
from controlador_garçon import ControladorGarçon
from controlador_mesa import ControladorMesa

class ControladorSistema:

    def __init__(self):
        self.__controlador_produto = ControladorProduto()
        self.__controlador_contato = ControladorContato()
        self.__controlador_garçon = ControladorGarçon(self)
        self.__controlador_mesa = ControladorMesa(self)
        self.__controlador_cliente = ControladorCliente(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_produto(self):
        return self.__controlador_produto
    
    @property
    def controlador_mesa(self):
        return self.__controlador_mesa
    
    @property
    def controlador_contato(self):
        return self.__controlador_contato
    
    @property
    def controlador_garçon(self):
        return self.__controlador_garçon
    
    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
    
    def iniciar_sistema(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.__tela_sistema.tela_opcoes()

                if op == 1:
                    self.controlador_produto.abre_tela_inicial()
    
                elif op == 2:
                    self.controlador_contato.abre_tela_inicial()
    
                elif op == 3:
                    self.controlador_garçon.abre_tela_inicial()
    
                elif op == 4:
                    self.__controlador_mesa.abre_tela_inicial()

                elif op == 5:
                    self.__controlador_cliente.abre_tela_inicial()
            
                elif op == 0 or botao == 'Cancelar':
                    continua = False
            except:
                self.__tela_sistema.mostra_msg('Selecione uma opção ou desligue o sistema')
    
            
            
