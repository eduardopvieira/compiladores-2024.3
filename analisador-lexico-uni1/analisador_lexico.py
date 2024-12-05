import re

TOKENS = [
    ("NOME_INDIVIDUO", r"([A-Z][a-z]+)+[0-9]"),  # Eduardo1, MikaelJohnatan2
    ("PALAVRA_RESERVADA", r"([A-Z][a-z]+)+:"),   # EquivalentTo: e palavras com :
    ("CLASSE", r"([A-Z][a-z]+[_]?)+"),           # Pizza, Pizza_Margherita, PizzaMargherita
    ("TIPO_DE_DADO", r"[a-z]+:[a-z]+([A-Z][a-z]+)*"),  # owl:algo
    ("PROPRIEDADE", r"has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+"),  # hasAbcDe, isAbcDeOf, abc
    ("ESPACO_BRANCO", r"\s"),                    # espaços em branco
    ("CARACTERE_ESPECIAL", r"[{}\[\]()<>.,=]{1,2}")  # caracteres especiais
]

# Tabela de símbolos
tabela_simbolos = {}

def lexer(input, tabela):
    tokens = []
    linha_atual = 1
    posicao_atual = 0

    while input:
        match = None
        for token_nome, token_regex in TOKENS:
            padrao = re.compile(token_regex)
            match = padrao.match(input)
            if match:
                lexema = match.group(0)
                if token_nome != "ESPACO_BRANCO":  # ignorando espaços em branco
                    tokens.append((token_nome, lexema))
                    adicionar_tabela(lexema, token_nome, linha_atual, posicao_atual, tabela)
                input = input[len(lexema):]  # avança no código
                posicao_atual += len(lexema)
                break
        if not match:
            print(f"Erro léxico: token não reconhecido perto de '{input[:10]}...'")
            break
    return tokens

def adicionar_tabela(lexema, tipo, linha, posicao, tabela):
    if lexema not in tabela:
        tabela[lexema] = {
            "tipo": tipo,
            "ocorrencias": 1,
            "linhas": [linha],
            "posicoes": [posicao]
        }
    else:
        tabela[lexema]["ocorrencias"] += 1
        tabela[lexema]["linhas"].append(linha)
        tabela[lexema]["posicoes"].append(posicao)

def codManual():
    codigo_manual = "EquivalentTo: Person and (purchasedPizza some Pizza) and"
    tokens = lexer(codigo_manual, tabela_simbolos)
    print("Tokens:", tokens)
    print("Tabela de Símbolos:", tabela_simbolos)

# Lê o código de um arquivo
def lerArquivo():
    with open('codigo.txt', 'r') as arquivo:
        for linha_num, linha in enumerate(arquivo, start=1):
            lexer(linha, tabela_simbolos)
    print("Tabela de Símbolos:", tabela_simbolos)

if __name__ == "__main__":
    codManual()
