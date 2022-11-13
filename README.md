# **Projeto 1** - D&D-Style Combat Game 
##### **Autoria:** Ricardo de Almeida, 21807601
---
**Realização do Trabalho:** Devido à minha situação de grupo, anteriormente discutida com o professor, realizei este trabalho na sua totalidade.

**Repositório Git:** [GitHub](https://github.com/Ricardo-Louro/Projeto-IC-2022)

##### **Arquitetura da Solução:**
**Main File:**
O programa é iniciado no *Main_File.py* e começa por importar as várias funções criadas em outros documentos utilizados durante todo o processo. De seguida, define as variáveis necessárias antes do jogo começar e apresenta algum texto de boas vindas ao jogador.

De seguida, começa por iniciar o *Main_Loop*, limpar o ecrã e criar 3 listas com os objetos de número desejado (introduzidos pelo jogador), instâncias das Classes de personagens. Junta as listas de Warriors e Priests numa terçeira lista Allies para ser utilizada para a verificação de condições de derrota e ataque dos Orc Warriors.

Caso a lista Allies ou a lista de Orc Warriors estiver vazia, o *Game_Loop* não irá iniciar e o jogador será informado de acordo, tendo a opção imediata de recomeçar o jogo.

Inicializa o *Game_Loop* que acrescenta um Turno sempre que correr e corre a função *Turn_Order* que cria uma lista com os objetos ordenados. Em seguida essa lista é iterada num *For Loop* para aceder a cada objeto na ordem decidida para o turno. Em seguida, existe um sistema de *Ifs* que verifica se o objeto é um Warrior, um Orc ou um Priest e realiza as operações necessárias.

Para os Warriors, o jogador tem de introduzir se pretende utilizar um Ataque ou a Magia. Caso seja um ataque, seleciona o alvo de entre os Orc Warriors e os cálculos de dano são realizados e atualizados no valor do objeto alvo. Case seja magia, seleciona o feitiço e só de seguida poderá selecionar o alvo.

Para os Priests, o jogador tem de escolher entre Ataque e Magia de igual modo aos Warriors. No entanto, caso este selecione o feitiço *Mend*, como este é um feitiço de cura, a escolha de alvo é feita através da lista de *Allies*.

Para os Orc Warriors, estes apenas atacam aleatoriamente um elemento da lista *Allies*.

Caso alguma unidade morra após os ataques, esta é removida das listas a que pertence para que não possa agir, ser alvo de qualquer ataque/feitiço ou participar nas contagens do turno.

Após cada ação o jogo verifica se quer a lista de *Allies* ou a lista de * Orc Warriors* está vazia. Caso este seja o caso, a variável que controla o loop tem o seu valor alterado para *False* o que irá terminar o turno e o jogo imediatamente. De seguida, o jogador pode escolher recomeçar o jogo ou terminar o programa.

**Select_Units:**
Esta função é fornecida uma *string* na sua inicialização que utiliza num sistema de *Ifs* para determinar se está a ser inicializada para criar *Warriors*, *Priests* ou *Orc Warriors*. Recebe um *input* de quantos objetos da *Class* queremos e itera num range desse *input* e mete-os numa lista para poder aceder-se a cada objeto através dos índices desta. De seguida, retorna esta lista.
Desejava criar uns *Loops* para a introdução dos valores de forma a evitar erros no caso da introdução de *strings*, no entanto, não houve tempo para proceder com esta implementação.

**Turn_Order:**
Esta função junta todas as listas de unidades criadas por *Select_Units* para outra lista. Esta lista é iterada e os objetos são colocados como valores num *defaultdict* às *keys* que são o valor de *Initiative* da unidade em questão somada ao lançamento do dado. O programa vai imprimindo estas informações para o jogador perceber a ordem.
Em caso de empate, ambos os valores são atribuidos à mesma *key* pela ordem desejada (a unidade com maior valor de *Initiative* fica o primeiro índice da lista de valor). De seguida, as *keys* são ordenadas por ordem decrescente através da função *sorted()* e os valores são enviados por ordem para uma nova lista.
Esta lista ordenada tem os seus valores imprimidos para informar o jogador da ordem em que os objetos irão agir. Finalmente, esta lista é retornada.

**Unit_Classes:**
Este *script* cria as várias Classes usada no projeto, incluindo os métodos destas (os feitiços específicos de cada class).
Cada classe tem os seus valores específicos e cada método retorna um tuplo com o valor de SpellEffectValue (quantidade de dano ou heal) e o custo de mana. Estes valores são utilizados no programa principal para proceder aos cálculos necessários quando os feitiços são utilizados.

##### **Referências:**
 - [W3Schools](https://www.w3schools.com/python/) para a consulta das diversas funções e funcionalidades de Python utilizadas durante este trabalho (ex: *Class*, *isinstance()*, etc...)
 
 - [GeeksForGeeks](https://www.geeksforgeeks.org/clear-screen-python/) para a consulta de referências para problemas que não tinha encontrado previamente.
 
 - [Docs.Python](https://docs.python.org/) para a consulta de diversas funções e funcionalidades de Python de forma mais aprofundada e específica do que W3Schools., utilizado maioritariamente para perceber o *defaultdict()* e a biblioteca *os*.

 - O Apoio e Ajuda dos meus Colegas:
    - *António Rodrigues, 22202884*
    - *Henrique Monteiro, 22202855*
    - *João Silva, 22004451*
    - *Mariana Marques, 22207510*
    - *Paulo Silva, 22206205*