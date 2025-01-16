import ply.lex as lex
import ply.yacc as yacc


#!======================================
#! DEFINIÇÕES DO LEXER
#!======================================
tokens = [
    "SUBCLASSOF",
    "EQUIVALENT_TO",
    "INDIVIDUALS",
    "DISJOINTCLASSES",
    "DISJOINTWITH",
    "COMPARADORES",
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
    "OR",
    "AND",
    "SOME",
    "ONLY"
]


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

#!======================== REGEX GENERICOS =====================

t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Tt][Hh][Aa][Tt]|[Nn][Oo][Tt]|Class:'
t_CLASSE = r'([A-Z]+[a-z]+[_]?)+' 
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
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = (p[1], p[2])

def p_tipo_classe_primaria(p):
    """
    tipo_classe_primaria : declaracao_classe_definida
                         | declaracao_classe_primitiva
    """
    p[0] = p[1]

def p_tipo_classe_secundaria(p):
    """
    tipo_classe_secundaria : declaracao_classe_aninhada
                          | declaracao_classe_enumerada
                          | declaracao_classe_coberta
                          | declaracao_classe_axioma_fechamento
    """
    p[0] = p[1]


#!===================== CLASSE PRIMITIVA ================

def p_declaracao_classe_primitiva(p):
    """
    declaracao_classe_primitiva : PALAVRA_RESERVADA CLASSE caso_subclassof caso_disjoint_opcional caso_individuals_opcional
                                | PALAVRA_RESERVADA CLASSE caso_subclassof caso_disjoint_opcional
                                | PALAVRA_RESERVADA CLASSE caso_subclassof caso_individuals_opcional
                                | PALAVRA_RESERVADA CLASSE caso_subclassof
    """
    if len(p) == 6:  # Com caso_subclassof, caso_disjoint_opcional e caso_individuals_opcional
        p[0] = ("Classe Primitiva ", p[2], p[3], p[4], p[5])
    elif len(p) == 5:  # Com caso_subclassof e caso_disjoint_opcional
        p[0] = ("Classe Primitiva ", p[2], p[3], p[4])
    else:  # Com caso_subclassof e caso_individuals_opcional
        p[0] = ("Classe Primitiva ", p[2], p[3])


def p_caso_subclassof(p):
    """
    caso_subclassof : SUBCLASSOF PROPRIEDADE SOME CLASSE
                   | SUBCLASSOF PROPRIEDADE SOME NAMESPACE TIPO
                   | SUBCLASSOF PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof 
                   | SUBCLASSOF PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof
                   | SUBCLASSOF declaracao_classe_axioma_fechamento
    """
    if len(p) == 3:
        p[0] = p[2]
    elif len(p) == 5:
        p[0] = (p[2], p[4])
    elif len(p) == 6:
        p[0] = (p[2], p[4], p[5])
    elif len(p) == 7:
        p[0] = (p[2], p[4], p[5], p[6])
    else:
        p[0] = (p[2], p[4], p[5], p[6], p[7])

def p_caso_individuals_opcional(p):
    """
    caso_individuals_opcional : INDIVIDUALS NOME_INDIVIDUO
                              | INDIVIDUALS NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals
    """
    
def p_continuacao_individuals(p):
    """
    continuacao_individuals : NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals
                            | NOME_INDIVIDUO
    """
    
    if len(p) == 2:  # Apenas NOME_INDIVIDUO
        p[0] = p[1]
    elif len(p) == 3:  # INDIVIDUALS seguido de NOME_INDIVIDUO
        p[0] = (p[1], p[2])
    elif len(p) == 4:  # NOME_INDIVIDUO seguido de CARACTERE_ESPECIAL e caso_individuals_opcional
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 5:  # INDIVIDUALS seguido de NOME_INDIVIDUO, CARACTERE_ESPECIAL e caso_individuals_opcional
        p[0] = (p[1], p[2], p[3], p[4])
    else:  # Caso vazio (regra sem tokens)
        p[0] = None

