import ply.lex as lex
import ply.yacc as yacc



#!======================================
#! DEFINIÇÕES DO LEXER
#!======================================
tokens = [
    "SUBCLASSOF", "EQUIVALENT_TO", "INDIVIDUALS", "DISJOINTS", "COMPARADORES", "NOME_INDIVIDUO", "PALAVRA_RESERVADA", "CLASSE",
    "NAMESPACE", "TIPO", "PROPRIEDADE", "CARACTERE_ESPECIAL", "OPERADORES", "CARDINALIDADE", "ABRE_PARENT", "FECHA_PARENT", "ABRE_CHAVE", "FECHA_CHAVE",
    "OR", "AND", "SOME", "ONLY", "VALUE", "PALAVRA_CLASS", "ABRE_COLCHETE", "FECHA_COLCHETE" , "TIPO_NUMERICO"
]


lista_tuplas = []
lista_erros = []

lista_dataproperty = []
lista_objectproperty = []


fila_classe_de_propriedades = []
fila_classes_encontradas = []

#!========================== FUNÇÃO AUXILIAR DE PALAVRAS RESERVADAS ==========================
def t_DISJOINTS(t):
    r'DisjointClasses:|DisjointWith:'
    return t

def t_SUBCLASSOF(t):
    r'SubClassOf:'
    return t

def t_PALAVRA_CLASS(t):
    r'Class:'
    return t

def t_INDIVIDUALS(t):
    r'Individuals:'
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

def t_COMPARADORES(t):
    r'min|exactly|max'
    return t

def t_VALUE(t):
    r'value'
    return t

def t_TIPO_NUMERICO(t):
    r'integer|int|long|nonNegativeInteger|positiveInteger'
    return t



#!======================== REGEX GENERICOS =====================

t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Aa][Ll][Ll]|[Tt][Hh][Aa][Tt]|[Nn][Oo][Tt]'
t_CLASSE = r'\b([A-Z]+[a-z]+[_]?)+\b' 
t_TIPO = r'\b(rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|language|Name|NCName|NMTOKEN|normalizedString|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort)\b'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*' 
t_CARACTERE_ESPECIAL = r'[.,\"\']'
t_OPERADORES = r'[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'
t_ABRE_PARENT = r'\('
t_FECHA_PARENT = r'\)'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ignore = ' \t' 

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    erro = f"Erro léxico: token não reconhecido perto de '{t.value[:10]}'\n"
    print(erro)

#INSTANCIANDO O LEXER
lexer = lex.lex()


#?======================== REGRAS PRIMÁRIAS ============================= 
def p_programa(p):
    """programa : declaracao_classe programa
                | declaracao_classe"""

def p_declaracao_classe(p):
    """
    declaracao_classe : PALAVRA_CLASS CLASSE tipo_classe_primaria
    """
    
   
    print("============================\n")
    print(f"Classe lida: {p[2]}")
    print("============================")   
    
    for valor in lista_tuplas:
       
        if valor is not None:
            if valor[0] is None and valor[1] is not None:
                print(f"Tipos: {valor[1]}")
            elif valor[0] is not None:
                print(f"Tipos: {valor[0]}")
            else:
                print("Tipos: Valor não especificado")
        else:
            print("Tipos: Valor não especificado")
    print(" ")
    print("Object Properties:")
    for op in lista_objectproperty:
        print(f" - {op}")
    print(" ")
    print("Data Properties:")
    for dp in lista_dataproperty:
        print(f" - {dp}")
    print("ERROS: ")
    for error in lista_erros:
        print(error)

    #print(f" FILA CLASSE PROP {fila_classe_de_propriedades}")
    #print(f" FILA CLASSE ENC {fila_classes_encontradas}")
    for item in fila_classes_encontradas[:]:
        if item in fila_classe_de_propriedades:
            fila_classes_encontradas.remove(item)
            fila_classe_de_propriedades.remove(item)

    if fila_classe_de_propriedades:
         for item in fila_classe_de_propriedades:
            print(f"A Classe \"{item[1]}\" não foi encontrada para o fechamento da propriedade \"{item[0]}\"")


    lista_dataproperty.clear()
    lista_objectproperty.clear()

    while fila_classe_de_propriedades:
        fila_classe_de_propriedades.pop(0)

    lista_tuplas.clear()
    fila_classes_encontradas.clear()

