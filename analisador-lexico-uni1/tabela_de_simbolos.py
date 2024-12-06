class TabelaDeSimbolos:
    def __init__(self, prev=None):

        self.tabela = {}  # <-- DICIONARIO ONDE É GUARDADO O IDENTIFICADOR E O TIPO
        self.prev = prev  # <-- PONTEIRO PARA A TABELA ANTERIOR (nenhuma no momento)

    def printarTabela(self):
        print("Tabela de Símbolos Atual:")
        if not self.tabela:
            print("  <Vazio>")
        else:
            for identificador, tipo in self.tabela.items():
                print(f" [\'{identificador}\' : \'{tipo}\']")

    def adicionar_simbolo(self, identificador, tipo):
        if identificador in self.tabela:
            tipo_existente, quantidade = self.tabela[identificador]
            self.tabela[identificador] = (tipo_existente, quantidade + 1)
        else:
            self.tabela[identificador] = (tipo, 1)

    def registrarResultado(self, nome_arquivo='resultado_analise.txt'):
        with open(nome_arquivo, 'w') as arquivo:
            for identificador, (tipo, quantidade) in self.tabela.items():
                arquivo.write(f"['{identificador}' : '{tipo}', quantidade: {quantidade}]\n")

    def visualizarDados(self, nome_arquivo='visualizacao_dados.txt'):
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(f"\nCLASSES:\n")
            for identificador, (tipo, quantidade) in self.tabela.items():
                if tipo == "CLASSE":
                    arquivo.write(f"['{identificador}' : , quantidade: {quantidade}]\n")
            arquivo.write(f"\nINDIVIDUOS:\n")
            for identificador, (tipo, quantidade) in self.tabela.items():
                if tipo == "NOME_INDIVIDUO":
                    arquivo.write(f"['{identificador}' : , quantidade: {quantidade}]\n")
            arquivo.write(f"\nPROPRIEDADES:\n")
            for identificador, (tipo, quantidade) in self.tabela.items():
                if tipo == "PROPRIEDADE":
                    arquivo.write(f"['{identificador}' : , quantidade: {quantidade}]\n")