def p_caso_disjoint_opcional(p):
    """
    caso_disjoint_opcional : CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
                         |  CLASSE
                         |  DISJOINTCLASSES CLASSE 
                         |  DISJOINTCLASSES CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
                         |  DISJOINTWITH CLASSE 
                         |  DISJOINTWITH CLASSE CARACTERE_ESPECIAL caso_disjoint_opcional
    """
                         #|  empty
    
    
    if len(p) == 2:  # Apenas CLASSE
        p[0] = p[1]
    elif len(p) == 3:  # DISJOINTWITH ou DISJOINTCLASSES seguido de CLASSE
        p[0] = (p[1], p[2])
    elif len(p) == 4:  # CLASSE seguido de CARACTERE_ESPECIAL e caso_disjoint_opcional
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 5:  # DISJOINTWITH ou DISJOINTCLASSES seguido de CLASSE, CARACTERE_ESPECIAL e caso_disjoint_opcional
        p[0] = (p[1], p[2], p[3], p[4])
    else:  # Caso vazio
        p[0] = None

def p_continuacao_subclassof(p):
    """continuacao_subclassof : PROPRIEDADE SOME CLASSE
                   | PROPRIEDADE SOME NAMESPACE TIPO
                   | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL continuacao_subclassof 
                   | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL continuacao_subclassof
    """
    if len(p) == 4:  # PROPRIEDADE SOME CLASSE ou NAMESPACE TIPO
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 6:  # PROPRIEDADE SOME CLASSE ou NAMESPACE TIPO com CARACTERE_ESPECIAL e continuacao_subclassof
        p[0] = (p[1], p[2], p[3], p[4], p[5])

#!==================== CLASSE DEFINIDA ==================

def p_declaracao_classe_definida(p):
    """
    declaracao_classe_definida : PALAVRA_RESERVADA CLASSE EQUIVALENT_TO caso_simples_opcional estrutura_definida
                               | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO estrutura_definida
    """
    if len(p) == 5:  # Com estrutura_definida apenas
        p[0] = ("Classe Definida: ", p[1], p[2], p[3], p[4])
    elif len(p) == 6:  # Com caso_simples_opcional e estrutura_definida
        p[0] = ("Classe Definida: ", p[1], p[2], p[3], p[4], p[5])

def p_estrutura_definida(p): 
    """
    estrutura_definida : caso_individuals_opcional estrutura_definida
                       | tipo_classe_secundaria estrutura_definida
                       | declaracao_classe_coberta 
    """
    if len(p) == 3:  # caso_individuals_opcional ou tipo_classe_secundaria seguido de estrutura_definida
        p[0] = (p[1], p[2])
    elif len(p) == 2:  # Apenas declaracao_classe_coberta
        p[0] = p[1]
    else:  # Caso vazio
        p[0] = None

def p_caso_simples_opcional(p):
    """
    caso_simples_opcional : CLASSE caso_ands
    """
                          #| empty
    if len(p) == 3:  # CLASSE seguido de caso_ands
        p[0] = (p[1], p[2])
    else:  # Caso vazio
        p[0] = None

def p_declaracao_classe_aninhada(p):
    """
    declaracao_classe_aninhada : caso_ands
    """
    p[0] = p[1]

def p_caso_ands(p):
    """
    caso_ands : AND restricoes_aninhada caso_ands
              | AND restricoes_aninhada
              | AND restricoes_aninhada_sem_parentese caso_ands
              | AND restricoes_aninhada_sem_parentese              

    """
    if len(p) == 3:  # AND seguido de restricoes_aninhada ou restricoes_aninhada_sem_parentese
        p[0] = (p[1], p[2])
    elif len(p) == 4:  # AND seguido de restricoes_aninhada ou restricoes_aninhada_sem_parentese e caso_ands
        p[0] = (p[1], p[2], p[3])