def p_declaracao_classe_error(p):
    """
    declaracao_classe : PALAVRA_CLASS error tipo_classe_primaria
                      | error CLASSE tipo_classe_primaria        
    """
    if p.slice[1].type == 'error':
        print(f"Linha {p.lineno(1)}: É necessária a palavra reservada 'Class'.")
    elif p.slice[2].type == 'error':
        print(f"Linha {p.lineno(2)}: A classe deve começar com SubClassOf ou EquivalentTo.")
    else:
        print(f"Linha {p.lineno(1)}: Erro na declaração da classe.")

def p_tipo_classe_primaria(p):
    """
    tipo_classe_primaria : declaracao_classe_definida
                         | declaracao_classe_primitiva
    """


#!===================== CLASSE PRIMITIVA ================

def p_declaracao_classe_primitiva(p):
    """
    declaracao_classe_primitiva : SUBCLASSOF continuacao_subclassof
    """

    lista_tuplas.append((p[2], "Classe primitiva "))



#!===================== CASO INDIVIDUALS OPCIONAL ============================


def p_continuacao_individuals(p):
    """
    continuacao_individuals : NOME_INDIVIDUO 
                            | NOME_INDIVIDUO CARACTERE_ESPECIAL continuacao_individuals
    """

#!==================== CASO DISJOINT OPCIONAL ====================================

def p_caso_disjoint_opcional(p):
    """
    caso_disjoint_opcional : DISJOINTS continuacao_disjoint_opcional INDIVIDUALS continuacao_individuals
                           | DISJOINTS continuacao_disjoint_opcional
    """
    if len(p) == 3:
        lista_erros.append(f"Linha {p.lineno(1)}:Palavra \"Individuals\" obrigatória após DisjointWith ou DisjointClasses.")


def p_caso_disjoint_opcional_error(p):
    """
    caso_disjoint_opcional : error continuacao_disjoint_opcional INDIVIDUALS continuacao_individuals
                           | DISJOINTS continuacao_disjoint_opcional error
                           | DISJOINTS continuacao_disjoint_opcional INDIVIDUALS error
    """
    if p.slice[1].type == 'error':
        print(f"Linha {p.lineno(1)}: Deve começar com DisjointClasses ou DisjointWith.")
    elif p.slice[3].type == 'error':
        print(f"Linha {p.lineno(3)}: Palavra \"Individuals\" obrigatória após DisjointWith ou DisjointClasses.")
    elif p.slice[4].type == 'error':
        print(f"Linha {p.lineno(4)}: Erro na declaração dos individuos.")


def p_continuacao_disjoint_opcional(p):
    """
    continuacao_disjoint_opcional : CLASSE CARACTERE_ESPECIAL continuacao_disjoint_opcional
                                  | CLASSE 
    """



def p_continuacao_subclassof(p):
    """continuacao_subclassof :   CLASSE caso_ands
                                | CLASSE
                                | declaracao_propriedades
                                | declaracao_propriedades caso_disjoint_opcional
                                | CLASSE CARACTERE_ESPECIAL continuacao_subclassof
                                | caso_ands
                                | ABRE_PARENT declaracao_propriedades FECHA_PARENT
                                | ABRE_PARENT declaracao_propriedades FECHA_PARENT AND continuacao_subclassof
                                | ABRE_PARENT declaracao_propriedades FECHA_PARENT CARACTERE_ESPECIAL continuacao_subclassof
                                | CLASSE caso_disjoint_opcional
                                | caso_disjoint_opcional
    """


def p_declaracao_propriedades(p):
   """
    declaracao_propriedades : declaracao_existencial declaracao_propriedades
                            | declaracao_existencial
    """
       
