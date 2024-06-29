from bebida import Bebida
from tela_bebida import TelaBebida

class ControladorBebida():
    def __init__(self):
        self.__tela_bebida = TelaBebida()
        self.__bebidas = []

    @property
    def bebidas(self):
        return self.__bebidas
    
    @property
    def tela_bebida(self):
        return self.__tela_bebida

    #status: funcionando
    def inclui_bebida(self) -> bool:
        bebida_dados, botao = self.tela_bebida.pega_dados_bebida()

        certo = self.testador_variaveis(bebida_dados)

        if botao == 'Cancelar':
            return None

        if not certo:
            self.tela_bebida.mostra_msg('Não foi possivel cadastrar esta bebida:')
            self.tela_bebida.mostra_msg('parâmetros inválidos')

        else:
            duplicado = False

            novo = Bebida(bebida_dados["nome"], 
                         bebida_dados["preco"], 
                         bebida_dados["despesa"], 
                         bebida_dados["codigo"])

            for bebida in self.bebidas:
                if bebida.codigo == novo.codigo:
                    duplicado = True
            
            if not duplicado:
                self.bebidas.append(novo)
                return True
            
            else:
                self.tela_bebida.mostra_msg('Não foi possivel cadastrar este bebida:')
                self.tela_bebida.mostra_msg('código já existente')
                return False

    #status: funcionando
    def altera_bebida(self):
        #seleção do bebida a ser alterado
        bebida = self.acha_bebida_by_cod()

        #caso clique no botao cancelar
        if isinstance(bebida, str):
            return None

        #checagem de bebida nulo
        if bebida == None:
            self.tela_bebida.mostra_msg("Não foi possível alterar esta bebida, ela não existe")
            return False

        #captação de dados
        dados_alterados, botao = self.tela_bebida.altera_dados_bebida()

        print('conseguiu pegar os dados')
        print(dados_alterados, botao)

        if botao == 'Cancelar':
            print('o botao foi cancelar')
            return None
        
        print('testou o botao')
        print(dados_alterados)

        bebida.nome = dados_alterados["nome"]
        print('alterou o nome')
        bebida.preco = dados_alterados["preco"]
        print("Alterou o preco")
        bebida.despesa = dados_alterados["despesa"]
        print("Alterou o preco")
        bebida.codigo = bebida.codigo
        print('Alterou os dados')
        return True  

    #status: funcionando
    def exclui_bebida(self):
        self.lista_bebida()
        bebida = self.acha_bebida_by_cod()

        #se for cancelado retorna o botao
        if isinstance(bebida, str):
            return None

        if bebida in self.bebidas:
            self.bebidas.remove(bebida)
            self.tela_bebida.mostra_msg('bebida excluída')
        else:
            self.tela_bebida.mostra_msg("Atenção: bebida inexistente")

    #status: ainda não chequei
    def lista_bebida(self):
        for bebida in self.bebidas:
            self.tela_bebida.mostra_bebida({"nome": bebida.nome, "preco": bebida.preco, "despesa": bebida.despesa, "codigo": bebida.codigo})

    #status: funcionando
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                #to trazendo o botao junto
                op, botao = self.tela_bebida.tela_opcoes()

                if op == 1:
                    self.inclui_bebida()
                elif op == 2:
                    self.altera_bebida()
                elif op == 3:
                    self.lista_bebida()
                elif op == 4:
                    self.exclui_bebida()
                elif op == 0 or botao == 'Cancelar':
                    continua = False
                    
            except:
                self.tela_bebida.mostra_msg("Selecione uma opção ou retorne")
                op = None

    #status: funcionando
    def acha_bebida_by_cod(self) -> Bebida:
        #input de código

        cod, botao = self.tela_bebida.seleciona_bebida()

        if botao == 'Cancelar':
            return botao

        ok = False
        while not ok:
            try:
                int(cod)
                ok = True
            except:
                self.tela_bebida.mostra_msg("código deve ser um inteiro registrado\n")
        

        for bebida in self.bebidas:
            if bebida.codigo == cod:
                return bebida
        
        return False

    
    def testador_variaveis(self, bebida_dados) -> dict:
        try:
            bebida_dados_checados = {"nome":str(bebida_dados["nome"]),
                                    "preco": float(bebida_dados["preco"]),
                                    "despesa":float(bebida_dados["despesa"]),
                                    "codigo":int(bebida_dados["codigo"])}
            return True
        
        except:
            return False