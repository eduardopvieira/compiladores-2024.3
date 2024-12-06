class TabelaDeSimbolos:
    def __init__(self, prev=None):

        self.tabela = {}  # <-- DICIONARIO ONDE É GUARDADO O IDENTIFICADOR E O TIPO
        self.prev = prev  # <-- PONTEIRO PARA A TABELA ANTERIOR (nenhuma no momento)

    # def adicionar_simbolo(self, identificador, tipo):
    #     self.tabela[identificador] = tipo

    def buscar_tipo(self, identificador):
        if identificador in self.tabela:
            return self.tabela[identificador]
        elif self.prev:  # Se não encontrar, busca na tabela anterior
            return self.prev.buscar_tipo(identificador)
        return None

    def printarTabela(self):
        print("Tabela de Símbolos Atual:")
        if not self.tabela:
            print("  <Vazio>")
        else:
            for identificador, tipo in self.tabela.items():
                print(f" [\'{identificador}\' : \'{tipo}\']")

    # def registrarResultado(self):
    #     with open('resultado_analise.txt', 'w') as arquivo:
    #         for identificador, tipo in self.tabela.items():
    #             arquivo.write(f" [\'{identificador}\' : \'{tipo}\']\n")
    #             print('registrado com sucesso')

    def adicionar_simbolo(self, identificador, tipo):
        if identificador in self.tabela:
            # Incrementa a quantidade se já existir
            tipo_existente, quantidade = self.tabela[identificador]
            self.tabela[identificador] = (tipo_existente, quantidade + 1)
        else:
            # Cria a entrada com quantidade inicial de 1
            self.tabela[identificador] = (tipo, 1)

    def registrarResultado(self, nome_arquivo='resultado_analise.txt'):
        with open(nome_arquivo, 'w') as arquivo:
            for identificador, (tipo, quantidade) in self.tabela.items():
                arquivo.write(f"['{identificador}' : '{tipo}', quantidade: {quantidade}]\n")
                print('registrado com sucesso')