def p_declaracao_existencial(p):
    """""""""
    declaracao_existencial : PROPRIEDADE SOME CLASSE
                           | PROPRIEDADE ONLY ABRE_PARENT declaracao_classe_axioma_fechamento FECHA_PARENT
                           | PROPRIEDADE ONLY CLASSE
                           | PROPRIEDADE ONLY CLASSE CARACTERE_ESPECIAL declaracao_existencial
                           
                           | PROPRIEDADE SOME NAMESPACE TIPO
                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE
                           | PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL declaracao_existencial
                           | PROPRIEDADE PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE
                           | PROPRIEDADE PROPRIEDADE COMPARADORES CARDINALIDADE CLASSE CARACTERE_ESPECIAL declaracao_existencial
                           
                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO
                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO
                           | PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial

                           | PROPRIEDADE SOME NAMESPACE TIPO ABRE_COLCHETE OPERADORES
                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial
                           | PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL declaracao_existencial


                           | PROPRIEDADE PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL declaracao_existencial
                           
                           
                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE
                           | PROPRIEDADE SOME NAMESPACE TIPO CARACTERE_ESPECIAL OPERADORES CARDINALIDADE CARACTERE_ESPECIAL

                                                      
                           | PROPRIEDADE SOME NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE CARACTERE_ESPECIAL declaracao_existencial

                           
                           | PROPRIEDADE COMPARADORES CARDINALIDADE NAMESPACE TIPO_NUMERICO ABRE_COLCHETE OPERADORES CARDINALIDADE FECHA_COLCHETE
                           
    """
    
    if len(p) == 4 and p[2] == 'some':
        fila_classes_encontradas.append([p[1], p[3]])
    
    if len(p) == 6 and p[2] == 'some' and isinstance(p[3], str):  # p[0] PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL recursao
        fila_classes_encontradas.append([p[1], p[3]])

    if len(p) == 7 and p[3] == 'some' and isinstance(p[4], str):  # p[0] PROPRIEDADE PROPRIEDADE SOME CLASSE CARACTERE_ESPECIAL recursao
        fila_classes_encontradas.append([p[2], p[4]])

    if p[2] == 'only' and p[3] == '(':
        if p[4]:
            classes = p[4].split("|")

            for classe in classes:
                if classe != '(' and classe != ')':
                    fila_classe_de_propriedades.append([p[1], classe])



    if len(p) == 4:
        lista_objectproperty.append((p[1]))

    elif len(p) == 5:
        if p[2] in ["min", "max", "exactly"]:
            if p[4] in t_TIPO:
                lista_dataproperty.append((p[1], p[4]))
            else:
                lista_objectproperty.append(p[1])
        elif p[3] == "some":
            lista_dataproperty.append((p[2], p[4]))

    elif len(p) == 6:
        if p[2] in ["min", "max", "exactly"] and p[5] in t_TIPO:
            lista_dataproperty.append((p[1], p[5]))
        elif p[2] == "some":
            namespace_tipo = f"{p[3]}{p[4]}"
            if namespace_tipo in t_TIPO:
                lista_dataproperty.append((p[1], namespace_tipo))
            else:
                lista_objectproperty.append(p[1])

    elif len(p) == 7:
        namespace_tipo = f"{p[4]}{p[5]}" 
        if namespace_tipo in t_TIPO:
            lista_dataproperty.append((p[2], namespace_tipo))
        else:
            lista_objectproperty.append(p[2])

    elif len(p) >= 8:
        if p[4] in ["integer", "int", "long", "nonNegativeInteger", "positiveInteger"]:
            lista_dataproperty.append((p[1], p[4]))
        elif len(p) == 10 and p[5] in ["integer", "int", "long", "nonNegativeInteger", "positiveInteger"]:
            lista_dataproperty.append((p[1], p[5]))
    else:
        print("NAO ENTROU EM NENHUMA REGRA")
    

#!==================== CLASSE DEFINIDA ==================

def p_declaracao_classe_definida(p):
    """
    declaracao_classe_definida : EQUIVALENT_TO continuacao_equivalentto caso_disjoint_opcional
                               | EQUIVALENT_TO continuacao_equivalentto
                               | EQUIVALENT_TO declaracao_classe_enumerada
                               | EQUIVALENT_TO continuacao_equivalentto SUBCLASSOF continuacao_subclassof
    """

    lista_tuplas.append((p[2], "Classe definida"))

