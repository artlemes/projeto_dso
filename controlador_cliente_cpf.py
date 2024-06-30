from cliente_cpf import ClienteCpf
from telas.tela_cliente_cpf import TelaClienteCpf
from DAOs.cliente_cpf_dao import ClienteCpfDAO
from DAOs.contato_dao import ContatoDAO

class ControladorClienteCpf():
    def __init__(self, controlador_sistema):
        self.__tela_cliente_cpf = TelaClienteCpf()
        self.__cliente_DAO = ClienteCpfDAO()
        self.__contato_DAO = ContatoDAO()

    @property
    def tela_cliente_cpf(self):
        return self.__tela_cliente_cpf

    #status: funcionando
    def incluir_cliente_cpf(self) -> bool:
        dados, botao = self.tela_cliente_cpf.pega_dados_cliente()

        if botao == 'Cancelar':
            return None

        certo = self.testador_variaveis(dados)

        if not certo:
            self.tela_cliente_cpf.mostra_msg('Não foi possivel cadastrar esta cliente:')
            self.tela_cliente_cpf.mostra_msg('parâmetros inválidos')

        else:
            duplicado = False

            novo = ClienteCpf(dados["nome"], 
                         dados["celular"], 
                         dados["email"], 
                         dados["cpf"])

            for cliente in self.__cliente_DAO.get_all():
                if cliente.cpf == novo.cpf:
                    duplicado = True
            
            if not duplicado:
                self.__cliente_DAO.add(novo)
                self.__contato_DAO.add(novo.contato)
                self.tela_cliente_cpf.mostra_msg("cliente adicionado com sucesso")
                return True
            
            else:
                self.tela_cliente_cpf.mostra_msg('Não foi possivel cadastrar este cliente:')
                self.tela_cliente_cpf.mostra_msg('cpf já existente')
                return False

    #status: feito, erro, recursao
    def alterar_cliente_cpf(self):

        #seleção do cliente_cpf a ser alterado
        cliente = self.acha_cliente_by_cpf()

        if cliente == None:
            return

        #captação de dados
        dados_alterados, botao = self.tela_cliente_cpf.altera_dados_cliente()

        if botao == 'Cancelar':
            return None

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            cliente.nome = dados_alterados["nome"]
            cliente.contato.celular = dados_alterados["celular"]
            cliente.contato.email = dados_alterados["email"]
            self.__cliente_DAO.update(cliente)
            self.__contato_DAO.update(cliente.contato)
            return True
        
        if not certo:
            self.tela_cliente_cpf.mostra_msg("Não foi possível alterar este cliente")
            self.tela_cliente_cpf.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def excluir_cliente_cpf(self):

        self.listar_cliente_cpf()
        cliente = self.acha_cliente_by_cpf()

        if cliente == None:
            return None

        if cliente in self.__cliente_DAO.get_all():
            self.__cliente_DAO.remove(cliente.cpf)
            self.tela_cliente_cnpj.mostra_msg('Cliente excluído')
        else:
            self.tela_cliente_cpf.mostra_msg("Atenção: cliente inexistente")

    #status: funcionando
    def listar_cliente_cpf(self):
        for cliente in self.__cliente_DAO.get_all():
            self.tela_cliente_cpf.mostra_cliente(cliente)

    #status: fazer
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_cliente_cpf.tela_opcoes()

                if op == 1:
                    self.incluir_cliente_cpf()
                elif op == 2:
                    self.alterar_cliente_cpf()
                elif op == 3:
                    self.listar_cliente_cpf()
                elif op == 4:
                    self.excluir_cliente_cpf()
                elif op == 0 or botao == 'Cancelar':
                    continua = False
            except:
                self.tela_cliente_cpf.mostra_msg("Selecione algo ou retorne")
                op = None

    #status: funcionanod
    def acha_cliente_by_cpf(self):
        #input de código

        cpf, botao = self.tela_cliente_cpf.seleciona_cliente()

        if botao == 'Cancelar':
            return None

        for cliente in self.__cliente_DAO.get_all():
            if cliente.cpf == cpf:
                return cliente

        self.tela_cliente_cpf.mostra_msg('cpf não encontrado, tente novamente')
        return None

    #status: funcionando?
    #serve de algo?
    def testador_variaveis(self, dados) -> bool:
        if len(dados) == 4:
            if len(dados['cpf']) != 11 or dados['nome'] == '' or dados['celular'] == '' or dados['email'] == '':
                return False
            else:
                try:
                    int(dados['cpf'])
                    int(dados['celular'])
                except:
                    self.tela_cliente_cpf.mostra_msg('Celular e cpf devem conter apenas números')
                    return False
                return True
        else:
            if dados['nome'] == '' or dados['celular'] == '' or dados['email'] == '':
                return False
            else:
                return True