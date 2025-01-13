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
    "OPERADORES",
    "CARDINALIDADE",
    "ABRE_PARENT",
    "FECHA_PARENT",
    "EQUIVALENT_TO",
    "OR",
    "SUBCLASS0F",
    "INDIVIDUALS",
    "DISJOINTCLASSES"
]

# Regras de expressão regular para os tokens
t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt]|[Mm][Aa][Xx]|[Nn][Oo][Tt]|[Aa][Nn][Dd]|Class:|DisjointWith:|and|some|only'
t_CLASSE = r'([A-Z][a-z]+[_]?)+' 
t_NAMESPACE = r'[a-z]{3,4}:'
t_TIPO = r'rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|integer|int|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*' 
t_CARACTERE_ESPECIAL = r'[{}\[\].,\"\']'
t_OPERADORES = r'[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'
t_ABRE_PARENT = r'\('
t_FECHA_PARENT = r'\)'
t_EQUIVALENT_TO = r'EquivalentTo:'
t_OR = r'[Oo][Rr]'
t_SUBCLASSOF = r'SubClassOf:'
t_INDIVIDUALS = r'Individuals:' 
t_DISJOINTCLASSES = r'DisjointClasses:'
# Ignora os espaços em branco e tabulações
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    erro = f"Erro léxico: token não reconhecido perto de '{t.value[:10]}'\n"
    print(erro)
    with open("erros_lexicos.txt", "a") as log_file:
        log_file.write(erro)
    t.lexer.skip(1)

# Instancia do analisador léxico
lexer = lex.lex(errorlog=lex.NullLogger())

#?======================== REGRAS PRIMÁRIAS ============================= 
def p_programa(p):
    """programa : tipo_classe_primaria programa
                | tipo_classe_primaria"""
    pass

def p_tipo_classe_primaria(p):
    """
    tipo_classe_primaria: declaracao_classe_definida
                        | declaracao_classe_primitiva
    """
    pass

def p_tipo_classe_secundaria(p):
    """
    tipo_classe_secundaria: declaracao_classe_aninhada
                          | declaracao_classe_enumerada
                          | declaracao_classe_coberta
    """
    pass

#!===================== CLASSE PRIMITIVA ================

def p_declaracao_classe_primitiva(p):
    """declaracao_classe_primitiva : PALAVRA_RESERVADA CLASSE caso_subclassof caso_individuals_opcional caso_disjoint_opcional"""
    pass

def p_caso_subclassof(p):
    """
    caso_subclassof: SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA CLASSE
                   | SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO
                   | SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL caso_subclassof 
                   | SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL caso_subclassof
    """
    pass

def p_caso_individuals_opcional(p):
    """
    caso_individuals_opcional: NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional
                             | NOME_INDIVIDUO
                             | INDIVIDUALS NOME_INDIVIDUO
                             | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional
    """
    pass

def p_caso_disjoint_opcional(p):
    """
    caso_disjoint_opcional: CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
                         |  CLASSE
                         |  DISJOINTCLASSES CLASSE 
                         |  DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
    """

def p_restricoes_primitiva(p):
    """restricoes_primitiva : CARACTERE_ESPECIAL PALAVRA_RESERVADA CLASSE restricoes
                  | """
    pass

#!==================== CLASSE DEFINIDA ==================

def p_declaracao_classe_definida(p):
    """declaracao_classe_definida : PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE PALAVRA_RESERVADA restricoes_definida"""
    pass

# def p_restricoes_definida(p):
#     """restricoes_definida : ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT
#                            | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT PALAVRA_RESERVADA restricoes_definida

#                            | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE FECHA_PARENT   
#                            | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE FECHA_PARENT PALAVRA_RESERVADA  restricoes_definida

#                            | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA restricoes_definida FECHA_PARENT 
#                            | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA  caso_definida FECHA_PARENT """
                           
#     pass

# def p_caso_definida(p):
#       """caso_definida : CLASSE 
#                     | CLASSE PALAVRA_RESERVADA  FECHA_PARENT caso_definida
#                     | CLASSE PALAVRA_RESERVADA  FECHA_PARENT 
#                     | ABRE_PARENT CLASSE PALAVRA_RESERVADA caso_definida FECHA_PARENT"""
# pass
            
#!===================== CLASSE AXIOMA DE FECHAMENTO ========================

