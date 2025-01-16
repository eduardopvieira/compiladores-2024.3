# Analisador Sintático e Léxico com PLY

Este projeto implementa um analisador léxico e sintático em Python utilizando a biblioteca [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/). O analisador é responsável por reconhecer e validar a sintaxe de uma linguagem específica, estruturada com classes, propriedades, axiomas e outras entidades.

## Funcionalidades

- **Análise Léxica:** Identificação de tokens como palavras-chave, operadores, classes, propriedades e mais.
- **Análise Sintática:** Construção e validação da estrutura gramatical com base em regras definidas.
- **Suporte a Classes:** Declaração e diferenciação entre classes primitivas e definidas.
- **Axiomas de Fechamento:** Identificação de regras e propriedades para fechamento semântico.
- **Tratamento de Erros:** Registro de erros léxicos em um arquivo separado para facilitar a depuração.

## Estrutura do Código

- **Lexer:** Define os tokens utilizando expressões regulares. Exemplos de tokens:
  - `SUBCLASSOF`, `EQUIVALENT_TO`, `AND`, `OR`
  - Identificadores como `CLASSE`, `NOME_INDIVIDUO` e `PROPRIEDADE`
- **Parser:** Implementa as regras gramaticais da linguagem utilizando produções como:
  - Declaração de classes primitivas e definidas
  - Conjuntos de disjunção e indivíduos
  - Expressões complexas com axiomas de fechamento

## Principais Tokens

| Token              | Descrição                                                    |
|--------------------|------------------------------------------------------------|
| `SUBCLASSOF`       | Define uma relação de subclasse entre classes                |
| `EQUIVALENT_TO`    | Declara classes equivalentes                                 |
| `INDIVIDUALS`      | Lista indivíduos de uma classe                               |
| `DISJOINTCLASSES`  | Declara classes disjuntas                                    |
| `NOME_INDIVIDUO`   | Identificador de indivíduos                                  |
| `CLASSE`           | Identificador de classes                                    |
| `PROPRIEDADE`      | Define propriedades de classe ou relação                    |
| `AND`, `OR`, `SOME`| Conectivos lógicos                                           |

## Requisitos

Para executar este projeto, é necessário ter o Python 3 instalado e a biblioteca PLY. Você pode instalá-la usando o seguinte comando:

```bash
pip install ply
