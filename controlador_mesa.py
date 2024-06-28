from tela_mesa import TelaMesa
from mesa import Mesa
from controlador_conta import ControladorConta

class ControladorMesa():

    def __init__(self, controlador_sistema):
        self.__tela_mesa = TelaMesa()
        self.__controlador_sistema = controlador_sistema
        self.__mesas = []

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def mesas(self):
        return self.__mesas

    @property
    def tela_mesa(self):
        return self.__tela_mesa
    
    #metodo para acessar contas pagas do controlador de uma mesa, sem ter que digitar aquela linha gigante
    def contas_pagas(self, mesa) -> list:
        return mesa.controlador_conta.contas_pagas

    #status: feito, testar   
    def criar_mesa(self) -> bool:
        num_mesas = len(self.mesas)

        nova_mesa = Mesa(num_mesas + 1, ControladorConta(self.controlador_sistema))

        self.mesas.append(nova_mesa)

        self.tela_mesa.mostra_msg("mesa criada com sucesso")

    
    #status: feito
    def excluir_mesa(self):
        mesa = self.acha_mesa_by_num()

        if mesa in self.mesas:
            self.mesas.remove(mesa)
            self.tela_mesa.mostra_msg('Mesa excluída')

    #status: feito
    def listar_mesa(self):
        for mesa in self.mesas:
            self.tela_mesa.mostra_mesa(mesa)

    #status: feito
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_mesa.tela_opcoes())
                if op == 1:
                    self.criar_mesa()
                elif op == 2:
                    self.listar_mesa()
                elif op == 3:
                    self.abre_opcoes_alteracoes()
                elif op == 4:
                    self.excluir_mesa()
                elif op == 0:
                    continua = False
                else: 
                    self.tela_mesa.mostra_msg("opção inválida")
            except:
                self.tela_mesa.mostra_msg("opção não é um inteiro")

    #status: feito
    def abre_opcoes_alteracoes(self):
        #input seleção de mesa
        mesa = self.acha_mesa_by_num()
        #se a mesa não existir, retorna vazio
        if mesa == None:
            return
        else:
            continua = True
            while continua:
                try:
                    op = int(self.tela_mesa.tela_opcoes_alteraçoes(mesa))
                    if op == 1:
                        #altera garçon da mesa mesmo que nulo e encerra o anterior
                        self.alterar_garçon(mesa)
                    elif op == 2:
                        #abre controlador da mesa
                        mesa.controlador_conta.abre_tela_inicial()
                    elif op == 3:
                        #encerra turno de garçon na mesa
                        self.encerrar_turno_garçon(mesa)
                    elif op == 0:
                        continua = False
                    else: 
                        self.tela_mesa.mostra_msg("opção inválida")
                except:
                    self.tela_mesa.mostra_msg("opção não é um inteiro")

    #status: feito
    def acha_mesa_by_num(self):
        self.listar_mesa()
        try:
            #recebe input e procura para retornar mesa
            num = int(self.tela_mesa.seleciona_mesa())
            for mesa in self.mesas:
                if mesa.numero_da_mesa == num:
                    return mesa
        except:
            self.tela_mesa.mostra_msg('Não existe uma mesa com este numero')
            return

    def acha_garçon_by_cpf(self):
        #usa controlador sistema para utilizar do controlador de garçons geral para exibir lista de garçons
        self.controlador_sistema.controlador_garçon.lista_garçon()
        #roda função para selecionar garçon seguindo a mesma lógica e retorna instancia da classe garçon escolhida
        return self.controlador_sistema.controlador_garçon.acha_garçon_by_cpf()

    #status: feito, testar
    def alterar_garçon(self, mesa):
        #escolhe novo garçon
        garçon_escolhido = self.acha_garçon_by_cpf()
        #se já tiver um garçon na mesa, encerra sua comissão
        if mesa.garçon != None:
            mesa.garçon.lista_de_comissao += self.contas_pagas(mesa)
        #set garçon da mesa para escolhido
        mesa.garçon = garçon_escolhido
        #adiciona ao registro da mesa todas as contas pagas no serviço do garçon anterior
        mesa.registro = mesa.registro + self.contas_pagas(mesa)
        #zera a lista de contas pagas no serviço do garçon para ser reutilizada
        mesa.controlador_conta.contas_pagas = []
    
    def encerrar_turno_garçon(self, mesa):
        if mesa.garçon != None:
            #adiciona contas pagas a lista de comissão do garçon
            mesa.garçon.lista_de_comissao += self.contas_pagas(mesa)
            #retira ele da mesa atual
            mesa.garçon = None


