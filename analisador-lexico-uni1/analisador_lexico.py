import re
from tabela_de_simbolos import TabelaDeSimbolos

#Ler cod manual (fins de debug):
def codManual():
    tabela = TabelaDeSimbolos()
    codigo_manual = "EquivalentTo: Person and (purchasedPizza some Pizza) and Person"
    result = lexer(codigo_manual, tabela)
    print(result)
    tabela.registrarResultado()
#Ler arquivo:
def lerArquivo():
    tabela = TabelaDeSimbolos()
    with open('codigo.txt', 'r') as arquivo:
        codigo = arquivo.readlines()

    for linha in codigo:
        lexer(linha, tabela)
    tabela.registrarResultado()

TOKENS = [
    ("NOME_INDIVIDUO", r"([A-Z][a-z]+)+[0-9]+"),  # Eduardo1, MikaelJohnatan2
    ("PALAVRA_RESERVADA", r"([A-Z][a-z]+)+:"),   # EquivalentTo: e palavras com :
    ("CLASSE", r"([A-Z][a-z]+[_]?)+"),           # Pizza, Pizza_Margherita, PizzaMargherita
    ("TIPO_DE_DADO", r"[a-z]+:[a-z]+([A-Z][a-z]+)*"),  # owl:algo
    ("PROPRIEDADE", r"has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+"),  # hasAbcDe, isAbcDeOf, abc
    ("ESPACO_BRANCO", r"\s"),                    # espaços em branco
    ("CARACTERE_ESPECIAL", r"[{}\[\]()<>.,=]{1,2}"),  # caracteres especiais
    ("CARDINALIDADE", r"[0-9]+")
]


def lexer(input, tabela: TabelaDeSimbolos):
    while input:
        match = None
        for token_nome, token_regex in TOKENS:
            padrao = re.compile(token_regex)
            match = padrao.match(input)
            if match:
                lexema = match.group(0)
                if token_nome != "ESPACO_BRANCO":  # ignorando espaços em branco
                    tabela.adicionar_simbolo(lexema, token_nome)
                input = input[len(lexema):]  # avança a palavra
                break
        if not match:
            print(f"Erro léxico: token não reconhecido perto de '{input[:10]}'")
            break
    tabela.printarTabela()

lerArquivo()
#codManual()
