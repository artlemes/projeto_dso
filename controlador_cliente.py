from controlador_cliente_cnpj import ControladorClienteCnpj
from controlador_cliente_cpf import ControladorClienteCpf
from tela_cliente import TelaCliente
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
    
    def clientes(self) -> list:
        clientes = []
        for cliente_cnpj in self.controlador_cliente_cnpj.cliente_cnpj:
            clientes.append(cliente_cnpj)
        for cliente_cpf in self.controlador_cliente_cpf.cliente_cpf:
            clientes.append(cliente_cpf)
        return clientes

    @property
    def tela_cliente(self):
        return self.__tela_cliente
    
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_cliente.tela_opcoes())

            except:
                self.tela_cliente.mostra_msg("opção não é um inteiro")
                op = None
            
            if op == 1:
                self.controlador_cliente_cnpj.abre_tela_inicial()
            
            elif op == 2:
                self.controlador_cliente_cpf.abre_tela_inicial()
            
            elif op == 0:
                continua = False

            else:
                self.tela_cliente.mostra_msg("opção inválida")