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
            total_classes = 0
            total_individuos = 0
            total_propriedades = 0
            total_tipos_de_dados = 0
            total_palavras_reservadas = 0
            total_namespace = 0
            total_caracteres_especiais = 0
            total_cardinalidades = 0
            for (tipo, quantidade) in self.tabela.items():
                if tipo == "CLASSE":
                    total_classes += quantidade
                elif tipo == "NOME_INDIVIDUO":
                    total_individuos += quantidade
                elif tipo == "PROPRIEDADE":
                    total_propriedades += quantidade
                elif tipo == "TIPO":
                    total_tipos_de_dados += quantidade
                elif tipo == "PALAVRA_RESERVADA":
                    total_palavras_reservadas += quantidade
                elif tipo == "NAMESPACE":
                    total_namespace += quantidade
                elif tipo == "CARACTERE_ESPECIAL":
                    total_caracteres_especiais += quantidade
                elif tipo == "CARDINALIDADE":
                    total_cardinalidades += quantidade
            arquivo.write(f"\nTOTAL DE CLASSES: {total_classes}\n")
            arquivo.write(f"TOTAL DE INDIVIDUOS: {total_individuos}\n")
            arquivo.write(f"TOTAL DE PROPRIEDADES: {total_propriedades}\n")
            arquivo.write(f"TOTAL DE TIPOS DE DADOS: {total_tipos_de_dados}\n")
            arquivo.write(f"TOTAL DE PALAVRAS RESERVADAS: {total_palavras_reservadas}\n")
            arquivo.write(f"TOTAL DE NAMESPACE: {total_namespace}\n")
            arquivo.write(f"TOTAL DE CARACTERES ESPECIAIS: {total_caracteres_especiais}\n")
            arquivo.write(f"TOTAL DE CARDINALIDADES: {total_cardinalidades}\n")
            