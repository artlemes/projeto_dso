from cliente_cnpj import ClienteCnpj
from tela_cliente_cnpj import TelaClienteCnpj
from DAOs.cliente_cnpj_dao import ClienteCnpjDAO
from DAOs.contato_dao import ContatoDAO

class ControladorClienteCnpj():
    def __init__(self, controlador_sistema):
        self.__tela_cliente_cnpj = TelaClienteCnpj()
        self.__cliente_DAO = ClienteCnpjDAO()
        self.__contato_DAO = ContatoDAO()

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def clientes_cnpj(self):
        return self.__clientes_cnpj
    
    @property
    def tela_cliente_cnpj(self):
        return self.__tela_cliente_cnpj

    #status: funcionando
    def incluir_cliente_cnpj(self) -> bool:
        dados, botao = self.tela_cliente_cnpj.pega_dados_cliente()

        if botao == 'Cancelar':
            return None

        certo = self.testador_variaveis(dados)

        if not certo:
            self.tela_cliente_cnpj.mostra_msg('Não foi possivel cadastrar esta cliente:')
            self.tela_cliente_cnpj.mostra_msg('parâmetros fora do padrão')

        else:
            duplicado = False

            novo = ClienteCnpj(dados["nome"], 
                         dados["celular"], 
                         dados["email"], 
                         dados["cnpj"])

            for cliente in self.__cliente_DAO.get_all():
                if cliente.cnpj == novo.cnpj:
                    duplicado = True
            
            if not duplicado:
                self.__cliente_DAO.add(novo)
                self.__contato_DAO.add(novo.contato)
                self.tela_cliente_cnpj.mostra_msg("cliente adicionado com sucesso")
                return True
            
            else:
                self.tela_cliente_cnpj.mostra_msg('Não foi possivel cadastrar este cliente:')
                self.tela_cliente_cnpj.mostra_msg('Cnpj já existente')
                return False

    #status: feito, erro, recursao
    def altera_cliente_cnpj(self):

        #seleção do cliente_cnpj a ser alterado
        cliente = self.acha_cliente_by_cnpj()

        if cliente == None:
            return None

        #captação de dados
        dados_alterados, botao = self.tela_cliente_cnpj.altera_dados_cliente()

        if botao == 'Cancelar':
            return None

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)
        print(certo)

        if certo:
            cliente.nome = dados_alterados["nome"]
            cliente.contato.celular = dados_alterados["celular"]
            cliente.contato.email = dados_alterados["email"]
            self.__cliente_DAO.update(cliente)
            self.__contato_DAO.update(cliente.contato)
            return True

        if not certo:
            self.tela_cliente_cnpj.mostra_msg("Não foi possível alterar este cliente")
            self.tela_cliente_cnpj.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def excluir_cliente_cnpj(self):

        self.listar_cliente_cnpj()
        cliente = self.acha_cliente_by_cnpj()

        if cliente == None:
            return None

        if cliente in self.__cliente_DAO.get_all():
            self.__cliente_DAO.remove(cliente.cnpj)
            self.tela_cliente_cnpj.mostra_msg('Cliente excluído')
        else:
            self.tela_cliente_cnpj.mostra_msg("Atenção: cliente inexistente")

    #status: funcionando
    def listar_cliente_cnpj(self):
        for cliente in self.__cliente_DAO.get_all():
            self.tela_cliente_cnpj.mostra_cliente(cliente)

    #status: fazer
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_cliente_cnpj.tela_opcoes()
                print(op, botao)
                print(type(op))

                if op == 1:
                    self.incluir_cliente_cnpj()
                elif op == 2:
                    self.altera_cliente_cnpj()
                elif op == 3:
                    self.listar_cliente_cnpj()
                elif op == 4:
                    self.excluir_cliente_cnpj()
                elif op == 0 or botao == 'Cancelar':
                    continua = False
            except:
                self.tela_cliente_cnpj.mostra_msg("Selecione algo ou retorne")
                op = None

    #status: funcionanod
    def acha_cliente_by_cnpj(self):
        #input de código

        cnpj, botao = self.tela_cliente_cnpj.seleciona_cliente()

        if botao == 'Cancelar':
            return None

        for cliente in self.__cliente_DAO.get_all():
            if cliente.cnpj == cnpj:
                return cliente

        self.tela_cliente_cnpj.mostra_msg('Cnpj não encontrado, tente novamente')
        return None

    #status: funcionando?
    #serve de algo?
    def testador_variaveis(self, dados) -> bool:
        if len(dados) == 4:
            if len(dados['cnpj']) != 14 or dados['nome'] == '' or dados['celular'] == '' or dados['email'] == '':
                return False
            else:
                try:
                    int(dados['cnpj'])
                    int(dados['celular'])
                except:
                    self.tela_cliente_cnpj.mostra_msg('Celular e CNPJ devem conter apenas números')
                    return False
                return True
        else:
            if dados['nome'] == '' or dados['celular'] == '' or dados['email'] == '':
                return False
            else:
                return True