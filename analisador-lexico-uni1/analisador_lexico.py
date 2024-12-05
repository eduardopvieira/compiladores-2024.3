import re

#codigo manual:
def codManual():
    codigo_manual = "and (hasCaloricContent some xsd:integer[>= 400])"
    result = lexer(codigo_manual)
    print(result)

#Ler arquivo:
def lerArquivo():

    arquivo = open('codigo.txt', 'r')
    codigo = arquivo.readlines()

    for linha in codigo:
        result = lexer(linha)
        print(result)

    arquivo.close()

TOKENS = [

    ("NOME_INDIVIDUO", r"([A-Z][a-z]+)+[0-9]"), # Eduardo1, MikaelJohnatan2
    ("PALAVRA_RESERVADA", r"([A-Z][a-z]+)+:"), #EquivalentTo: e palavras com :' 
    ("CLASSE", r"([A-Z][a-z]+[_]?)+"), # Pizza, Pizza_Margherita, PizzaMargherita, Pizza_Margherita_
    ("TIPO_DE_DADO", r"[a-z]+:[a-z]+([A-z][a-z]+)*"), #owl:algo
    ("PROPRIEDADE", r"has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+"), # hasAbcDe, isAbcDeOf, abc
    ("ESPACO_BRANCO", r"\s"),
    ("CARACTERE_ESPECIAL", r"[{}\[\]()<>.,=]{1,2}")

]


def lexer(input):
    tokens = []
    while input:
        match = None
        for token_nome, token_regex in TOKENS:
            padrao = re.compile(token_regex)
            match = padrao.match(input)
            if match:
                lexema = match.group(0)
                if token_nome != "ESPACO_BRANCO":  # ignorando espaços em branco
                    tokens.append((token_nome, lexema))
                input = input[len(lexema):]  # vai avançando o codigo
                break
        if not match:            
            print("erro em '{input:10}'")
            break
    return tokens


codManual()