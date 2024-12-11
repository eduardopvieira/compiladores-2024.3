# Descrição do Projeto
Esse projeto faz parte da disciplina de Compiladores da Universidade Federal Rural do Semi-Árido (UFERSA), e nele foi implementado uma versão inicial de um analisador léxico para a linguagem OWL utilizando Python.

# O que faz? Como funciona?
Em poucas palavras, o programa apenas irá percorrer toda a entrada do usuário e irá tentar encaixar cada "palavra" do código (chamados lexema), em uma expressão regular pré-definida e guardá-la em uma tabela de símbolos. No fim da execução, o programa escreve em qual expressão regular cada lexema se encaixou e diz o total.

# Requisitos
## Python 3
### - Em sistemas baseados em Debian, os seguintes comandos devem ser escritos no terminal:
`sudo apt update`
`sudo apt install python3`

### - Para sistemas Windows, é necessário ir na [página oficial do Python](www.python.org) e baixar o instalador.

# Clonando o repositório
É necessário criar uma pasta nova, abrir o terminal no diretorio da pasta criada e rodar o código:
`git clone https://github.com/eduardopvieira/compiladores-2024.3.git`

## Visual Studio Code
Link para instalação: [Clique aqui](https://code.visualstudio.com/)
### Extensões necessárias:
- Python (Microsoft)
- Pylance (Microsoft)
- Python Debugger (Microsoft)

# Como utilizar:
Para o usuário, apenas 2 arquivos são importantes:

- 'codigo.txt': Nele, o usuário irá escrever o código que deseja ser analisado pelo analisador léxico. Um código modelo já está escrito para servir como base.
- 'analisador_lexico.py': É necessário apenas rodar o arquivo normalmente no Visual Studio Code, sem nenhuma alteração. Para a execução deste arquivo, o usuário precisa estar dentro da pasta analisador-lexico-uni1 para que a resposta seja registrada sem problemas. Quando isso for feito, uma pequena interface no terminal perguntará se o código a ser analisado será lido diretamente do 'codigo.txt' ou será escrito manualmente, fica a critério do usuário escolher.

# Resultados:
Após feito o procedimento, caso tenha escolhido para escrever o código manualmente, o resultado aparecerá apenas no terminal e não será salvo em nenhum arquivo. Caso o código tenha sido lido diretamente do 'codigo.txt', o resultado será escrito nos arquivos 'resultado_analise.txt' e 'visualizacao_dados.txt'. Este primeiro tem por tarefa mostrar em qual expressão regular cada lexema no código se enquadrou e dizer quantas vezes aquele lexema apareceu. O segundo mostra quantas vezes cada token foi encontrado no codigo.
