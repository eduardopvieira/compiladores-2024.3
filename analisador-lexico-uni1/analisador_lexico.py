import re
from tabela_de_simbolos import TabelaDeSimbolos

#Ler cod manualmente (fins de debug):
def codManual(codigo_manual: str):
    tabela_manual = TabelaDeSimbolos()
    lexer(codigo_manual, tabela_manual)
    tabela_manual.printarTabela()
    
#Ler arquivo de codigo:
def lerArquivo():
    tabela = TabelaDeSimbolos()
    with open('codigo.txt', 'r') as arquivo:
        codigo = arquivo.readlines()

    for linha in codigo:
        lexer(linha, tabela)
    tabela.registrarResultado()
    tabela.visualizarDados()

TOKENS = [
    ("NOME_INDIVIDUO", r"([A-Z][a-z]+)+[0-9]+"),            # Eduardo1, MikaelJohnatan2
    ("PALAVRA_RESERVADA", r"([A-Z][a-z]+)+:|some|all|value|min|exactly|that|max|not|and|or"), # EquivalentTo:, palavras com : e palavras reservadas
    ("CLASSE", r"([A-Z][a-z]+[_]?)+"),                      # Pizza, Pizza_Margherita, PizzaMargherita
    ("NAMESPACE", r"[a-z]{3,4}:"),                          # rdf:, owl:, rdfs:
    ("TIPO", r"rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|int|integer|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort"),  # tipos de dados
    ("PROPRIEDADE", r"has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-z][a-z]+)*"),  # hasAbcDe, isAbcDeOf, abc, abCdeFgh,  # hasAbcDe, isAbcDeOf, abc
    ("ESPACO_BRANCO", r"\s"),                               # espaços em branco
    ("CARACTERE_ESPECIAL", r"[{}\[\]().,\"']|[<>=\"]{1,2}"),    # caracteres especiais
    ("CARDINALIDADE", r"[0-9]+")                            # numeros
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

#Chamada de funções: (descomentar a que deseja usar)

lerArquivo()
#codManual("Class:teste1 Class:teste2 Class:teste3")