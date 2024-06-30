from contato import Contato
from telas.tela_contato import TelaContato
from DAOs.contato_dao import ContatoDAO

class ControladorContato():
    def __init__(self):
        self.__tela_contato = TelaContato()
        self.__contato_DAO = ContatoDAO()

    @property
    def contatos(self):
        return self.__contatos
    
    @property
    def tela_contato(self):
        return self.__tela_contato

    #status: temos que pensar, porque teoricamente o contato é criado dentro de uma pessoa
    def inclui_contato(self) -> bool:
        contato_dados, botao = self.tela_contato.pega_dados_contato()

        #essa pode ser uma das nossas exceções criadas
        if contato_dados['celular'] == '' or contato_dados['email'] == '':
            self.tela_contato.mostra_msg('Não foi possivel cadastrar esta contato:')
            self.tela_contato.mostra_msg('parâmetros inválidos')
            return False

        #essa pode ser uma das nossas exceções criadas
        if botao == 'Cancelar':
            return None
        
        certo = self.testador_variaveis(contato_dados)


        if not certo:
            self.tela_contato.mostra_msg('Não foi possivel cadastrar esta contato:')
            self.tela_contato.mostra_msg('parâmetros inválidos')

        else:
            duplicado = False

            novo = Contato(contato_dados["celular"], contato_dados['email'])

            for contato in self.__contato_DAO.get_all():
                if contato.celular == novo.celular:
                    duplicado = True
            
            if not duplicado:
                self.__contato_DAO.add(novo)
                self.tela_contato.mostra_msg('Contato incluido com sucesso')
            
            else:
                self.tela_contato.mostra_msg('Não foi possivel cadastrar este contato: ')
                self.tela_contato.mostra_msg('Celular já existente')
                return False

    #status: feito, testar
    def altera_contato(self):
        #seleção do contato a ser alterado
        contato = self.acha_contato_by_num()
        
        #testando se o botao foi cancelar
        if isinstance(contato, str):
            return None
        
        #checagem de contato nulo
        if contato == None:
            self.tela_contato.mostra_msg("Não foi possível alterar este contato, ele não existe")

        #captação de dados
        dados_alterados, botao = self.tela_contato.pega_dados_contato()

        if botao == 'Cancelar':
            return None

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)
        print(certo)

        if certo:
            contato.celular = dados_alterados['celular']
            contato.email = dados_alterados['email']
            print('dados mudaram, erro no dao')
            self.__contato_DAO.update(contato)
            self.tela_contato.mostra_msg('Contato alterado com sucesso')

        else:
            self.tela_contato.mostra_msg("Não foi possível alterar esta contato")
            self.tela_contato.mostra_msg("erro na captação de dados")

    #status: feito, testar
    def exclui_contato(self):
        self.lista_contato()
        contato = self.acha_contato_by_num()

        if isinstance(contato, str):
            return None

        if contato in self.__contato_DAO.get_all():
            self.__contato_DAO.remove(str(contato.celular))
            self.tela_contato.mostra_msg('contato excluído')
        else:
            self.tela_contato.mostra_msg("Atenção: contato inexistente")

    #status: feito, testar
    def lista_contato(self):
        for contato in self.__contato_DAO.get_all():
            print(contato.celular)
            self.tela_contato.mostra_contato({"celular": contato.celular, "email": contato.email})

    #status: feita, testar
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op, botao = self.tela_contato.tela_opcoes()

                if op == 1:
                    self.inclui_contato()
                elif op == 2:
                    self.altera_contato()
                elif op == 3:
                    self.lista_contato()
                elif op == 4:
                    self.exclui_contato()
                elif op == 0 or botao == 'Cancelar':
                    continua = False
            except:
                self.tela_contato.mostra_msg("Selecione uma opção ou retorne")
                op = None

    #status: feito, testar
    def acha_contato_by_num(self):
        #input de código
        num, botao = self.tela_contato.seleciona_contato()

        if botao == 'Cancelar':
            print('o botao foi cancelar')
            return botao

        for contato in self.__contato_DAO.get_all():
            if str(contato.celular) == str(num):
                return contato

        self.tela_contato.mostra_msg('Numero nao reconhecido')
    
        return False

    
    def testador_variaveis(self, contato_dados) -> dict:
        try:
            int(contato_dados['celular'])
            print('funcionou')

            if contato_dados['email'] == '':
                return False
            
            return True
        except:
            print('erro')

        return False