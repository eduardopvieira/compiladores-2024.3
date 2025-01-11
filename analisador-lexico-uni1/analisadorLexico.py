import ply.lex as lex
import ply.yacc as yacc

# Classe substituta para TabelaDeSimbolos
class TabelaDeSimbolos:
    def __init__(self):
        self.simbolos = []

    def adicionar_simbolo(self, lexema, tipo):
        self.simbolos.append((lexema, tipo))

    def exibir(self):
        print("Tabela de Símbolos:")
        for simbolo in self.simbolos:
            print(simbolo)

# Tokens 
tokens = [
    "NOME_INDIVIDUO",
    "PALAVRA_RESERVADA",
    "CLASSE",
    "NAMESPACE",
    "TIPO",
    "PROPRIEDADE",
    "CARACTERE_ESPECIAL",
    "CARDINALIDADE",
]

# Regras de expressão regular para os tokens
t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt]|[Mm][Aa][Xx]|[Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:|DisjointWith:|and|some'
t_CLASSE = r'([A-Z][a-z]+[_]?)+' 
t_NAMESPACE = r'[a-z]{3,4}:'
t_TIPO = r'rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|integer|int|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*' 
t_CARACTERE_ESPECIAL = r'[{}\[\]().,\"\']|[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'


# Ignora os espaços em branco e tabulações
t_ignore = ' \t\n\r'

def t_error(t):
    erro = f"Erro léxico: token não reconhecido perto de '{t.value[:10]}'\n"
    print(erro)
    with open("erros_lexicos.txt", "a") as log_file:
        log_file.write(erro)
    t.lexer.skip(1)

# Instancia do analisador léxico
lexer = lex.lex(errorlog=lex.NullLogger())

# Regras sintáticas
def p_programa(p):
    """programa : declaracao_classe programa
        | declaracao_classe"""
    pass

# Classe Primitiva
def p_declaracao_classe_primitiva(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE restricoes """ #disjunto individuos
    pass

def p_restricoes(p):
    """restricoes : CARACTERE_ESPECIAL PALAVRA_RESERVADA CLASSE restricoes
                  | """
    pass
                  #| restricoes_composta
                  #| CARDINALIDADE
                  #| CARACTERE_ESPECIAL"""

def p_declaracao_classe_axioma_fechamento(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento """
    pass
#CLASS: oiajsdoa
#Subclassof:
#poksapdkas, 
#lkaçlsdkaçs
def p_restricoes_axioma_fechamento(p):
    """restricoes_axioma_fechamento : PROPRIEDADE PALAVRA_RESERVADA CLASSE
                  | PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
                  | PROPRIEDADE PALAVRA_RESERVADA CARACTERE_ESPECIAL CLASSE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL 
                  | PROPRIEDADE PALAVRA_RESERVADA CARACTERE_ESPECIAL CLASSE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL CARACTERE_ESPECIAL restricoes_axioma_fechamento"""
    pass
                  #| restricoes_composta


def p_restricoes_composta(p):
    """restricoes_composta : restricoes CARACTERE_ESPECIAL PROPRIEDADE PALAVRA_RESERVADA CLASSE
                           | restricoes CARACTERE_ESPECIAL PALAVRA_RESERVADA CARACTERE_ESPECIAL CLASSE"""
    pass

def p_disjunto(p):
    """disjunto : PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL CLASSE
                | """
    pass

def p_individuos(p):
    """individuos : PALAVRA_RESERVADA NOME_INDIVIDUO
                  | individuos CARACTERE_ESPECIAL NOME_INDIVIDUO"""
    pass

# Classe Definida
def p_declaracao_classe_definida(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL restricoes_def"""
    pass

def p_restricoes_def(p):
    """restricoes_def : CLASSE PALAVRA_RESERVADA restricoes
                      | restricoes_composta CARACTERE_ESPECIAL restricoes"""
    pass

# Classe Enumerada
def p_declaracao_classe_enumerada(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL CARACTERE_ESPECIAL lista_individuos CARACTERE_ESPECIAL"""
    pass

def p_lista_individuos(p):
    """lista_individuos : NOME_INDIVIDUO
                         | lista_individuos CARACTERE_ESPECIAL NOME_INDIVIDUO"""
    pass

# Classe Coberta
def p_declaracao_classe_coberta(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL lista_classes"""
    pass

def p_lista_classes(p):
    """lista_classes : CLASSE
                      | lista_classes PALAVRA_RESERVADA CLASSE"""
    pass

# Erro sintático
def p_error(p):
    if p:
        print(f"Erro sintático: token inesperado '{p.value}', linha {p.lineno}")
    else:
        print("Erro sintático: fim inesperado da entrada.")

# Construir o analisador sintático
parser = yacc.yacc()

def executar_analisador(codigo):
    lexer.input(codigo)
    result = parser.parse(codigo, lexer=lexer)
    if result is None:
        print("Análise sintática concluída com sucesso.")
    else:
        print("Erros encontrados na análise sintática.")

# Função principal
def main():
    print("Escolha uma opção:")
    print("1 - Ler código do arquivo 'codigo.txt'")
    print("2 - Escrever código manualmente")
    print("3 - Sair")
    opcao = input()

    if opcao == "1":
        try:
            with open('codigo.txt', 'r') as arquivo:
                codigo = arquivo.read()
            executar_analisador(codigo)
        except FileNotFoundError:
            print("Erro: O arquivo 'codigo.txt' não foi encontrado.")

    elif opcao == "2":
        print("Digite o código:")
        codigo = input()
        executar_analisador(codigo)

    elif opcao == "3":
        exit()

    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
