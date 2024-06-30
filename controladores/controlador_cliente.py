from controladores.controlador_cliente_cnpj import ControladorClienteCnpj
from controladores.controlador_cliente_cpf import ControladorClienteCpf
from telas.tela_cliente import TelaCliente
from cliente_cpf import ClienteCpf
from cliente_cnpj import ClienteCnpj

class ControladorCliente():
    def __init__(self, controlador_sistema):
        self.__controlador_cliente_cnpj = ControladorClienteCnpj(controlador_sistema)
        self.__controlador_cliente_cpf = ControladorClienteCpf(controlador_sistema)
        self.__tela_cliente = TelaCliente()

    @property
    def controlador_cliente_cnpj(self):
        return self.__controlador_cliente_cnpj
    
    @property
    def controlador_cliente_cpf(self):
        return self.__controlador_cliente_cpf
    
    @property
    def tela_cliente(self):
        return self.__tela_cliente
    
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_cliente.tela_opcoes()
            
                if op == 1:
                    self.controlador_cliente_cnpj.abre_tela_inicial()
            
                elif op == 2:
                    self.controlador_cliente_cpf.abre_tela_inicial()
            
                elif op == 0 or botao == 'Cancelar':
                    continua = False
            
            except:
                self.tela_cliente.mostra_msg('Selecione uma opção ou retorne')
                op = None