def p_restricoes_aninhada(p):
    """
    restricoes_aninhada : ABRE_PARENT PROPRIEDADE SOME CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE ONLY CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE ONLY restricoes_aninhada FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE PALAVRA_RESERVADA CLASSE FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT classes_and FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE SOME restricoes_aninhada FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE SOME CARDINALIDADE CLASSE FECHA_PARENT restricoes_aninhada
                        | ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT
                        | ABRE_PARENT PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL FECHA_PARENT CARACTERE_ESPECIAL restricoes_aninhada
                        | ABRE_PARENT PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE FECHA_PARENT
                        | ABRE_PARENT restricoes_aninhada FECHA_PARENT
                        | ABRE_PARENT restricoes_aninhada caso_ands FECHA_PARENT
                        | ABRE_PARENT classes_or FECHA_PARENT"""
    if len(p) == 6:  # Casos básicos com FECHA_PARENT
        p[0] = (p[2], p[3], p[4])
    elif len(p) == 7:  # restricoes_aninhada com ABRE_PARENT ou casos com ONLY/SOME
        p[0] = (p[2], p[3], p[4], p[5])
    elif len(p) == 8:  # Casos com restricoes_aninhada e CARDINALIDADE
        p[0] = (p[2], p[3], p[4], p[5], p[6])
    elif len(p) == 9:  # NAMESPACE e TIPO com CARACTERE_ESPECIAL
        p[0] = (p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    elif len(p) == 10:  # NAMESPACE com TIPO, OPERADORES e CARDINALIDADE
        p[0] = (p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9])
    elif len(p) == 11:  # NAMESPACE e TIPO com operadores extras
        p[0] = (p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10])
    elif len(p) == 12:  # Casos aninhados com CARACTERE_ESPECIAL e restricoes_aninhada
        p[0] = (p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11])
    elif len(p) == 4:  # restricoes_aninhada simples entre parênteses
        p[0] = (p[2],)
    elif len(p) == 5:  # restricoes_aninhada com caso_ands
        p[0] = (p[2], p[3])
    else:  # Caso com classes_or
        p[0] = p[2]

def p_restricoes_aninhada_sem_parentese(p):
    """
    restricoes_aninhada_sem_parentese :  PROPRIEDADE SOME CLASSE 
                                     |  PROPRIEDADE ONLY CLASSE 
                                     |  PROPRIEDADE ONLY restricoes_aninhada 
                                     |  PROPRIEDADE PALAVRA_RESERVADA CLASSE 
                                     |  PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE 
    """
    if len(p) == 4: 
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = (p[1], p[2], p[3], p[4])
    else:
        p[0] = None

def p_classes_and(p):
    """
    classes_and : CLASSE AND classes_and
                | CLASSE
    """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]


#!===================== CLASSE AXIOMA DE FECHAMENTO ========================

def p_declaracao_classe_axioma_fechamento(p):
    """declaracao_classe_axioma_fechamento : CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento"""
    if len(p) == 4:  # CLASSE seguida de CARACTERE_ESPECIAL e restrições
        p[0] = (p[1], p[2], p[3])

