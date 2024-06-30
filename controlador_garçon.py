from garçon import Garçon
from telas.tela_garçon import TelaGarçon
from controlador_mesa import ControladorMesa


class ControladorGarçon():

    def __init__(self, controlador_sistema):
        self.__tela_garçon = TelaGarçon()
        self.__garçons = []
        self.__controlador_sistema = controlador_sistema

    @property
    def garçons(self):
        return self.__garçons
    
    @property
    def tela_garçon(self):
        return self.__tela_garçon

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema
    
    #status: funcionando
    def inclui_garçon(self) -> bool:
        garçon_dados = self.tela_garçon.pega_dados_garçon()

        certo = self.testador_variaveis(garçon_dados)

        if not certo:
            self.tela_garçon.mostra_msg('Não foi possivel cadastrar este garçon:')
            self.tela_garçon.mostra_msg('parâmetros inválidos')
        else:

            duplicado = False

            novo = Garçon(garçon_dados["nome"], 
                         garçon_dados["celular"], 
                         garçon_dados["email"], 
                         garçon_dados["cpf"])

            for garçon in self.garçons:
                if garçon.cpf == novo.cpf:
                    duplicado = True
            
            if not duplicado:
                self.garçons.append(novo)
                self.controlador_sistema.controlador_contato.contatos.append(novo.contato)
                return True
            
            else:
                self.tela_garçon.mostra_msg('Não foi possivel cadastrar este garçon:')
                self.tela_garçon.mostra_msg('Garçon já existente')
                return False

    #status: funcionando
    def altera_garçon(self):
        #seleção do garçon a ser alterado
        garçon = self.acha_garçon_by_cpf()

        #checagem de garçon nulo
        if garçon == None:
            self.tela_garçon.mostra_msg("Não foi possível alterar este garçon, ele não existe")
            return False

        #captação de dados
        dados_alterados = self.tela_garçon.pega_dados_garçon()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            garçon.nome = dados_alterados["nome"]
            garçon.contato.celular = dados_alterados["celular"]
            garçon.contato.email = dados_alterados["email"]
            garçon.cpf = dados_alterados["cpf"]  
            return True

        else:
            self.tela_garçon.mostra_msg("Não foi possível alterar este garçon")
            self.tela_garçon.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def exclui_garçon(self):
        try:
            self.lista_garçon()
            garçon = self.acha_garçon_by_cpf()
            self.garçons.remove(garçon)
            self.controlador_sistema.controlador_contato.contatos.remove(garçon.contato)
            self.tela_garçon.mostra_msg('garçon excluido')
        except:
            self.tela_garçon.mostra_msg('não foi possível encontrar o garçon')

    #status: feito, testar
    def lista_garçon(self):
        for garçon in self.garçons:
            self.tela_garçon.mostra_garçon({"nome": garçon.nome, 
                                            "celular": garçon.contato.celular,
                                            "email": garçon.contato.email,
                                            "cpf": garçon.cpf},False)

    #status: funcionando
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_garçon.tela_opcoes())

            except:
                self.tela_garçon.mostra_msg("opção não é um inteiro")
                op =None

            if op == 1:
                self.inclui_garçon()

            elif op == 2:
                self.altera_garçon()

            elif op == 3:
                self.tela_garçon.espacamento()
                self.lista_garçon()

            elif op == 4:
                self.exclui_garçon()

            elif op == 5:
                self.mostrar_comissao()
            
            elif op == 6:
                self.zera_comissao()

            elif op == 0:
                continua = False
                
            else: 
                self.tela_garçon.mostra_msg("opção inválida")

    #status: ainda nao da pra testar, precisamos da conta e da mesa funcionando
    def mostrar_comissao(self):
        garçon = self.acha_garçon_by_cpf()
        if garçon != None:
            self.tela_garçon.mostra_comissao(garçon.comissao)
        else:
            self.tela_garçon.mostra_msg("garçon não encontrado")
            
    def zera_comissao(self):
        garçon = self.acha_garçon_by_cpf()
        if garçon != None:
            garçon.lista_de_comissao = []
            self.tela_garçon.mostra_msg("comissão zerada com sucesso")
        else:
            self.tela_garçon.mostra_msg("garçon não encontrado")

    #status: ainda nao da pra testar, precisamos da conta e da mesa funcionando
    def mostra_mesas(self, garçon):
        dados = []

        for mesa in garçon.mesas:
            dados.append(mesa.numero_da_mesa)

        self.tela_garçon.mostra_mesas_atendidas(dados)

    #status: funcionando
    def acha_garçon_by_cpf(self):
        #input de código
        ok = False
        while not ok:
            try:
                cpf = str(self.tela_garçon.seleciona_garçon())
                ok = True
            except:
                self.tela_garçon.mostra_msg("O cpf deve ser uma string registrada\n")
        
        for garçon in self.garçons:
            if garçon.cpf == cpf:
                self.tela_garçon.mostra_msg("garçon encontrado")
                return garçon

    #status: feito, testar
    #se der certo retorna true, se der errado false
    def testador_variaveis(self, garçon_dados) -> dict:
        try:
            garçon_dados_checados = {"nome":str(garçon_dados["nome"]),
                                    "celular": str(garçon_dados["celular"]),
                                    "email":str(garçon_dados["email"]),
                                    "cpf":str(garçon_dados["cpf"])}
            return True
        
        except:
            return False
        
    #status: feito, só da pra testar quando a mesa e a conta tiverem prontas
