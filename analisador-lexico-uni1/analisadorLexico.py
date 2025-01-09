import ply.lex as lex
import ply.yacc as yacc

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
t_NAMESPACE = r'[a-z][a-z][a-z]:|[a-z][a-z][a-z][a-z]:'
t_NOME_INDIVIDUO = r'([A-Z][a-z]+)+[0-9]+'
t_PALAVRA_RESERVADA = r'[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt]|[Mm][Aa][Xx]|[Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses:|DisjointWith:|and|some'
t_CLASSE = r'([A-Z][a-z]+[_]?)+'
t_TIPO = r'integer|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|rational|int|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*'
t_CARACTERE_ESPECIAL = r'[{}\[\]().,\"\']|[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'
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
    """programa : declaracao_classe"""
    pass

# Classe Primitiva
def p_classe_primitiva(p):
    """declaracao_classe : PALAVRA_RESERVADA CLASSE obrigatorio_subclassof caso_disjointclasses caso_individuals"""
    p[0] = {
        "palavra_reservada": p[1],
        "classe": p[2],
        "subclassof": p[3],
        "disjoint_classes": p[4],
        "individuals": p[5]
    }

def p_obrigatorio_subclassof(p):
    """obrigatorio_subclassof : PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE
                       | PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO
                       | PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL outra_propriedade
                       | PALAVRA_RESERVADA PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_propriedade"""
    if len(p) == 5:
        p[0] = ("SubClassOf", p[2], p[4])
    elif len(p) == 6:
        p[0] = ("SubClassOf", p[2], (p[4], p[5]))
    else:
        p[0] = ("SubClassOf", p[2], p[4], p[6])


def p_outra_propriedade(p):
    """outra_propriedade : PROPRIEDADE PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_propriedade
                         | PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO CARACTERE_ESPECIAL outra_propriedade
                         | PROPRIEDADE PALAVRA_RESERVADA CLASSE
                         | PROPRIEDADE PALAVRA_RESERVADA NAMESPACE TIPO"""
    if len(p) == 4:
        p[0] = [{"propriedade": p[1], "classe": p[3]}]
    elif len(p) == 5:
        p[0] = [{"propriedade": p[1], "tipo": p[4]}]
    else:
        p[0] = [{"propriedade": p[1], "classe": p[3], "outra_propriedade": p[5]}]

def p_caso_disjointclasses(p):
    """caso_disjointclasses : PALAVRA_RESERVADA CLASSE
                            | PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL outra_classe"""
    if len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[4]

def p_outra_classe(p):
    """outra_classe : CLASSE
                    | CLASSE CARACTERE_ESPECIAL outra_classe"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_caso_individuals(p):
    """caso_individuals : PALAVRA_RESERVADA NOME_INDIVIDUO
                        | PALAVRA_RESERVADA NOME_INDIVIDUO CARACTERE_ESPECIAL outro_individuo"""
    if len(p) == 3:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[4]

def p_outro_individuo(p):
    """outro_individuo : NOME_INDIVIDUO
                       | NOME_INDIVIDUO CARACTERE_ESPECIAL outro_individuo"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# Função de erro
def p_error(p):
    print(f"Erro de sintaxe em '{p.value}'" if p else "Erro de sintaxe inesperado.")

# # Classe Enumerada
# def p_declaracao_classe_enumerada(p):
#     """declaracao_classe : PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL CARACTERE_ESPECIAL lista_individuos CARACTERE_ESPECIAL"""
#     pass

# def p_lista_individuos(p):
#     """lista_individuos : NOME_INDIVIDUO
#                          | lista_individuos CARACTERE_ESPECIAL NOME_INDIVIDUO"""
#     pass

# # Classe Coberta
# def p_declaracao_classe_coberta(p):
#     """declaracao_classe : PALAVRA_RESERVADA CLASSE CARACTERE_ESPECIAL lista_classes"""
#     pass

# def p_lista_classes(p):
#     """lista_classes : CLASSE
#                       | lista_classes PALAVRA_RESERVADA CLASSE"""
#     pass


def p_error(p):
    if p:
        print(f"Erro sintático: token inesperado '{p.value}' de tipo '{p.type}'")
        with open("token_log.txt", "a") as log:
            log.write(f"Erro sintático: token inesperado '{p.value}' de tipo '{p.type}'\n")
    else:
        print("Erro sintático: fim inesperado do arquivo.")
        with open("token_log.txt", "a") as log:
            log.write("Erro sintático: fim inesperado do arquivo.\n")



def log_token(token):
    with open("token_log.txt", "a") as log:
        log.write(f"{token.type}: {token.value}\n")



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