def p_restricoes_axioma_fechamento(p):
    """
    restricoes_axioma_fechamento : casos_propriedade ONLY ABRE_PARENT classes_or FECHA_PARENT
                                 | casos_propriedade SOME CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
                                 | casos_propriedade SOME CLASSE
                                 | casos_propriedade ONLY CLASSE 
                                 | casos_propriedade ONLY CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
                                 | casos_propriedade COMPARADORES CARDINALIDADE CLASSE
                                 | casos_propriedade COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
                                 | ABRE_PARENT restricoes_axioma_fechamento FECHA_PARENT 
                                 | ABRE_PARENT restricoes_axioma_fechamento FECHA_PARENT AND restricoes_axioma_fechamento
                                 | ABRE_PARENT restricoes_axioma_fechamento FECHA_PARENT CARACTERE_ESPECIAL restricoes_axioma_fechamento
                                 
    """
    if len(p) == 6 and p[2] == "ONLY" and p[3] == "ABRE_PARENT":  # casos_propriedade ONLY (classes_or)
        p[0] = (p[1], p[2], p[4])
    elif len(p) == 6:  # casos_propriedade SOME CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
        p[0] = (p[1], p[2], p[3], p[5])
    elif len(p) == 4:  # casos_propriedade SOME/ONLY CLASSE
        p[0] = (p[1], p[2], p[3])
    elif len(p) == 7:  # casos_propriedade COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL restricoes_axioma_fechamento
        p[0] = (p[1], p[2], p[3], p[4], p[6])
    elif len(p) == 5:  # casos_propriedade COMPARADORES CARDINALIDADE CLASSE
        p[0] = (p[1], p[2], p[3], p[4])
    elif len(p) == 4 and p[1] == "ABRE_PARENT":  # (restricoes_axioma_fechamento)
        p[0] = p[2]
    elif len(p) == 6 and p[4] == "AND":  # (restricoes_axioma_fechamento) AND restricoes_axioma_fechamento
        p[0] = (p[2], "AND", p[5])
    elif len(p) == 6:  # (restricoes_axioma_fechamento) CARACTERE_ESPECIAL restricoes_axioma_fechamento
        p[0] = (p[2], p[4])
    else:
        p[0] = None

def p_casos_propriedade(p):
    """
    casos_propriedade : PROPRIEDADE PROPRIEDADE
                      | PROPRIEDADE
    """
    if len(p) == 3:  # Dois PROPRIEDADE
        p[0] = (p[1], p[2])
    elif len(p) == 2:  # Um PROPRIEDADE
        p[0] = p[1]

def p_classes_or(p):
    """
    classes_or : CLASSE OR classes_or
              | CLASSE 
    """
    if len(p) == 2:  # Uma única classe
        p[0] = [p[1]]
    elif len(p) == 4:  # CLASSE OR outras classes
        p[0] = [p[1]] + p[3]


#!======================== CLASSE ENUMERADA ==========================
def p_declaracao_classe_enumerada(p):
    """
    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE
    """
    if len(p) == 4:  # { classes_enumeradas }
        p[0] = p[2]

def p_classes_enumeradas(p):
    """
    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas
                       | CLASSE
    """
    if len(p) == 2:  # Uma única classe
        p[0] = [p[1]]
    elif len(p) == 4:  # CLASSE CARACTERE_ESPECIAL outras classes
        p[0] = [p[1]] + p[3]

#!======================== CLASSE COBERTA ============================

def p_declaracao_classe_coberta(p):
    """
    declaracao_classe_coberta : classes_or 
    """
    if len(p) == 2:  # Apenas classes_or
        p[0] = p[1]


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
    if result:
        for token in result:
            print(token)
    else:
        print("Nenhum resultado retornado pelo parser.")



# def executar_analisador_manual(cod_teste):
#     lexer.input(cod_teste)
#     print("\n### Tokens Identificados ###")
#     while True:
#             token = lexer.token()
#             if not token:
#                 break
#             print(f"Token: {token.type}, Valor: {token.value}, Linha: {token.lineno}, Posição: {token.lexpos}")
        
#     # Processa o parser
#     print("\n### Análise Sintática ###")
#     result = parser.parse(cod_teste, lexer=lexer)
#     if result:
#         for token in result:
#             print(token)
#     else:
#         print("Nenhum resultado retornado pelo parser.")



cod_teste = """ Class: SpicyPizza
 EquivalentTo:
 Pizza
 and (hasTopping some (hasSpiciness value Hot))"""

# Função principal
def main():
    print("Escolha uma opção:")
    print("1 - Ler código do arquivo 'codigo.txt'")
    print("2 - Sair")
    opcao = input()

    if opcao == "1":
        try:
            with open('codigo.txt', 'r') as arquivo:
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
