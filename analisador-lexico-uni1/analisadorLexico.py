import ply.lex as lex
import ply.yacc as yacc
from tabela_de_simbolos import TabelaDeSimbolos

#https://www.dabeaz.com/ply/ply.html#ply_nn22
# Regras sintáticas
def p_programa(p):
    """programa : declaracoes"""
    pass

def p_declaracoes(p):
    """declaracoes : declaracao
                   | declaracoes declaracao"""
    pass

def p_declaracao(p):
    """declaracao : NOME_INDIVIDUO ':' CLASSE
                  | CLASSE '{' declaracoes '}'
                  | PALAVRA_RESERVADA NOME_INDIVIDUO
                  | NAMESPACE CLASSE"""
    pass

# Erro sintático
def p_error(p):
    if p:
        print(f"Erro sintático: token inesperado '{p.value}', linha {p.lineno}")
    else:
        print("Erro sintático: fim inesperado da entrada.")

# Construindo o analisador sintático
parser = yacc.yacc()

# Definição dos tokens
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
t_PALAVRA_RESERVADA = r'[Ss][Oo][Mm][Ee]|[Aa][Ll][Ll]|[Vv][Aa][Ll][Uu][Ee]|[Mm][Ii][Nn]|[Ee][Xx][Aa][Cc][Tt][Ll][Yy]|[Tt][Hh][Aa][Tt]|[Mm][Aa][Xx]|[Nn][Oo][Tt]|[Aa][Nn][Dd]|[Oo][Rr]|Class:|EquivalentTo:|Individuals:|SubClassOf:|DisjointClasses|DisjointWith:'
t_CLASSE = r'([A-Z][a-z]+[_]?)+'
t_NAMESPACE = r'[a-z]{3,4}:'
t_TIPO = r'rational|real|langString|PlainLiteral|XMLLiteral|Literal|anyURI|base64Binary|boolean|byte|dateTime|dateTimeStamp|decimal|double|float|hexBinary|integer|int|language|long|Name|NCName|negativeInteger|NMTOKEN|nonNegativeInteger|nonPositiveInteger|normalizedString|positiveInteger|short|string|token|unsignedByte|unsignedInt|unsignedLong|unsignedShort'
t_PROPRIEDADE = r'has([A-Z][a-z]+)+|is([A-Z][a-z]+)+Of|[a-z]+([A-Z][a-z]+)*'
t_CARACTERE_ESPECIAL = r'[{}\[\]().,\"\']|[<>="]{1,2}'
t_CARDINALIDADE = r'[0-9]+'

# Ignorar espaços em branco
t_ignore = ' \t\n'

def t_error(t):
    print(f"Erro léxico: token não reconhecido perto de '{t.value[:10]}'")
    t.lexer.skip(1)

# Construindo o analisador léxico
lexer = lex.lex()

def executar_analisador(codigo, tabela):
    """Executa o analisador sintático sobre o código fornecido."""
    result = parser.parse(codigo, lexer=lexer)
    lexer.input(codigo)
    for token in lexer:
        tabela.adicionar_simbolo(token.value, token.type)
    tabela.printarTabela()

def main():
    print("Escolha uma opção:")
    print("1 - Ler código do arquivo 'codigo.txt'")
    print("2 - Escrever código manualmente")
    print("3 - Sair")
    opcao = input()

    tabela = TabelaDeSimbolos()

    if opcao == "1":
        with open('codigo.txt', 'r') as arquivo:
            codigo = arquivo.read()
        executar_analisador(codigo, tabela)
        print("Resultado salvo nos arquivos 'resultado_analise.txt' e 'visualizacao_dados.txt'")

    elif opcao == "2":
        print("Digite o código:")
        codigo = input()
        executar_analisador(codigo, tabela)

    elif opcao == "3":
        exit()

    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()
