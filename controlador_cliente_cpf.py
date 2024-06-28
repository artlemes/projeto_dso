from cliente_cpf import ClienteCpf
from tela_cliente_cpf import TelaClienteCpf

class ControladorClienteCpf():
    def __init__(self, controlador_sistema):
        self.__tela_cliente_cpf = TelaClienteCpf()
        self.__clientes_cpf = []
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def clientes_cpf(self):
        return self.__clientes_cpf
    
    @property
    def tela_cliente_cpf(self):
        return self.__tela_cliente_cpf

    #status: funcionando
    def incluir_cliente_cpf(self) -> bool:
        dados = self.tela_cliente_cpf.pega_dados_cliente_cpf()

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

            for cliente in self.clientes_cpf:
                if cliente.cpf == novo.cpf:
                    duplicado = True
            
            if not duplicado:
                self.clientes_cpf.append(novo)
                self.controlador_sistema.controlador_contato.contatos.append(novo.contato)
                self.tela_cliente_cpf.mostra_msg("cliente adicionado com sucesso")
                return True
            
            else:
                self.tela_cliente_cpf.mostra_msg('Não foi possivel cadastrar este cliente:')
                self.tela_cliente_cpf.mostra_msg('cpf já existente')
                return False

    #status: feito, erro, recursao
    def alterar_cliente_cpf(self):
        self.listar_cliente_cpf()
        #seleção do cliente_cpf a ser alterado
        cliente = self.acha_cliente_by_cpf()
        if cliente == None:
            return

        #captação de dados
        dados_alterados = self.tela_cliente_cpf.pega_dados_cliente_cpf()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            cliente.nome = dados_alterados["nome"]
            cliente.contato.celular = dados_alterados["celular"]
            cliente.contato.email = dados_alterados["email"]
            cliente.cpf = dados_alterados["cpf"]  

        if not certo:
            self.tela_cliente_cpf.mostra_msg("Não foi possível alterar este cliente")
            self.tela_cliente_cpf.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def excluir_cliente_cpf(self):

        self.listar_cliente_cpf()
        cliente_cpf = self.acha_cliente_by_cpf()

        if cliente_cpf in self.clientes_cpf:
            self.clientes_cpf.remove(cliente_cpf)
            self.tela_cliente_cpf.mostra_msg('Cliente excluído')
        else:
            self.tela_cliente_cpf.mostra_msg("Atenção: cliente inexistente")

    #status: funcionando
    def listar_cliente_cpf(self):
        for cliente in self.clientes_cpf:
            self.tela_cliente_cpf.mostra_cliente_cpf(cliente)

    #status: fazer
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_cliente_cpf.tela_opcoes())
            except:
                self.tela_cliente_cpf.mostra_msg("opção não é um inteiro")
                op = None
            if op == 1:
                self.incluir_cliente_cpf()
            elif op == 2:
                self.alterar_cliente_cpf()
            elif op == 3:
                self.tela_cliente_cpf.espacamento()
                self.listar_cliente_cpf()
            elif op == 4:
                self.excluir_cliente_cpf()
            elif op == 0:
                continua = False
            else: 
                self.tela_cliente_cpf.mostra_msg("opção inválida")

    #status: funcionanod
    def acha_cliente_by_cpf(self):
        #input de código

        cpf = self.tela_cliente_cpf.seleciona_cliente_cpf()

        for cliente in self.clientes_cpf:
            if cliente.cpf == cpf:
                ok = True
                return cliente

        self.tela_cliente_cpf.mostra_msg('cpf não encontrado, tente novamente')
        return

    #status: funcionando?
    #serve de algo?
    def testador_variaveis(self, cliente_cpf_dados) -> bool:
        try:
            cliente_cpf_dados_checados = {"nome":str(cliente_cpf_dados["nome"]),
                                    "celular": str(cliente_cpf_dados["celular"]),
                                    "email":str(cliente_cpf_dados["email"]),
                                    "cpf":str(cliente_cpf_dados["cpf"])}
            return True
        
        except:
            return False