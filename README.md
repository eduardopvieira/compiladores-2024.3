#Descrição do Projeto
No projeto, está implementado uma versão inicial de um analisador léxico para a linguagem OWL utilizando Python como parte da disciplina de Compiladores.

#Requisitos
O único requisito é ter o python 3 instalado na máquina. 
Em sistemas baseados em Debian, os seguintes comandos devem ser escritos no terminal:
`sudo apt update
sudo apt install python3`

Para sistemas Windows, é necessário ir na página oficial do Python (python.org) e baixar o instalador.

#Como utilizar:

Para o usuário, apenas 2 arquivos são importantes:

-'codigo.txt': O usuário irá escrever o código que deseja ser analisado pelo analisador léxico neste arquivo. Um código modelo já está escrito para servir como base.
-'analisador_lexico.py': É necessário apenas rodar o arquivo normalmente, sem nenhuma alteração. Quando isso for feito, uma interface aparecerá perguntando se o código a ser analisado será lido diretamente do 'codigo.txt' ou será escrito manualmente, fica a critério do usuário.

Após feito o procedimento, o resultado será escrito nos arquivos 'resultado_analise.txt' e 'visualizacao_dados.txt'. Este primeiro tem por tarefa mostrar em qual expressão regular cada palavra no código se enquadrou e dizer quantas vezes aquela palavra apareceu. O segundo mostra quais foram as classes, individuos e propriedades encontrados e qual o total de cada tipo.
