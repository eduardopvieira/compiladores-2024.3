# Descrição do Projeto
Esse projeto faz parte da disciplina de Compiladores da Universidade Federal Rural do Semi-Árido (UFERSA), e nele foi implementado uma versão inicial de um analisador léxico para a linguagem OWL utilizando Python.

# Requisitos
## Python 3
### - Em sistemas baseados em Debian, os seguintes comandos devem ser escritos no terminal:
`sudo apt update`
`sudo apt install python3`

### - Para sistemas Windows, é necessário ir na [página oficial do Python](python.org) e baixar o instalador.

## Visual Studio Code
Link para instalação: [Clique aqui](https://code.visualstudio.com/)
### Extensões necessárias:
- Python (Microsoft)
- Pylance (Microsoft)
- Python Debugger (Microsoft)

# Como utilizar:
Para o usuário, apenas 2 arquivos são importantes:

- 'codigo.txt': Nele, o usuário irá escrever o código que deseja ser analisado pelo analisador léxico. Um código modelo já está escrito para servir como base.
- 'analisador_lexico.py': É necessário apenas rodar o arquivo normalmente, sem nenhuma alteração. Quando isso for feito, uma pequena interface no terminal perguntará se o código a ser analisado será lido diretamente do 'codigo.txt' ou será escrito manualmente, fica a critério do usuário escolher. Para a execução deste arquivo, o usuário precisa estar dentro da pasta analisador-lexico-uni1 para que a resposta seja registrada sem problemas.


# Resultados:
Após feito o procedimento, caso tenha escolhido para escrever o código manualmente, o resultado aparecerá apenas no terminal e não será salvo em nenhum arquivo. Caso o código tenha sido lido diretamente do 'codigo.txt', o resultado será escrito nos arquivos 'resultado_analise.txt' e 'visualizacao_dados.txt'. Este primeiro tem por tarefa mostrar em qual expressão regular cada palavra no código se enquadrou e dizer quantas vezes aquela palavra apareceu. O segundo mostra quais foram as classes, individuos e propriedades encontrados e qual o total de cada tipo.
