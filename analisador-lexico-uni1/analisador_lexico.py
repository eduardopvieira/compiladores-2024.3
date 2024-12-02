import re

#tokens registrados:

TOKENS = [

    ("NOME_INDIVIDUO", r"([A-Z][a-z]+)+[0-9]"), # Eduardo1, MikaelJohnatan2
    ("CLASSE", r"([A-Z][a-z]+[_]?)+"), # Pizza, Pizza_Margherita, PizzaMargherita, Pizza_Margherita_
    ("PROPRIEDADE", r"has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+"), # hasAbcDe, isAbcDeOf, abc
    ("TIPO_DE_DADO", r"[a-z]+: [a-z]+"), #owl: algo
    ("PALAVRA_RESERVADA", r"[A-Z]+"), #SOME, OF, THAT, ABC
    ("CARACTERE_ESPECIAL", r"[ \[ \] { } ( ) , < > ]"), #[ , ], (), ><
    ("ESPACO_BRANCO", r"\s"),

]

#ignore abaixo, apenas teste

def lexer(input_code):
    tokens = []
    while input_code:
        match = None
        for token_name, token_regex in TOKENS:
            pattern = re.compile(token_regex)
            match = pattern.match(input_code)
            if match:
                lexeme = match.group(0)
                if token_name != "ESPACO_BRANCO":  # ignorando espaços em branco
                    tokens.append((token_name, lexeme))
                input_code = input_code[len(lexeme):]  # vai avançando o codigo
                break
        if not match:
            # CASO NAO DE NENHUM MATCH VEM PRA CA E DA ERRO
            raise SyntaxError(f"Token inválido: '{input_code[0]}' em '{input_code}'")
    return tokens

# Exemplo de uso
code = "ALO"
result = lexer(code)
print(result)
