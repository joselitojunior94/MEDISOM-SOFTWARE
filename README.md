# MEDISOM / MEDIC GRAPHICS VIEWER SOFTWARE

Projeto Medisom / Medic é composto por : 

 - Paul Denis  Etienne Regnier - Orientador
 - Camila Moura Ferreira Santos - Aluna de Mestrado pela UFBA
 - Joselito Mota Júnior - Aluno de Iniciação Cientifica.
 - Luan da Cruz Silva - Aluno de Iniciação Cientifica.
 - Vitor Fernando Rezende da Silva Vidal - Aluno de Iniciação Cientifica.
 
Medisom é uma plataforma mecatrônica de Medição para Estudos de Campos de Radiações Ultrassônicas.

Os membros do projeto trabalharam para que cada parte fosse feita( Hardware, Firmware e Software). 

Para mais informações sobre a parte mecânica ou o escopo do projeto, veja o vídeo para o DCC Demo Day em: https://youtu.be/EecQuuVCOqs ou leia o relatório que está disponível acima.

Cada aluno ficou responsável por módulos do projeto: Hardware, Firmware e Software. 

Este código é referente só sobre o Software, parte em que trabalhei neste projeto. Portanto, tratarei apenas sobre a aplicação de visualização. 

Esse é um software de visualização de pontos gerados pelo firmware do projeto de pesquisa Medic/Medisom que foi financiado pela Fapesb em 2015.

Basicamente este programa vai plotar o gráfico com os pontos passados desse programa.

O programa de Firmware foi feito brilhantemente por Vitor Fernando Rezende da Silva Vidal que ao meu lado conseguiu desenvolver a integração do firmware com o software de visualização. 

O programa de visualização vai ler os dados passados de um arquivo .txt que foi gerado do firmware. Este arquivo vem com uma formatação padrão para que o software possa desempenhar a sua função. 

A formação é:

Diâmetro do duto

X;Y;Z;intensidade

Se o arquivo estiver fora desta formatação, a plotagem do gráfico vai estar errada! Portanto, se atentem para que o formato do arquivo esteja certo!

A biblioteca TKinter para desenho das janelas e a a Matplotlib foi utilizada.

Conheça mais sobre Matplotlib  e a TKinter em: http://matplotlib.org/ e https://wiki.python.org/moin/TkInter

Recomendo a utilização da Matplotlib pois é uma biblioteca muito bem documentada e com vários exemplos disponíveis na internet.  Esses exemplos me ajudou bastante a fazer este software de visualização. 

Exemplos que são encontrados aqui: http://matplotlib.org/examples/index.html

Lembrando que o código está disponível neste Github, mas se utiliza - lo por favor deixar as devidas referências pelo meu trabalho.

Instalação:

Lembrando que por se tratar de uma proposta livre(proposta utilizada no projeto de pesquisa), o software só é compatível com sistemas Linux. Por tanto, a instação será feita em sistemas linux. 

Os sistemas operacionais que utilizei  para o desenvolvimento e teste foram: Debian e Ubuntu.

Veja o guia de instalação do idle 2.7(https://www.python.org/) e do Matplotlib(http://matplotlib.org/contents.html). Pacotes necessários para rodar o software.

Com o idle e o matplotlib instalado, é hora de rodar a aplicação. 

Aperte F5 para que o interpretador Python rode o programa.

A primeira tela é a tela de inserir o .txt. Procure pelo computador utilizando a caixa de seleção.

Depois de encontrado, clique em Abrir.

A tela de seleção de pontos vai estar pronta para uso. 

Mais informações só sequir o relatório que está neste repositório. Lá mostra as telas e detalha sobre todo o processo do projeto.

O SOFTWARE É APRESENTADO NO ESTADO EM QUE SE ENCONTRA, SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA. EM NENHUMA CIRCUNSTÂNCIA OS AUTORES SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE. O USO DO SOFTWARE É POR CONTA E RISCO DO USUÁRIO.






