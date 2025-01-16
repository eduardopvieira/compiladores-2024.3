import ply.lex as lex
import ply.yacc as yacc


#!======================================
#! DEFINIÇÕES DO LEXER
#!======================================
tokens = [
    "SUBCLASSOF", "EQUIVALENT_TO", "INDIVIDUALS", "DISJOINTCLASSES", "DISJOINTWITH", "COMPARADORES", "NOME_INDIVIDUO", "PALAVRA_RESERVADA", "CLASSE",
    "NAMESPACE", "TIPO", "PROPRIEDADE", "CARACTERE_ESPECIAL", "OPERADORES", "CARDINALIDADE", "ABRE_PARENT", "FECHA_PARENT", "ABRE_CHAVE", "FECHA_CHAVE",
    "OR", "AND", "SOME", "ONLY", "VALUE"
]

lista_tipos = []
#!========================== FUNÇÃO AUXILIAR DE PALAVRAS RESERVADAS ==========================
def t_SUBCLASSOF(t):
    r'SubClassOf:'
    return t

def t_INDIVIDUALS(t):
    r'Individuals:'
    return t

def t_DISJOINTCLASSES(t):
    r'DisjointClasses:'
    return t

def t_EQUIVALENT_TO(t):
    r'EquivalentTo:'
    return t

def t_OR(t):
    r'or'
    return t

def t_AND(t):
    r'and'
    return t

def t_SOME(t):
    r'some'
    return t

def t_ONLY(t):
    r'only'
    return t

def t_NAMESPACE(t):
    r'[a-z]{3,4}:'
    return t

def t_DISJOINTWITH(t):
    r'DisjointWith:'
    return t

def t_COMPARADORES(t):
    r'min|exactly|max'
    return t
def t_VALUE(t):
    r'value'
    return t

#!======================== REGEX GENERICOS =====================

t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Aa][Ll][Ll]|[Tt][Hh][Aa][Tt]|[Nn][Oo][Tt]|Class:'
t_CLASSE = r'\b([A-Z]+[a-z]+[_]?)+\b' 
t_TIPO = r'\b(rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|integer|int|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort)\b'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*' 
t_CARACTERE_ESPECIAL = r'[\[\].,\"\']'
t_OPERADORES = r'[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'
t_ABRE_PARENT = r'\('
t_FECHA_PARENT = r'\)'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
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

# INSTANCIANDO O LEXER
lexer = lex.lex()

#?======================== REGRAS PRIMÁRIAS ============================= 
def p_programa(p):
    """programa : tipo_classe_primaria programa
                | tipo_classe_primaria"""

def p_tipo_classe_primaria(p):
    """
    tipo_classe_primaria : declaracao_classe_definida
                         | declaracao_classe_primitiva
    """

def p_tipo_classe_secundaria(p):
    """
    tipo_classe_secundaria : declaracao_classe_aninhada
                          | declaracao_classe_enumerada
                          | declaracao_classe_coberta
                          | declaracao_classe_axioma_fechamento
    """


#!===================== CLASSE PRIMITIVA ================

def p_declaracao_classe_primitiva(p):
    """
    declaracao_classe_primitiva : PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_disjoint_opcional caso_individuals_opcional
                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_individuals_opcional caso_disjoint_opcional
                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_disjoint_opcional
                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof caso_individuals_opcional
                                | PALAVRA_RESERVADA CLASSE SUBCLASSOF continuacao_subclassof
    """
    #p[0] = ("{p[2]} : Classe primitiva ")
    #lista_tipos.append(f"{p[2]}: Classe primitiva ")
    p[0] = "Classe primitiva"
    lista_tipos.append(f"{p[2]}: {p[0]}")
        

def p_caso_individuals_opcional(p):
    """
    caso_individuals_opcional : INDIVIDUALS NOME_INDIVIDUO
                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals
    """
    
def p_continuacao_individuals(p):
    """
    continuacao_individuals : NOME_INDIVIDUO 
                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals
    """

def p_caso_disjoint_opcional(p):
    """
    caso_disjoint_opcional : CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
                         |  CLASSE
                         |  DISJOINTCLASSES CLASSE 
                         |  DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
                         |  DISJOINTWITH CLASSE 
                         |  DISJOINTWITH CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
    """

def p_continuacao_subclassof(p):
    """continuacao_subclassof : PROPRIEDADE SOME CLASSE
                   | CLASSE CARACTERE_ESPECIAL declaracao_classe_axioma_fechamento
                   | PROPRIEDADE SOME NAMESPACE TIPO
                   | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof 
                   | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof
    """

#!==================== CLASSE DEFINIDA ==================

def p_declaracao_classe_definida(p):
    """
    declaracao_classe_definida : PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto caso_individuals_opcional
                               | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto
                               | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof
                               | PALAVRA_RESERVADA CLASSE continuacao_subclassof EQUIVALENT_TO continuacao_equivalentto
    """

    #p[0] = ("{p[2]} : Classe Definida ")
    lista_tipos.append(f"{p[2]}: Classe Definida")


