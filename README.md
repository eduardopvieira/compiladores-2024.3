# Analisador Semântico com PLY

Este projeto implementa um analisador semântico em Python utilizando a biblioteca [PLY (Python Lex-Yacc)](http://www.dabeaz.com/ply/). O analisador é responsável por reconhecer e validar a sintaxe de uma linguagem específica, estruturada com classes, propriedades, axiomas e outras entidades.

## Funcionalidades

- **Análise Léxica:** Identifica tokens como palavras reservadas, classes, propriedades, operadores e caracteres especiais.
- **Análise Sintática:** Processa as regras gramaticais e valida a sintaxe de classes definidas e primitivas, além de construções complexas como hierarquias de classes especializadas (enumerada, axioma de fechamento, aninhada e coberta).
- **Análise Semântica:** Identifica se as palavras e propriedades estão nos locais correspondentes para que o código faça sentido.


## Como executar 

Recomendado o uso de uma IDE como o VSCode para facilitar a visualização das saídas:

No GitHub, acesse o repositório que deseja clonar e clone o repositorio na branch alternative-main-2. Para isso, copie o código:
```bash
git clone https://github.com/eduardopvieira/compiladores-2024.3.git
```
Se ainda não tem o VSCode instalado, baixe e instale a partir do site oficial: 
https://code.visualstudio.com/.

Inicie o VSCode.

Abra o Projeto no VSCode, navegue até a pasta onde você clonou o repositório e selecione-a. Para executar o projeto, é **necessário** estar dentro da pasta "analisador-semantico-uni-3".

O arquivo principal analisador_semantico.py faz a leitura do arquivo "codigo.txt" que contem o código que será analisado. Certifique-se que o arquivo codigo.txt tem o conteudo que deseja analisar.

Os arquivos parser.out e parsertab.py são gerados automaticamente pelo PLY, portanto, não é necessário mexer em nenhum deles.

Após essas verificações, execute o arquivo analisador_semantico.py.

## Observação: 
Caso queira rodar mais de uma vez o programa é recomendado excluir o terminal anterior e executar novamente o arquivo analisador_semantico para que a saida seja correta.
A saida pode sofrer distorções caso executada mais de uma vez no mesmo terminal (possivelmente por conta da lib ply). 

## Exemplo de entrada esperada: 

    Class: Customer 
    EquivalentTo: 
        Person 
         and (purchasedPizza some Pizza) 
         and (hasPhone some xsd:string) 


## Exemplo de saída esperada: 

    Classe lida: Customer
    ============================
    Tipos: Classe definida
    
    Object Properties:
    ('purchasedPizza', 'Pizza')
    
    Data Properties:
    ('hasPhone', 'string')
    
    ERROS:

Nesse exemplo, como não há erros, 'ERROS:' não está sucedido por nada.

## Requisitos

Para executar este projeto, é necessário ter o Python 3 instalado e a biblioteca PLY. Você pode instalá-la usando o seguinte comando:

```bash
pip install ply


