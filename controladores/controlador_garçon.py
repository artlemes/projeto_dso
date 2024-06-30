from garçon import Garçon
from telas.tela_garçon import TelaGarçon
from controladores.controlador_mesa import ControladorMesa
from DAOs.garçon_DAO import GarçonDAO
from DAOs.contato_dao import ContatoDAO


class ControladorGarçon():

    def __init__(self, controlador_sistema):
        self.__tela_garçon = TelaGarçon()
        self.__garçon_DAO = GarçonDAO()
        self.__contato_DAO = ContatoDAO()
    
    @property
    def tela_garçon(self):
        return self.__tela_garçon
    
    #status: funcionando
    def inclui_garçon(self) -> bool:
        garçon_dados, botao = self.tela_garçon.pega_dados_garçon()

        if botao == 'Cancelar':
            return None

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

            for garçon in self.__garçon_DAO.get_all():
                if garçon.cpf == novo.cpf:
                    duplicado = True
            
            if not duplicado:
                self.__garçon_DAO.add(novo)
                self.__contato_DAO.add(novo.contato)
                self.tela_garçon.mostra_msg('Garçon cadastrado com sucesso')
                return True
            
            else:
                self.tela_garçon.mostra_msg('Não foi possivel cadastrar este garçon:')
                self.tela_garçon.mostra_msg('Garçon já existente')
                return False

    #status: funcionando
    def altera_garçon(self):
        #seleção do garçon a ser alterado
        garçon = self.acha_garçon_by_cpf()

        if isinstance(garçon, str):
            return None

        #checagem de garçon nulo
        if garçon == None:
            self.tela_garçon.mostra_msg("Não foi possível alterar este garçon, ele não existe")
            return False

        #captação de dados
        dados_alterados, botao = self.tela_garçon.altera_dados_garçon()

        if botao == 'Cancelar':
            return None

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            garçon.nome = dados_alterados["nome"]
            garçon.contato.celular = dados_alterados["celular"]
            garçon.contato.email = dados_alterados["email"]
            self.__garçon_DAO.update(garçon)
            self.__contato_DAO.update(garçon.contato)
            return True

        else:
            self.tela_garçon.mostra_msg("Não foi possível alterar este garçon")
            self.tela_garçon.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def exclui_garçon(self):

        self.lista_garçon()

        garçon = self.acha_garçon_by_cpf()

        if isinstance(garçon, str):
            return None
        
        if garçon == None:
            self.tela_garçon.mostra_msg('Garçon não encontrado')
            return False

        self.__garçon_DAO.remove(garçon.cpf)
        self.__contato_DAO.remove(garçon.contato)
        self.tela_garçon.mostra_msg('garçon excluido')
        return True
       
    #status: feito, testar
    def lista_garçon(self):
        for garçon in self.__garçon_DAO.get_all():
            if len(garçon.mesas) == 0:
                self.tela_garçon.mostra_garçon({"nome": garçon.nome, 
                                                "celular": garçon.contato.celular,
                                                "email": garçon.contato.email,
                                                "cpf": garçon.cpf},False)
            else:
                mesas = self.num_mesas(garçon)
                self.tela_garçon.mostra_garçon({"nome": garçon.nome, 
                                                "celular": garçon.contato.celular,
                                                "email": garçon.contato.email,
                                                "cpf": garçon.cpf,
                                                'mesas': mesas},True)

    #status: funcionando
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_garçon.tela_opcoes()

                if op == 1:
                    self.inclui_garçon()

                elif op == 2:
                    self.altera_garçon()

                elif op == 3:
                    self.lista_garçon()

                elif op == 4:
                    self.exclui_garçon()

                elif op == 5:
                    self.mostrar_comissao()
            
                elif op == 6:
                    self.zera_comissao()

                elif op == 0 or botao == 'Cancelar':
                    continua = False
                
            except:
                self.tela_garçon.mostra_msg("Selecione uma opção ou retorne")
                op = None

    #status: ainda nao da pra testar, precisamos da conta e da mesa funcionando
    def mostrar_comissao(self):
        garçon = self.acha_garçon_by_cpf()

        if isinstance(garçon, str):
            return None

        if garçon != None:
            self.tela_garçon.mostra_comissao(garçon.comissao)
            return True
        else:
            self.tela_garçon.mostra_msg("garçon não encontrado")
            return False

            
    def zera_comissao(self):

        garçon = self.acha_garçon_by_cpf()

        if isinstance(garçon, str):
            return None
        
        if garçon != None:
            garçon.lista_de_comissao = []
            self.tela_garçon.mostra_msg("comissão zerada com sucesso")
            return True
        else:
            return False

    #status: ainda nao da pra testar, precisamos da conta e da mesa funcionando
    def num_mesas(self, garçon):
        dados = []

        for mesa in garçon.mesas:
            dados.append(mesa.numero_da_mesa)

        return dados

    #status: funcionando
    def acha_garçon_by_cpf(self):
        #input de código
        ok = False
        while not ok:

            cpf, botao = self.tela_garçon.seleciona_garçon()

            if botao == 'Cancelar':
                return botao
            
            try:
                int(cpf)
                str(cpf)
                ok = True
            except:
                self.tela_garçon.mostra_msg("O cpf deve conter apenas números")
        
        for garçon in self.__garçon_DAO.get_all():
            if garçon.cpf == cpf:
                self.tela_garçon.mostra_msg("garçon encontrado")
                return garçon
        
        self.tela_garçon.mostra_msg('Garçon não encontrado')
        return None

    #status: feito, testar
    #se der certo retorna true, se der errado false
    def testador_variaveis(self, dados) -> dict:
        if len(dados) == 4:
            if len(dados['cpf']) != 11 or dados['nome'] == '' or dados['celular'] == '' or dados['email'] == '':
                self.tela_garçon.mostra_msg("É necessário preencher todos os campos")
                return False
            else:
                try:
                    int(dados['cpf'])
                    int(dados['celular'])
                except:
                    self.tela_garçon.mostra_msg('Celular e cpf devem conter apenas números')
                    return False
                return True
        else:
            if dados['nome'] == '' or dados['celular'] == '' or dados['email'] == '':
                self.tela_garçon.mostra_msg("É necessário preencher todos os campos")
                return False
            else:
                return True
