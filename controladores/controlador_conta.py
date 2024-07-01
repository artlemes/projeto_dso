from telas.tela_conta import TelaConta
from conta import Conta
from prato import Prato
from bebida import Bebida
from DAOs.conta_dao import ContaDAO

class ControladorConta():
    def __init__(self, controlador_sistema):
        self.__tela_conta = TelaConta()
        self.__conta_DAO = ContaDAO()
        self.__contas_ativas = []
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_conta(self):
        return self.__tela_conta
    
    @property
    def contas_ativas(self):
        return self.__contas_ativas
    
    def criar_conta(self):

        cod, botao = self.tela_conta.criar_conta()

        if botao == 'Cancelar':
            return None

        try:
            int(cod)
        except:
            self.tela_conta.mostra_msg("Código recebido não é um inteiro")
            return None
        
        cod_int = int(cod)
        
        #testando se o codigo está em uma conta ativa
        for conta in self.contas:
            if conta.codigo_conta == cod_int:
                print("codigo já existente em contas ativas")
                return None

        #testando se o codigo está em uma conta paga
        for conta in self.__conta_DAO.get_all():
            if conta.codigo_conta == cod_int:
                print("codigo já existente em contas pagas")
                return None
            
        self.contas.append(Conta(cod_int))
        return True

    def listar_contas_ativas(self):
        for conta in self.contas:
            self.tela_conta.mostra_conta(conta)


    def encontrar_conta_ativa(self) -> Conta:

        cod, botao = self.tela_conta.selecionar_conta()

        if botao == 'Cancelar':
            return None

        try:
            int(cod)
        except:
            self.tela_conta.mostra_msg('Código não é um inteiro')

        cod_int = int(cod)
            
        for conta in self.contas:
            if conta.codigo_conta == cod_int:
                return conta
        
        self.tela_conta.mostra_msg("código inválido")
        return None
        

    def adicionar_produto(self, conta: Conta):
        continua = True
        while continua:

            op, botao = self.tela_conta.mostra_opcoes_produto()

            try:
                if op == 1:
                    self.controlador_sistema.controlador_produto.controlador_pratos.lista_prato()
                    prato = self.controlador_sistema.controlador_produto.controlador_pratos.acha_prato_by_cod()
                    conta.produtos.append(prato)

                if op == 2:
                    self.controlador_sistema.controlador_produto.controlador_bebidas.lista_bebida()
                    bebida = self.controlador_sistema.controlador_produto.controlador_bebidas.acha_bebida_by_cod()
                    conta.produtos.append(bebida)

                if op == 0 or botao == 'Cancelar':
                    continua = False

            except:
                self.tela_conta.mostra_msg("Selecione uma opção ou retorne")
    
    def listar_produtos(self, conta: Conta):

        for produto in conta.produtos:
            self.tela_conta.mostra_produto(produto)
   
    def remover_produto(self, conta: Conta):

        self.listar_produtos(conta)

        continua = True
        while continua:

            op, botao = self.tela_conta.mostra_opcoes_produto()

            try:

                if op == 1:
                    prato = self.controlador_sistema.controlador_produto.controlador_pratos.acha_prato_by_cod()
                    conta.produtos.remove(prato)

                if op == 2:
                    self.listar_produtos
                    bebida = self.controlador_sistema.controlador_produto.controlador_bebidas.acha_bebida_by_cod()
                    conta.produtos.remove(bebida)

                if op == 0 or botao == 'Cancelar':
                    continua = False

            except:
                self.tela_conta.mostra_msg("Selecione algo ou retorne")

    def pagar_conta(self, conta: Conta):
            
            cadastro = self.tela_conta.cadastro_cliente()

            if cadastro == 'Sim':
                
                #a busca funciona
                cliente = self.acha_cliente()

                #funciona
                if cliente is not None:
                    conta.cliente = cliente
                else:
                    self.tela_conta.mostra_msg("Cliente não encontrado")
                    return False

            try:
                self.__conta_DAO.add(conta)
                conta.pago = True
                self.contas.remove(conta)
                self.tela_conta.mostra_msg("fechamento bem sucedido")
                return True
            
            except:
                self.tela_conta.mostra_msg("ocorreu um erro inesperado")
                return False
            
    #essa funcao acha o cliente independente se é cpf ou cnpj
    def acha_cliente(self):

        cod_cliente, botao = self.tela_conta.seleciona_cliente()

        if botao == 'Cancelar':
            return None

        try:
            int(cod_cliente)
        except:
            self.tela_conta.mostra_msg('O código deve conter apenas números')

        cod_str = str(cod_cliente)

        if len(cod_str) == 11:
            for cliente in self.controlador_sistema.controlador_cliente.controlador_cliente_cpf.__cliente_DAO.get_all():
                if cliente.cpf == cod_str:
                    return cliente
        else:
            for cliente in self.controlador_sistema.controlador_cliente.controlador_cliente_cnpj.__cliente_DAO.get_all():
                if cliente.cnpj == cod_str:
                    return cliente
        
        self.tela_conta.mostra_msg('Cliente não tem registro')
        return None

    def listar_contas_pagas(self):
        for conta in self.__conta_DAO.get_all():
            self.tela_conta.mostra_conta(conta)

    def deletar_conta_ativa(self):

        self.listar_contas_ativas()

        cod, botao = self.tela_conta.selecionar_conta()

        if botao == 'Cancelar':
            return None

        try:
            conta = self.encontrar_conta_ativa()

            if conta == None:
                self.tela_conta.mostra_msg("codigo inexistente")

            else:
                self.contas.remove(conta)

        except:
            self.tela_conta.mostra_msg("dado coletado não foi um inteiro")

    #status: feito
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_conta.tela_opcoes_gerais()

                if op == 1:
                    self.criar_conta()
                elif op == 2:
                    self.listar_contas_ativas()
                elif op == 3:
                    self.deletar_conta_ativa()
                elif op == 4:
                    self.mexer_contas_ativas()
                elif op == 5:
                    self.listar_contas_pagas()
                elif op == 0 or botao == 'Cancelar':
                    continua = False
            except:
                self.tela_conta.mostra_msg("Selecione uma opção ou retorne")
                op = None
    
    def mexer_contas_ativas(self) -> any:
        #selecionar conta
        self.listar_contas_ativas()

        selecionada = self.encontrar_conta_ativa()

        if selecionada == None:
            return None
        else:
            continua = True
            while continua:
                try:
                    op, botao = self.tela_conta.tela_opcoes_conta()

                    if op == 1:
                        self.adicionar_produto(selecionada)
                    elif op == 2:
                        self.remover_produto(selecionada)
                    elif op == 3:
                        self.listar_produtos(selecionada)
                    elif op == 4:
                        self.pagar_conta(selecionada)
                    elif op == 0 or botao == 'Cancelar':
                        continua = False

                except:
                    self.tela_conta.mostra_msg("Selecione uma opção ou retorne")
