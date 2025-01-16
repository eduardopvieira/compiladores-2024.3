Analisador Sintático com PLY
#Descrição
Este projeto implementa um analisador léxico e sintático utilizando a biblioteca PLY (Python Lex-Yacc), projetado para processar e interpretar uma linguagem específica baseada em classes, propriedades e axiomas. A aplicação realiza a análise sintática de entradas textuais, identificando e validando estruturas como classes definidas, classes primitivas e axiomas de fechamento.

#Funcionalidades
Analisador Léxico: Identifica tokens como palavras reservadas, classes, propriedades, operadores e caracteres especiais.
Analisador Sintático: Processa as regras gramaticais e valida a sintaxe de classes definidas e primitivas, além de construções complexas como axiomas de fechamento e hierarquias de classes.
Mensagens de Erro: Reporta erros léxicos e sintáticos para ajudar na depuração.
Estrutura Modular: Separação clara entre análise léxica e sintática, permitindo fácil extensão.
Tokens Suportados
Os principais tokens reconhecidos pelo analisador incluem:

Palavras Reservadas: SubClassOf, EquivalentTo, Individuals, DisjointClasses, DisjointWith.
Operadores: and, or, some, only, value, operadores de cardinalidade (min, exactly, max).
Identificadores: Classes, propriedades, nomes de indivíduos, namespaces e tipos de dados.

#Requisitos
Python 3.8+
Biblioteca ply

Para instalar o PLY, use o seguinte comando: 
pip install ply

#Estrutura do Código
Analisador Léxico (tokens)

Define os padrões de regex para identificar os diferentes componentes da linguagem.
Implementa funções para tokens específicos como SubClassOf, EquivalentTo, e outros.
Analisador Sintático

Contém regras gramaticais principais que são :
Declarações de classes primitivas (declaracao_classe_primitiva).
Declarações de classes definidas (declaracao_classe_definida). 

As demais classes derivam delas e são:

Axioma de fechamento
classe enumerada
classe aninhada 
classe coberta