def p_continuacao_equivalentto(p):
    """
        continuacao_equivalentto : CLASSE AND ABRE_PARENT PROPRIEDADE SOME CLASSE FECHA_PARENT
                                 | CLASSE AND ABRE_PARENT PROPRIEDADE SOME restricoes_aninhada FECHA_PARENT
                                 | CLASSE AND ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT
                                 | CLASSE AND restricoes_aninhada caso_ands
                                 | CLASSE OR declaracao_classe_coberta
                                 
    """

def p_caso_simples_opcional(p):
    """
    caso_simples_opcional : CLASSE caso_ands
    """


def p_declaracao_classe_aninhada(p):
    """
    declaracao_classe_aninhada : caso_ands
    """

def p_caso_ands(p):
    """
    caso_ands : AND restricoes_aninhada caso_ands
              | AND restricoes_aninhada
              | AND restricoes_aninhada_sem_parentese caso_ands
              | AND restricoes_aninhada_sem_parentese              
    """

def p_restricoes_aninhada(p):
    """
    restricoes_aninhada : ABRE_PARENT PROPRIEDADE ONLY CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE ONLY ABRE_PARENT classes_or FECHA_PARENT FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE SOME CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT classes_or FECHA_PARENT FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT
                        | ABRE_PARENT restricoes_aninhada OR restricoes_aninhada FECHA_PARENT
    """
    lista_tipos.append(" aninhada ")
    #p[0] = (" aninhada ")

def p_restricoes_aninhada_sem_parentese(p):
    """
    restricoes_aninhada_sem_parentese :  PROPRIEDADE SOME CLASSE 
                                     |  PROPRIEDADE ONLY CLASSE 
                                     |  PROPRIEDADE ONLY restricoes_aninhada 
                                     |  PROPRIEDADE PALAVRA_RESERVADA CLASSE 
                                     |  PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE 
    """
    

def p_classes_and(p):
    """
    classes_and : CLASSE AND classes_and
                | CLASSE
    """
    


#!===================== CLASSE AXIOMA DE FECHAMENTO ========================

def p_declaracao_classe_axioma_fechamento(p):
    """
    declaracao_classe_axioma_fechamento : regras_classe_axioma_fechamento
    """
    lista_tipos.append(f"{p[0]}: fechamento ")
    #p[0] = (" fechamento ")

def p_regras_classe_axioma_fechamento(p):
    """
    regras_classe_axioma_fechamento : PROPRIEDADE SOME_ONLY CLASSE
                                    | PROPRIEDADE SOME_ONLY CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento
                                    | ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT
                                    | ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT AND regras_classe_axioma_fechamento
                                    | ABRE_PARENT PROPRIEDADE SOME_ONLY CLASSE FECHA_PARENT CARACTERE_ESPECIAL regras_classe_axioma_fechamento

                                            
                                    | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE 
                                    | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL regras_classe_axioma_fechamento
                                    | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT
                                    | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL FECHA_PARENT regras_classe_axioma_fechamento
                                        
    """
    

def p_SOME_ONLY(p):
    """
    SOME_ONLY : SOME
              | ONLY
    """


def p_classes_or(p):
    """
    classes_or : CLASSE OR classes_or
               | CLASSE
               | ABRE_PARENT classes_or FECHA_PARENT
    """

def p_classes_virgula(p):
    """
    classes_virgula : CLASSE CARACTERE_ESPECIAL classes_virgula
                    | CLASSE
    """
    


#!======================== CLASSE ENUMERADA ==========================
def p_declaracao_classe_enumerada(p):
    """
    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE
    """
    lista_tipos.append(" enumerada ")
    #p[0] = (" enumerada ")

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
    #p[0] = (" coberta ")
    lista_tipos.append(" coberta ")
    

# Erro sintático
def p_error(p):
    if p:
        linha_erro = p.lineno
        print(f"Erro sintático: token inesperado '{p.value}' do tipo '{p.type}' na linha {linha_erro}")
    else:
        print("Erro sintático: fim inesperado do arquivo")

parser = yacc.yacc(debug=True)


def executar_analisador(codigo):
    lexer.input(codigo)
    print("\n### Tokens Identificados ###")
    while True:
        token = lexer.token()
        if not token:
            break
        print(f"Token: {token.type}, Valor: {token.value}, Linha: {token.lineno}, Posição: {token.lexpos}")
    
    lexer.lineno = 1
    print("\n### Análise Sintática ###")
    result = parser.parse(codigo, lexer=lexer)   

    print("\n".join(lista_tipos))
    
    if result:
        for token in result:
            print(token)
    else:
        print("Nenhum resultado retornado pelo parser.")

# Função principal
def main():
    print("Escolha uma opção:")
    print("1 - Ler código do arquivo 'codigo.txt'")
    print("2 - Sair")
    opcao = input()

    if opcao == "1":
        try:
            with open('codigo2.txt', 'r') as arquivo:
                codigo = arquivo.read()
            executar_analisador(codigo)
        except FileNotFoundError:
            print("Erro: O arquivo 'codigo.txt' não foi encontrado.")

    elif opcao == "2":
        exit()

    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
