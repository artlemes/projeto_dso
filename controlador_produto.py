from controlador_bebida import ControladorBebida
from controlador_prato import ControladorPrato
from tela_produto import TelaProduto
from prato import Prato
from bebida import Bebida

class ControladorProduto():
    def __init__(self):
        self.__controlador_bebidas = ControladorBebida()
        self.__controlador_pratos = ControladorPrato()
        self.__tela_produtos = TelaProduto()

    @property
    def controlador_bebidas(self):
        return self.__controlador_bebidas
    
    @property
    def controlador_pratos(self):
        return self.__controlador_pratos
    
    def produtos(self) -> list:
        produtos = []
        for bebida in self.controlador_bebidas.bebidas:
            produtos.append(bebida)
        for prato in self.controlador_pratos.pratos:
            produtos.append(prato)
        return produtos

    @property
    def tela_produtos(self):
        return self.__tela_produtos
    
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_produtos.tela_opcoes()
            
                if op == 1:
                    self.controlador_bebidas.abre_tela_inicial()
            
                elif op == 2:
                    self.controlador_pratos.abre_tela_inicial()
            
                elif op == 0 or botao == 'Cancelar':
                    continua = False

            except:
                self.tela_produtos.mostra_msg('Selecione uma opção ou retorne')
            