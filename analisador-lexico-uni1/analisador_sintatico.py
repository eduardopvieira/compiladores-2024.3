class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens  # Lista de tokens gerados pelo lexer
        self.pos = 0  # Posição atual na lista de tokens
        self.saida = []  # Armazena a saída da análise sintática

    def obter_token_atual(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consumir(self):
        token = self.obter_token_atual()
        self.pos += 1
        return token

    def erro_sintatico(self, esperado):
        token_atual = self.obter_token_atual()
        mensagem = f"Erro sintático: esperado '{esperado}', mas encontrou '{token_atual}'"
        self.saida.append(mensagem)
        raise Exception(mensagem)

    def verificar(self, tipo):
        token = self.obter_token_atual()
        if token and token[0] == tipo:
            return True
        return False

    # Regras de gramática
    def parse(self):
        self.saida.append("Iniciando análise sintática...")
        while self.obter_token_atual():
            self.parse_declaracao_classe()
        self.saida.append("Análise sintática concluída com sucesso.")

    def parse_declaracao_classe(self):
        if self.verificar("PALAVRA_RESERVADA"):
            token = self.consumir()
            if token[1].lower() == "class:":
                self.saida.append(f"Declarando classe: {token[1]}")
                self.parse_nome_classe()
                self.parse_corpo_classe()
            else:
                self.erro_sintatico("Class:")

    def parse_nome_classe(self):
        if self.verificar("CLASSE"):
            token = self.consumir()
            self.saida.append(f"Nome da classe: {token[1]}")
        else:
            self.erro_sintatico("nome de classe")

    def parse_corpo_classe(self):
        while self.verificar("PALAVRA_RESERVADA"):
            token = self.consumir()
            if token[1].lower() in ["equivalentto:", "subclassof:", "individuals:", "disjointclasses:"]:
                self.saida.append(f"Encontrado: {token[1]}")
                self.parse_expressao()
            else:
                self.erro_sintatico("EquivalentTo, SubClassOf, Individuals, DisjointClasses")

    def parse_expressao(self):
        while not self.verificar("PALAVRA_RESERVADA") and self.obter_token_atual():
            token = self.consumir()
            self.saida.append(f"Expressão: {token}")

    def salvar_saida(self, arquivo):
        with open(arquivo, "w") as f:
            for linha in self.saida:
                f.write(linha + "\n")

# Teste com tokens gerados pelo lexer
if __name__ == "__main__":
    # Exemplo de tokens gerados pelo lexer
    tokens = [
        ("PALAVRA_RESERVADA", "Class:"),
        ("CLASSE", "Customer"),
        ("PALAVRA_RESERVADA", "EquivalentTo:"),
        ("CLASSE", "Person"),
        ("CARACTERE_ESPECIAL", "("),
        ("PROPRIEDADE", "purchasedPizza"),
        ("CLASSE", "Pizza"),
        ("CARACTERE_ESPECIAL", ")"),
    ]

    parser = AnalisadorSintatico(tokens)
    try:
        parser.parse()
        print("\n".join(parser.saida))
        parser.salvar_saida("saida_sintatica.txt")
        print("Saída salva em 'saida_sintatica.txt'")
    except Exception as e:
        print(e)