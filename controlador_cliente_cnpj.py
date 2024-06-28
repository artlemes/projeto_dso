from cliente_cnpj import ClienteCnpj
from tela_cliente_cnpj import TelaClienteCnpj

class ControladorClienteCnpj():
    def __init__(self, controlador_sistema):
        self.__tela_cliente_cnpj = TelaClienteCnpj()
        self.__clientes_cnpj = []
        self.__controlador_sistema = controlador_sistema

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
        dados = self.tela_cliente_cnpj.pega_dados_cliente_cnpj()

        certo = self.testador_variaveis(dados)

        if not certo:
            self.tela_cliente_cnpj.mostra_msg('Não foi possivel cadastrar esta cliente:')
            self.tela_cliente_cnpj.mostra_msg('parâmetros inválidos')

        else:
            duplicado = False

            novo = ClienteCnpj(dados["nome"], 
                         dados["celular"], 
                         dados["email"], 
                         dados["cnpj"])

            for cliente in self.clientes_cnpj:
                if cliente.cnpj == novo.cnpj:
                    duplicado = True
            
            if not duplicado:
                self.clientes_cnpj.append(novo)
                self.controlador_sistema.controlador_contato.contatos.append(novo.contato)
                self.tela_cliente_cnpj.mostra_msg("cliente adicionado com sucesso")
                return True
            
            else:
                self.tela_cliente_cnpj.mostra_msg('Não foi possivel cadastrar este cliente:')
                self.tela_cliente_cnpj.mostra_msg('Cnpj já existente')
                return False

    #status: feito, erro, recursao
    def alterar_cliente_cnpj(self):
        self.listar_cliente_cnpj()
        #seleção do cliente_cnpj a ser alterado
        cliente = self.acha_cliente_by_cnpj()
        if cliente == None:
            return

        #captação de dados
        dados_alterados = self.tela_cliente_cnpj.pega_dados_cliente_cnpj()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            cliente.nome = dados_alterados["nome"]
            cliente.contato.celular = dados_alterados["celular"]
            cliente.contato.email = dados_alterados["email"]
            cliente.cnpj = dados_alterados["cnpj"]  

        if not certo:
            self.tela_cliente_cnpj.mostra_msg("Não foi possível alterar este cliente")
            self.tela_cliente_cnpj.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def excluir_cliente_cnpj(self):

        self.listar_cliente_cnpj()
        cliente_cnpj = self.acha_cliente_by_cnpj()

        if cliente_cnpj in self.clientes_cnpj:
            self.clientes_cnpj.remove(cliente_cnpj)
            self.tela_cliente_cnpj.mostra_msg('Cliente excluído')
        else:
            self.tela_cliente_cnpj.mostra_msg("Atenção: cliente inexistente")

    #status: funcionando
    def listar_cliente_cnpj(self):
        for cliente in self.clientes_cnpj:
            self.tela_cliente_cnpj.mostra_cliente_cnpj(cliente)

    #status: fazer
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_cliente_cnpj.tela_opcoes())
            except:
                self.tela_cliente_cnpj.mostra_msg("opção não é um inteiro")
                op = None
            if op == 1:
                self.incluir_cliente_cnpj()
            elif op == 2:
                self.alterar_cliente_cnpj()
            elif op == 3:
                self.tela_cliente_cnpj.espacamento()
                self.listar_cliente_cnpj()
            elif op == 4:
                self.excluir_cliente_cnpj()
            elif op == 0:
                continua = False
            else: 
                self.tela_cliente_cnpj.mostra_msg("opção inválida")

    #status: funcionanod
    def acha_cliente_by_cnpj(self):
        #input de código

        cnpj = self.tela_cliente_cnpj.seleciona_cliente_cnpj()

        for cliente in self.clientes_cnpj:
            if cliente.cnpj == cnpj:
                ok = True
                return cliente

        self.tela_cliente_cnpj.mostra_msg('Cnpj não encontrado, tente novamente')
        return

    #status: funcionando?
    #serve de algo?
    def testador_variaveis(self, cliente_cnpj_dados) -> bool:
        try:
            cliente_cnpj_dados_checados = {"nome":str(cliente_cnpj_dados["nome"]),
                                    "celular": str(cliente_cnpj_dados["celular"]),
                                    "email":str(cliente_cnpj_dados["email"]),
                                    "cnpj":str(cliente_cnpj_dados["cnpj"])}
            return True
        
        except:
            return False