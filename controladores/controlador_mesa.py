from telas.tela_mesa import TelaMesa
from mesa import Mesa
from controladores.controlador_conta import ControladorConta
from DAOs.mesa_dao import MesaDAO

class ControladorMesa():

    def __init__(self, controlador_sistema):
        self.__tela_mesa = TelaMesa()
        self.__controlador_conta = ControladorConta(controlador_sistema)
        self.__mesa_DAO = MesaDAO()
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    @property
    def tela_mesa(self):
        return self.__tela_mesa
    
    #metodo para acessar contas pagas do controlador de uma mesa, sem ter que digitar aquela linha gigante
    def contas_pagas(self, mesa) -> list:
        return self.controlador_conta.contas_pagas

    #status: feito, testar   
    def criar_mesa(self) -> bool:
        print('Entrou em criar mesa')
        num_mesas = len(self.__mesa_DAO.get_all())

        print(num_mesas)

        novo_num = num_mesas + 1

        #que bomba é essa meu deus maluco burro da porra
        nova_mesa = Mesa(novo_num)

        print('numero da nova mesa: ', nova_mesa.numero_da_mesa)

        self.__mesa_DAO.add(nova_mesa)

        self.tela_mesa.mostra_msg("mesa criada com sucesso")

    #status: feito
    def excluir_mesa(self):

        self.listar_mesa()

        mesa = self.acha_mesa_by_num()

        if mesa == None:
            return None

        self.__mesa_DAO.remove(mesa.numero_da_mesa)
        self.tela_mesa.mostra_msg('Mesa excluída')

    #status: feito
    def listar_mesa(self):
        print('entrou em listar mesas')
        for mesa in self.__mesa_DAO.get_all():
            self.tela_mesa.mostra_mesa(mesa)

    #status: feito
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_mesa.tela_opcoes()

                if 0 < op and op <= 4:
                    continua = False
                    self.abre_tela_inicial()
                #if op == 1:
                    #self.criar_mesa()
                #elif op == 2:
                    #self.listar_mesa()
                #elif op == 3:
                    #self.abre_opcoes_alteracoes()
                #elif op == 4:
                    #self.excluir_mesa()
                elif op == 0 or botao == 'Cancelar':
                    continua = False
        
            except:
                self.tela_mesa.mostra_msg("Selecione uma opção ou retorne")

    #status: feito
    def abre_opcoes_alteracoes(self):
        #input seleção de mesa
        mesa = self.acha_mesa_by_num()
        #se a mesa não existir, retorna vazio
        if mesa == None:
            return None
        else:
            continua = True
            while continua:
                try:
                    op, botao = self.tela_mesa.tela_opcoes_alteraçoes(mesa)

                    if op == 1:
                        #altera garçon da mesa mesmo que nulo e encerra o anterior
                        self.alterar_garçon(mesa)
                    elif op == 2:
                        #abre controlador da mesa
                        self.controlador_conta.abre_tela_inicial()
                    elif op == 3:
                        #encerra turno de garçon na mesa
                        self.encerrar_turno_garçon(mesa)
                    elif op == 0 or botao == 'Cancelar':
                        continua = False
                    
                except:
                    self.tela_mesa.mostra_msg("Selecione uma opção ou retorne")

    #status: feito
    def acha_mesa_by_num(self):

        num, botao = self.tela_mesa.seleciona_mesa()

        if botao == 'Cancelar':
            return None

        try:
            int(num)
        except:
            self.tela_mesa.mostra_msg('Digite apenas números')
            return None
        
        numero_int = int(num)

        print('proxima coisa é procurar')

        for mesa in self.__mesa_DAO.get_all():
                if mesa.numero_da_mesa == numero_int:
                    print('Achou a mesa')
                    return mesa
        
        self.tela_mesa.mostra_msg('Não existe uma mesa com este número')
        return None
                
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