def p_continuacao_equivalentto(p):
    """
        continuacao_equivalentto : CLASSE OR declaracao_classe_coberta
                                 | PALAVRA_RESERVADA CLASSE EQUIVALENT_TO CLASSE declaracao_classe_aninhada 
                                 | CLASSE AND ABRE_PARENT declaracao_existencial casos_parentese FECHA_PARENT
                                 | CLASSE AND declaracao_existencial casos_parentese
                                 | CLASSE AND declaracao_existencial
                                 | CLASSE AND declaracao_existencial classes_or
                                 | CLASSE AND declaracao_existencial caso_ands
                                 | CLASSE AND declaracao_existencial classes_or caso_ands
                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT 
                                 | CLASSE AND ABRE_PARENT declaracao_existencial classes_or FECHA_PARENT caso_ands
                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT
                                 | CLASSE AND ABRE_PARENT casos_parentese declaracao_classe_aninhada FECHA_PARENT caso_ands
                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT continuacao_equivalentto
                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT 
                                 | CLASSE AND ABRE_PARENT declaracao_existencial FECHA_PARENT caso_ands
    """

def p_declaracao_classe_aninhada(p):
    """
    declaracao_classe_aninhada : caso_ands
    """
    lista_tuplas.append(("Aninhada", "Aninhada"))
def p_caso_ands(p):
    """
    caso_ands : AND casos_parentese caso_ands
              | AND casos_sem_parentese caso_ands
              | AND casos_parentese
              | AND casos_sem_parentese    
    """

def p_casos_parentese(p):
    """
    casos_parentese :  ABRE_PARENT PROPRIEDADE SOME ABRE_PARENT CLASSE classes_or FECHA_PARENT FECHA_PARENT
                      | ABRE_PARENT declaracao_existencial FECHA_PARENT
                      | ABRE_PARENT casos_parentese OR casos_parentese FECHA_PARENT
                      | ABRE_PARENT casos_parentese AND casos_parentese FECHA_PARENT
                      | ABRE_PARENT casos_parentese FECHA_PARENT
                      | ABRE_PARENT PROPRIEDADE VALUE CLASSE FECHA_PARENT
    """

def p_casos_sem_parentese(p):
    """
    casos_sem_parentese :  PROPRIEDADE ONLY casos_parentese 
                        |  PROPRIEDADE PALAVRA_RESERVADA CLASSE
                        |  declaracao_existencial
    """

#!===================== CLASSE AXIOMA DE FECHAMENTO ========================

def p_declaracao_classe_axioma_fechamento(p):
    """
    declaracao_classe_axioma_fechamento :  classes_or_fechamento 
                                        
    """
    lista_tuplas.append(("Fechamento", "Fechamento"))
    p[0] = p[1]

def p_classes_or_fechamento(p):
    """
    classes_or_fechamento : CLASSE OR classes_or_fechamento
                          | CLASSE
    """   

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}|{p[3]}" 



def p_classes_or(p):
    """
    classes_or : OR CLASSE classes_or
               | OR CLASSE
               
    """    

#!======================== CLASSE ENUMERADA ==========================
def p_declaracao_classe_enumerada(p):
    """
    declaracao_classe_enumerada : ABRE_CHAVE classes_enumeradas FECHA_CHAVE
    """
    lista_tuplas.append(("Enumerada", "Enumerada"))

def p_classes_enumeradas(p):
    """
    classes_enumeradas : CLASSE CARACTERE_ESPECIAL classes_enumeradas
                       | CLASSE
    """

#!======================== CLASSE COBERTA ============================

def p_declaracao_classe_coberta(p):
    """
    declaracao_classe_coberta : CLASSE classes_or 
    """
    lista_tuplas.append(("Coberta", "Coberta"))
    
#!============================= EXECUTAVEL ===================================

def p_error(p):
    if p:
        linha_erro = p.lineno
        print(f"Erro: token inesperado '{p.value}' do tipo '{p.type}' na linha {linha_erro}")
    else:
        print("Erro: fim inesperado do arquivo")


parser = yacc.yacc(debug=True)

def executar_analisador(codigo):
    lexer.input(codigo)
    result = parser.parse(codigo, lexer=lexer)

    i = 0
    while i < len(lista_tuplas):
        chave, valor = lista_tuplas[i]

        if chave == valor:
            if i + 1 < len(lista_tuplas):
                proxima_chave, proximo_valor = lista_tuplas[i + 1]
                if proximo_valor is not None:
                    lista_tuplas[i + 1] = (proxima_chave, proximo_valor + ', ' + (valor or ""))
            del lista_tuplas[i]
        else:
            i += 1  

#!============================= MAIN ===================================
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
