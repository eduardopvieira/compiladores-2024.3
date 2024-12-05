import re

TOKENS = [

    ("NOME_INDIVIDUO", r"([A-Z][a-z]+)+[0-9]"), # Eduardo1, MikaelJohnatan2
    ("PALAVRA_RESERVADA", r"([A-Z][a-z]+)+:"), #EquivalentTo: e palavras com :' 
    ("CLASSE", r"([A-Z][a-z]+[_]?)+"), # Pizza, Pizza_Margherita, PizzaMargherita, Pizza_Margherita_
    ("PROPRIEDADE", r"has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+"), # hasAbcDe, isAbcDeOf, abc
    ("TIPO_DE_DADO", r"[a-z]+: ?[a-z]+"), #owl: algo
    ("ESPACO_BRANCO", r"\s"),
    ("CARACTERE_ESPECIAL", r"[ \[ \] { } ( ) , < > ]"), #[ , ], (), ><

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
            
            print("deu ruim")
            #raise SyntaxError(f"Token inválido: '{input_code[0]}' em '{input_code}'")
            break
    return tokens

# USAR:
#arquivo = open('codigo.txt')
#codigo = arquivo.read
code = "EquivalentTo: Person and (purchasedPizza some Pizza) and"
result = lexer(code)
print(result)
