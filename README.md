# MEDISOM-SOFTWARE por Joselito Mota Júnior

MEDISOM Graphics Viewer Software 

Esse é um software de visualização de pontos gerados pelo firmaware do projeto de pesquisa Medic/Medisom que foi financiado pela Fapesb em 2015.

Basicamente este programa vai plotar o gráfico com os pontos passados desse programa.

O programa de Firmaware foi feito brilhantemente por Vitor Fernando Rezende da Silva Vidal que ao meu lado conseguiu desenvolver a integração do firmware com o software de visualização. 

Basicamente, o programa vai ler os dados passados de um arquivo .txt que foi gerado do firmaware. Este arquivo vem com uma formatação padrão para que o software possa desempenhar a sua função. 

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

Por: Joselito Mota Júnior.






