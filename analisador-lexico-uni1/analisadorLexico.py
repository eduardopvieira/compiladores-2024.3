import ply.lex as lex
import ply.yacc as yacc

# class TabelaDeSimbolos:
#     def __init__(self):
#         self.simbolos = []

#     def adicionar_simbolo(self, lexema, tipo):
#         self.simbolos.append((lexema, tipo))

#     def exibir(self):
#         print("Tabela de Símbolos:")
#         for simbolo in self.simbolos:
#             print(simbolo)

#!======================================
#! DEFINIÇÕES DO LEXER
#!======================================
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
    "ABRE_CHAVE",
    "FECHA_CHAVE",
    "EQUIVALENT_TO",
    "OR",
    "AND",
    "SUBCLASSOF",
    "INDIVIDUALS",
    "DISJOINTCLASSES",
    "SOME",
    "ONLY"
]

# Regras de expressão regular para os tokens
t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt]|[Mm][Aa][Xx]|[Nn][Oo][Tt]|Class:|DisjointWith:'
t_CLASSE = r'([A-Z][a-z]+[_]?)+' 
t_NAMESPACE = r'[a-z]{3,4}:'
t_TIPO = r'rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|integer|int|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*' 
t_CARACTERE_ESPECIAL = r'[{}\[\].,\"\']'
t_OPERADORES = r'[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'
t_ABRE_PARENT = r'\('
t_FECHA_PARENT = r'\)'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_EQUIVALENT_TO = r'EquivalentTo:'
t_OR = r'[Oo][Rr]'
t_AND = r'and'
t_SOME = r'some'
t_ONLY = r'only'
t_SUBCLASSOF = r'SubClassOf:'
t_INDIVIDUALS = r'Individuals:' 
t_DISJOINTCLASSES = r'DisjointClasses:'
t_ignore = ' \t' #ESPAÇOS EM BRANCO E TABULAÇOES

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    erro = f"Erro léxico: token não reconhecido perto de '{t.value[:10]}'\n"
    print(erro)
    with open("erros_lexicos.txt", "a") as log_file:
        log_file.write(erro)
    t.lexer.skip(1)

# INSTANCIANDO O LEXER
lexer = lex.lex()

#?======================== REGRAS PRIMÁRIAS ============================= 
def p_programa(p):
    """programa : tipo_classe_primaria programa
                | tipo_classe_primaria"""
    pass

def p_tipo_classe_primaria(p):
    """
    tipo_classe_primaria : declaracao_classe_definida
                        | declaracao_classe_primitiva
    """
    pass

def p_tipo_classe_secundaria(p):
    """
    tipo_classe_secundaria : declaracao_classe_aninhada
                          | declaracao_classe_enumerada
                          | declaracao_classe_coberta
                          | declaracao_classe_axioma_fechamento
    """
    pass

#!===================== CLASSE PRIMITIVA ================

def p_declaracao_classe_primitiva(p):
    """
    declaracao_classe_primitiva : PALAVRA_RESERVADA CLASSE caso_subclassof caso_individuals_opcional caso_disjoint_opcional
    """
    pass

def p_caso_subclassof(p):
    """
    caso_subclassof : SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA CLASSE
                   | SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO
                   | SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL continuacao_subclassof 
                   | SUBCLASSOF PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof
                   | SUBCLASSOF declaracao_classe_axioma_fechamento
    """
    pass

def p_caso_individuals_opcional(p):
    """
    caso_individuals_opcional : NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional
                             | NOME_INDIVIDUO
                             | INDIVIDUALS NOME_INDIVIDUO
                             | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL caso_individuals_opcional
    """
    pass

def p_caso_disjoint_opcional(p):
    """
    caso_disjoint_opcional : CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
                         |  CLASSE
                         |  DISJOINTCLASSES CLASSE 
                         |  DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
    """
    pass

def p_continuacao_subclassof(p):
    """continuacao_subclassof : PROPRIEDADE PALAVRA_RESERVADA CLASSE
                   | PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO
                   | PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL continuacao_subclassof 
                   | PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof
    """
    pass

#!==================== CLASSE DEFINIDA ==================

def p_declaracao_classe_definida(p):
    """
    declaracao_classe_definida : PALAVRA_RESERVADA CLASSE EQUIVALENT_TO tipo_classe_secundaria caso_individuals_opcional 
    """
    pass

def p_declaracao_classe_aninhada(p):
    """
    declaracao_classe_aninhada : caso_ands
    """
    pass

def p_caso_ands(p):
    """
    caso_ands : AND restricoes_aninhada caso_ands
              | AND restricoes_aninhada
    """
    pass

def p_restricoes_aninhada(p):
    """
    restricoes_aninhada : ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA ABRE_PARENT classes_and FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE restricoes_aninhada
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CARDINALIDADE CLASSE FECHA_PARENT restricoes_aninhada
                        | ABRE_PARENT restricoes_aninhada FECHA_PARENT"""
    pass

def p_classes_and(p):
    """
    classes_and : CLASSE AND classes_and
                | CLASSE
    """
#!===================== CLASSE AXIOMA DE FECHAMENTO ========================

def p_declaracao_classe_axioma_fechamento(p):
    """declaracao_classe_axioma_fechamento : CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento """
    pass

def p_restricoes_axioma_fechamento(p):
    """
    restricoes_axioma_fechamento : PROPRIEDADE SOME CLASSE
                                | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
                                | PROPRIEDADE ONLY ABRE_PARENT classes_or FECHA_PARENT
    """
    pass

def p_classes_or(p):
    """
    classes_or : CLASSE OR classes_or
              | CLASSE 
    """
    pass

#!======================== CLASSE ENUMERADA ==========================
def p_declaracao_classe_enumerada(p):
    """
    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE
    """
    pass

def p_classes_enumeradas(p):
    """
    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas
                      | CLASSE
    """

#!======================== CLASSE COBERTA ============================

def p_declaracao_classe_coberta(p):
    """
    declaracao_classe_coberta : classes_or
    """
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
