from telas.tela_conta import TelaConta
from conta import Conta
from prato import Prato
from bebida import Bebida

class ControladorConta():
    def __init__(self, controlador_sistema):
        self.__tela_conta = TelaConta()
        self.__contas_pagas = []
        self.__contas = []
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    @property
    def tela_conta(self):
        return self.__tela_conta
    
    @property
    def contas(self):
        return self.__contas
    
    @property
    def contas_pagas(self):
        return self.__contas_pagas
    
    def criar_conta(self):
        try:
            cod = int(self.tela_conta.pedir_dado("codigo da conta nova: "))
        except:
            print("dado recebido não foi um inteiro")
            return
        for conta in self.contas:
            if conta.codigo_conta == cod:
                print("codigo já existente em contas ativas")
                return
        for conta in self.contas_pagas:
            if conta.codigo_conta == cod:
                print("codigo já existente em contas pagas")
                return
        return self.contas.append(Conta(cod))

    def listar_contas_ativas(self):
        for conta in self.contas:
            self.tela_conta.mostra_conta(conta)

    def selecionar_conta_ativa(self, cod: int) -> Conta:
            
        for conta in self.contas:
            if conta.codigo_conta == cod:
                return conta
        
        self.tela_conta.mostra_msg("código inválido")
        return None
        

    def adicionar_produto(self, conta: Conta):
        continua = True
        while continua:

            try:
                op = int(self.tela_conta.mostra_opcoes_produto())

            except:
                self.tela_conta.mostra_msg("opção inválida")

            if op == 1:
                self.controlador_sistema.controlador_produto.controlador_pratos.lista_prato()
                prato = self.controlador_sistema.controlador_produto.controlador_pratos.acha_prato_by_cod()
                conta.produtos.append(prato)

            if op == 2:
                self.controlador_sistema.controlador_produto.controlador_bebidas.lista_bebida()
                bebida = self.controlador_sistema.controlador_produto.controlador_bebidas.acha_bebida_by_cod()
                conta.produtos.append(bebida)

            if op == 0:
                continua = False
    
    def listar_produtos(self, conta: Conta):
        for produto in conta.produtos:
            if isinstance(produto, Prato):
                self.controlador_sistema.controlador_produto.\
                    controlador_pratos.tela_prato.mostra_prato({"nome": produto.nome,
                                                                "preco": produto.preco,
                                                                "despesa": produto.despesa,
                                                                "codigo": produto.codigo})

            if isinstance(produto, Bebida):
                self.controlador_sistema.controlador_produto.\
                    controlador_bebidas.tela_bebida.mostra_bebida({"nome": produto.nome,
                                                                   "preco": produto.preco,
                                                                   "despesa": produto.despesa,
                                                                   "codigo": produto.codigo})
   
    def remover_produto(self, conta: Conta):
        self.listar_produtos(conta)
        continua = True
        while continua:
            try:
                op = int(self.tela_conta.mostra_opcoes_produto())

            except:
                self.tela_conta.mostra_msg("opção inválida")

            if op == 1:
                prato = self.controlador_sistema.controlador_produto.controlador_pratos.acha_prato_by_cod()
                conta.produtos.remove(prato)

            if op == 2:
                self.listar_produtos
                bebida = self.controlador_sistema.controlador_produto.controlador_bebidas.acha_bebida_by_cod()
                conta.produtos.remove(bebida)

            if op == 0:
                continua = False

    def pagar_conta(self, conta: Conta):
        if self.tela_conta.pedir_dado("tem certeza que deseja fechar está conta - s|n: ") in ["s","S"]:

            cadastro = self.tela_conta.pedir_dado("O cliente tem cadastro? - s|n: ")

            if cadastro in ['s', 'S']:
                
                #a busca funciona
                cliente = self.acha_cliente()

                #funciona
                if cliente is not None:
                    conta.cliente = cliente
                else:
                    self.tela_conta.mostra_msg("Cliente não encontrado")
                    return False

            try:
                self.contas_pagas.append(conta)
                self.contas.remove(conta)
                conta.pago = True
                self.tela_conta.mostra_msg("fechamento bem sucedido")
                return True
            
            except:
                self.tela_conta.mostra_msg("ocorreu um erro inesperado")
                return False
            
    #essa funcao acha o cliente independente se é cpf ou cnpj
    def acha_cliente(self):

        cod_cliente = self.tela_conta.seleciona_cliente()

        for cliente in self.controlador_sistema.controlador_cliente.controlador_cliente_cpf.clientes_cpf:
            if cliente.cpf == cod_cliente:
                return cliente
            
        for cliente in self.controlador_sistema.controlador_cliente.controlador_cliente_cnpj.clientes_cnpj:
            if cliente.cnpj == cod_cliente:
                return cliente
        
        return None

    def listar_contas_pagas(self):
        for conta in self.contas_pagas:
            self.tela_conta.mostra_conta(conta)

    def deletar_conta_ativa(self):
        self.listar_contas_ativas()
        try:
            cod = int(self.tela_conta.pedir_dado("digite o codigo da conta que deseja deletar: "))
            conta = self.selecionar_conta_ativa(cod)

            if conta == None:
                self.tela_conta.mostra_msg("codigo inexistentee")

            else:
                self.contas.remove(conta)

        except:
            self.tela_conta.mostra_msg("dado coletado não foi um inteiro")

    #status: feito
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_conta.tela_opcoes_gerais())
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
                elif op == 0:
                    continua = False
                else: 
                    self.tela_conta.mostra_msg("opção inválida")
            except:
                self.tela_conta.mostra_msg("opção não é um inteiro")
                op = None
    
    def mexer_contas_ativas(self) -> any:
        #selecionar conta
        try:
            self.listar_contas_ativas()
            cod = int(self.tela_conta.pedir_dado("selecione a conta com que você quer mexer: "))
            selecionada = self.selecionar_conta_ativa(cod)
        except:
            self.tela_conta.mostra_msg("opção inválida")
            return
        if selecionada == None:
            self.tela_conta.mostra_msg("conta inexistente")
        else:
            continua = True
            while continua:
                try:
                    op = int(self.tela_conta.tela_opcoes_conta())

                    if op == 1:
                        self.adicionar_produto(selecionada)
                    elif op == 2:
                        self.remover_produto(selecionada)
                    elif op == 3:
                        self.listar_produtos(selecionada)
                    elif op == 4:
                        if self.pagar_conta(selecionada):
                            continua = False
                    elif op == 0:
                        continua = False
                    else:
                        self.tela_conta.mostra_msg("opção inexistente")

                except:
                    self.tela_conta.mostra_msg("opção não é um inteiro")
