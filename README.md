# Analisador Sintático e Léxico com PLY

Este projeto implementa um analisador léxico e sintático em Python utilizando a biblioteca [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/). O analisador é responsável por reconhecer e validar a sintaxe de uma linguagem específica, estruturada com classes, propriedades, axiomas e outras entidades.

## Funcionalidades

- **Análise Léxica:** Identifica tokens como palavras reservadas, classes, propriedades, operadores e caracteres especiais.
- **Análise Sintática:** Processa as regras gramaticais e valida a sintaxe de classes definidas e primitivas, além de construções complexas como hierarquias de classes especializadas (enumerada, axioma de fechamento, aninhada e coberta).

## Estrutura do Código

- **Lexer:** Define os tokens utilizando expressões regulares. Exemplos de tokens:
  - `SUBCLASSOF`, `EQUIVALENT_TO`, `AND`, `OR`
  - Identificadores como `CLASSE`, `NOME_INDIVIDUO` e `PROPRIEDADE`
- **Parser:** Implementa as regras gramaticais da linguagem utilizando produções como:
  - Declaração de classes primitivas e definidas
  - Conjuntos de disjunção e indivíduos
  - Expressões complexas com axiomas de fechamento e tipos secundarios ...

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




## Como executar 

Recomendado o uso de uma IDE como o VSCode para facilitar a visualização das saídas:

Se ainda não tem o VSCode instalado, baixe e instale a partir do site oficial: 
https://code.visualstudio.com/.

Abra o Projeto no VSCode, navegue até a pasta onde você clonou o repositório e selecione-a e 
execute o arquivo analisador_sintatico.py.

## Requisitos

Para executar este projeto, é necessário ter o Python 3 instalado e a biblioteca PLY. Você pode instalá-la usando o seguinte comando:

```bash
pip install ply

