class TabelaSimbolos:

    def __init__(self):
        self.tabela_simbolos = {}

    def insere_simbolo(self, nome, tipo, escopo):
        if nome in self.tabela_simbolos:
            print(f"Erro: Identificador '{nome}' já declarado nesse escopo.")
        else:
            self.tabela_simbolos[nome] = {
                'tipo': tipo,
                'escopo': escopo
            }

    def busca_simbolo(self, nome):
        if nome in self.tabela_simbolos:
            return self.tabela_simbolos[nome]
        else:
            print(f"Erro: Identificador '{nome}' não encontrado.")
            return None