def p_declaracao_classe_axioma_fechamento(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento """
    pass

# def p_restricoes_axioma_fechamento(p):
#     """restricoes_axioma_fechamento : PROPRIEDADE PALAVRA_RESERVADA CLASSE
#                   | PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
#                   | PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
#                   | PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE 
#                   | PROPRIEDADE PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
#                   | PROPRIEDADE PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE 
#                   | caso_axioma 
#                   | PROPRIEDADE PROPRIEDADE PALAVRA_RESERVADA CLASSE
#                   | PROPRIEDADE PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
#                   | PROPRIEDADE PALAVRA_RESERVADA CARACTERE_ESPECIAL CLASSE PALAVRA_RESERVADA CLASSE  
#                   | PROPRIEDADE PALAVRA_RESERVADA CARACTERE_ESPECIAL CLASSE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL CARACTERE_ESPECIAL restricoes_axioma_fechamento"""
#     pass
                

# def p_caso_axioma(p):
#     """caso_axioma : ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT
#                     | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT CARACTERE_ESPECIAL restricoes_axioma_fechamento                    
#                     | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT PALAVRA_RESERVADA caso_axioma"""
#     pass



# Declaração de classe aninhada com suporte para múltiplas restrições e conectivos
def p_declaracao_classe_aninhada(p):
    """
    declaracao_classe : PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA CLASSE ands_aninhada FECHA_PARENT"""
    pass

# Suporte para cláusulas conectadas por "and" dentro de restrições
def p_ands_aninhada(p):
    """
    ands_aninhada : PALAVRA_RESERVADA restricoes_aninhada ands_aninhada
                  | PALAVRA_RESERVADA restricoes_aninhada"""
    pass

# Restrições aninhadas com cardinalidades, agrupamentos e conectivos lógicos
def p_restricoes_aninhada(p):
    """
    restricoes_aninhada : ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA ABRE_PARENT lista_classes FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE restricoes_aninhada
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE FECHA_PARENT restricoes_aninhada
                        | ABRE_PARENT restricoes_aninhada FECHA_PARENT"""
    pass

# Suporte para listas de classes em conectivos lógicos
def p_lista_classes(p):
    """
    lista_classes : CLASSE
                  | CLASSE conectivo_logico lista_classes"""
    pass

# Conectivos lógicos para combinações de classes e restrições
def p_conectivo_logico(p):
    """
    conectivo_logico : PALAVRA_RESERVADA
    """
    pass

# Definição de classes aninhadas e agrupamentos recursivos
def p_aninhada(p):
    """
    aninhada : ABRE_PARENT CLASSE PALAVRA_RESERVADA CLASSE FECHA_PARENT
             | ABRE_PARENT CLASSE PALAVRA_RESERVADA aninhada FECHA_PARENT
             | CLASSE PALAVRA_RESERVADA aninhada
             | CLASSE
    """
    pass

# def p_declaracao_classe_aninhada(p):
#     """
#     declaracao_classe : PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA ABRE_PARENT restricoes_aninhada FECHA_PARENT
#     """
#     pass

# def p_restricoes_aninhada(p):
#     """
#     restricoes_aninhada : PROPRIEDADE PALAVRA_RESERVADA CLASSE
#                         | PROPRIEDADE PALAVRA_RESERVADA ABRE_PARENT CLASSE PALAVRA_RESERVADA aninhada
#                         | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE restricoes_aninhada
#                         | PALAVRA_RESERVADA ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE FECHA_PARENT restricoes_aninhada
#     """
#     pass
#                         #| PROPRIEDADE PALAVRA_RESERVADA CLASSE restricoes_aninhada

# def p_aninhada(p):
#     """
#     aninhada : ABRE_PARENT CLASSE PALAVRA_RESERVADA CLASSE FECHA_PARENT
#               | ABRE_PARENT CLASSE PALAVRA_RESERVADA aninhada FECHA_PARENT
#               | CLASSE PALAVRA_RESERVADA aninhada 
#               | CLASSE
#     """
#     pass

#================================================================

# def p_declaracao_classe_aninhada(p): 
#      """declaracao_classe_aninhada : PALAVRA_RESERVADA CLASSE PALAVRA_RESERVADA CLASSE restricoes_aninhada"""
#      pass



# def p_restricoes_aninhada(p): 
#     """restricoes_aninhada : PALAVRA_RESERVADA ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT 
#                             |  PALAVRA_RESERVADA ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT restricoes_aninhada"""
#     pass
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
