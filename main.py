"""
Jogo da Forca ASCII
===================

Módulo lógico feito por Ana Carolina Erthal, Eduardo Adame, Murilo Calegari, Rodrigo Pintucci, Tiago Barradas e Vinicius Hedler. 

Módulo gráfico entregue por Juan, Lucas, Yasmin, Nicole e Carlos.

Utilizamos a função ``randbelow()`` da biblioteca padrão do python secrets para randomizar a palavra escolhida. <https://docs.python.org/3/library/secrets>

Isso foi necessário devido ao funcionamento da função ``randint()`` da biblioteca random não manter uma aleatoriedade 100% real.

A documentação formatada com Sphinx pode ser encontrada em <http://forcaascii.rtfd.io/>, que é feito com base no nosso reposítório do Github <https://github.com/adamesalles/forcaASCII>.

Instruções de jogo:

1. Tenha Python instalado na sua máquina. Nós utilizamos a versão 3.8.8 para desenvolver.
2. Certifique-se que os arquivos ``main.py``, ``modulo_grafico.py`` e ``palavras_temas.txt`` no mesmo diretório.
3. Execute o arquivo ``main.py``. No Linux (nossa plataforma de desenvolvimento), ``python3 main.py``. No Windows, ``py .\main.py``.
4. Se divirta!

Obs: se quiser adicionar palavras, não há limitação quando à açentuação ou hifenização/espaçamento em nosso software. No entanto, coloque em cada linha uma palavra e sua respectiva dica no formato "palavra;dica".
"""

# Professor, tá cheio de firula. Seja generoso conosco, por favor.

# alternativa 'mais aleatória' ao random.randint(). A biioteca secrets é padrão do python: https://docs.python.org/3/library/secrets.html
from secrets import randbelow

# importando módulo gráfico como mg. Logo, to
import modulo_grafico as mg


# Funções do menu:
def list_to_str(lista):
    """ Transforma uma lista em uma string no formato do menu. 
    Ex: 
    "0: Sair do jogo
    1: Começar novo jogo com dica
    2: Começar novo jogo sem dica"

    :param list lista: lista a ser traduzida para string no formato desejado.

    :return: string no formato desejado.
    :rtype: str

    """
    menu = ""
    n = 0
    for item in lista:
        menu += f"{n}: {item}\n"
        n += 1
    return menu


def iniciar_menu(opcoes):
    """Imprime um menu para que o usuário escolha qual opção ele quer. Retorna a opção.

    :param list opcoes: uma lista contendo as opções do jogador.

    :return: uma índice da lista, indicando a opção que o jogador escolheu.
    :rtype: int

    """
    str_opcoes = list_to_str(opcoes)
    texto_input = "Qual opção você deseja? "
    print(str_opcoes)
    while True:
        try:
            opcao = int(input(texto_input))
        # Inibe a interrupção do programa caso o usuário digite um valor inconversível para int.
        except ValueError:
            opcao = -1
        if opcao in range(len(opcoes)):
            return opcao
        else:
            texto_input = "Opção inválida.\nPor favor, escolha uma das opções: "


def sair():
    """ Última função a ser chamada pelo programa. Imprime a tela final do módulo gráfico.

    """
    mg.limpa_tela()
    mg.tela_final()
    input("Aperte enter para deixar o programa.")


def set_lista_palavras():
    """ Retorna uma lista, sendo cada item referente a uma linha do arquivo 'palavras_temas.txt'. Cada elemento será composto por uma lista de dois itens, sendo o primeiro a palavra, e o segundo a dica. Espera-se que cada linha tenha uma palavra e uma dica, separadas por um ';' (ponto e vírgula).

    :return: lista das listas das palavras e dicas que podem ser escolhidas como objetivo.
    :rtype: str

    """
    arquivo_palavras = open("palavras_temas.txt", "r")
    lista_palavras = []
    for linha in arquivo_palavras:
        lista_palavras.append(linha.rstrip("\n"))
    n = 0
    # criação de lista de listas
    for linha in lista_palavras:
        lista_palavras[n] = linha.split(";")
        n += 1
    return lista_palavras


def return_random(lista_objetos):
    """ Retorna um objeto aleatório de uma determinada lista.

    :param list lista_objetos: lista contendo os objetos dentre os quais um será retornado aleatoriamente.

    :return: um objeto aleatório da lista.

    """
    n = randbelow(len(lista_objetos))
    objeto = lista_objetos[n]
    return objeto


def retornar_alfabeto():
    """ Retorna uma lista contendo o alfabeto letra a letra.

    :return: alfabeto letra a letra em ordem alfabética.
    :rtype: list
    """
    str_letras = "abcdefghijklmnopqrstuvwxyz"
    alfabeto = []
    for letra in str_letras:
        alfabeto.append(letra)
    return alfabeto


def remover_acento(letra):
    """ Retorna uma letra sem acentuação.

    :param str letra: uma letra acentuada ou não.

    :return: letra recebida sem acentuação.
    :rtype: str
    """
    if letra.lower() in "aáàãâä":
        letra_sem_acento = "a"
    elif letra.lower() in "eéèêë":
        letra_sem_acento = "e"
    elif letra.lower() in "iíìîï":
        letra_sem_acento = "i"
    elif letra.lower() in "oóòõôö":
        letra_sem_acento = "o"
    elif letra.lower() in "uúùûü":
        letra_sem_acento = "u"
    elif letra.lower() in "cç":
        letra_sem_acento = "c"
    elif letra.lower() in "nñ":
        letra_sem_acento = "n"
    else:
        letra_sem_acento = letra
    return letra_sem_acento


def print_principal(valores_principais, dica):
    """ Print principal do jogo. Limpa a tela, imprime a forca, o estado atual da palavra que o jogador está adivinhando e a lista de TODAS as letras VÁLIDAS que o jogador já inseriu.

    :param list valores_principais: lista tendo o formato [vidas, letras_inseridas, palavra_jogador, dica_objetivo].

    :param bool dica: booleano que informa se o modo de jogo é com dica.

    """
    mg.limpa_tela()
    mg.printa_forca(valores_principais[0])
    print(*valores_principais[2], sep=" ", end="\n\n")
    if dica:
        print(f"A dica é: {valores_principais[3]}", end="\n\n")
    mg.printa_letras_inseridas(valores_principais[1])


def receber_letra(valores_principais, dica):
    """ Recebe uma letra do jogador, desde que esta letra ainda não tenha sido inserida e esteja no alfabeto.

    :param list valores_principais: lista tendo o formato [vidas, letras_inseridas, palavra_jogador, dica_objetivo].

    :param bool dica: booleano que informa se o modo de jogo é com dica.

    :return: letra recebida, em lower case, ou uma string vazia, fazendo o usuário receber uma letra ou até perder uma vida.
    :rtype: str
    """
    alfabeto = retornar_alfabeto()
    texto_input = "Insira uma letra: "
    erros = 0
    while True:
        print_principal(valores_principais, dica)
        letra = input(texto_input).lower()
        if letra in alfabeto and letra not in valores_principais[1]:
            return letra
        elif len(letra) > 1:
            texto_input = "Insira apenas um caractere: "
        elif letra in valores_principais[1]:
            texto_input = "Insira uma letra que você ainda não inseriu: "
        elif letra != remover_acento(letra):
            texto_input = "Insira uma letra sem acento: "
        elif letra[0] in "0123456789":
            texto_input = "Insira uma letra, não um número: "
        elif letra == "-":
            texto_input = "Se necessário, o hífen vem de brinde. Insira uma letra: "
        else:
            texto_input = "Eu não sei o que você digitou, mas limite-se ao alfabeto romano: "
        erros += 1
        if erros == 5:
            return ""
        elif erros == 4:
            texto_input = "Mais um erro e você perde uma vida: "
        elif erros >= 3:
            texto_input = texto_input.upper()[0:-2] + ", POR FAVOR!!! "


def atualizar_palavra_jogador(palavra_objetivo, letras_inseridas):
    """ Atualiza a palavra do jogador, inserindo nela todas as letras já inseridas até o momento.

    :param str palavra_objetivo: palavra a ser adivinhada pelo jogador.
    :param list letras_inseridas: lista das letras já inseridas pelo jogador.

    :return: palavra_objetivo, porém apenas com as letras contidas em letras_inseridas. Os espaços com letras faltantes são preenchidos por '_'.
    :rtype: str
    """
    palavra_jogador = ""
    for letra in palavra_objetivo:
        sem_acento = remover_acento(letra)
        if letra == "-" or letra == " ":  # Aceita hífen ou espaço
            palavra_jogador += letra
        elif sem_acento in letras_inseridas:
            palavra_jogador += letra
        else:
            palavra_jogador += "_"
    return palavra_jogador


def loop_jogo(palavra_objetivo, dica_objetivo, dica):
    """ Loop principal do jogo. Toma como parâmetro os objetivos do jogo e cria uma lista necessária para a função ``print_principal()``. Então começa um loop, onde:

    - Recebe uma letra do usuário através de receber_letra();
    - Insere esta letra na lista de letras já inseridas pelo usuário;
    - Cria uma variável que deixa gravada qual era a palavra do jogador até então, atualiza a palavra do jogador com a nova lista de letras inseridas e verifica se a palavra do jogador antiga é igual à nova, e caso seja, retira uma vida do usuário (normalmente tudo isto seria feito apenas checando se a letra inserida está na palavra objetivo, porém isto não funcionaria por causa da acentuação.);
    - Atualiza a lista de valores principais;
    - Chama ``print_principal()``;
    - Checa se o usuário já ganhou ou já perdeu, casos nos quais o sucesso ou fracasso do usuário retorna em um valor booleano.

    :param str palavra_objetivo: a palavra a ser adivinhada pelo usuário.

    :param str dica_objetivo: dica sobre a palavra a ser adivinhada pelo usuário.

    :param bool dica: booleano que informa se o modo de jogo é com dica.

    :return: ``True`` em caso de vitória, ``False`` em caso de derrota (do usuário).
    :rtype: bool
    """
    vidas = 6
    letras_inseridas = []
    palavra_jogador = atualizar_palavra_jogador(palavra_objetivo,
                                                letras_inseridas)
    valores_principais = [
        vidas, letras_inseridas, palavra_jogador, dica_objetivo
    ]
    while True:
        letra = receber_letra(valores_principais, dica)
        if letra != "":
            letras_inseridas.append(letra)
            letras_inseridas.sort()
        palavra_jogador_antiga = palavra_jogador
        palavra_jogador = atualizar_palavra_jogador(palavra_objetivo,
                                                    letras_inseridas)
        if palavra_jogador_antiga == palavra_jogador:
            vidas -= 1
        valores_principais = [
            vidas, letras_inseridas, palavra_jogador, dica_objetivo
        ]
        print_principal(valores_principais, dica)
        if palavra_jogador == palavra_objetivo:
            return True
        elif vidas <= 0:
            return False


def iniciar_jogo(lista_palavras, dica):
    """ Começa um jogo novo, definindo qual a nova palavra a ser adivinhada e, após retornado o sucesso do jogo, o finaliza, chamando as funções de imprimir a vitória ou a derrota do usuário.

    :param list lista_palavras: lista das palavras contidas no arquivo palavras_temas.txt.

    :param bool dica: booleano que informa se o modo de jogo é com dica.  

    """
    objetivo = return_random(lista_palavras)
    palavra_objetivo = objetivo[0]
    dica_objetivo = objetivo[1]
    sucesso = loop_jogo(palavra_objetivo, dica_objetivo, dica)
    if sucesso:
        mg.ganhou(palavra_objetivo)
    else:
        mg.perdeu(palavra_objetivo)
    input("Aperte enter para continuar")


def main():
    """
    Função mais externa do jogo da forca. Controla o fluxo do menu definindo o que será feito (sair ou jogar).

    """
    mg.abertura()
    opcoes = [
        "Sair do jogo", "Começar novo jogo com dica",
        "Começar novo jogo sem dica"
    ]
    continuar = True
    while continuar:
        mg.limpa_tela()
        opcao = iniciar_menu(opcoes)
        if opcao == 0:
            continuar = False
            sair()
        elif opcao == 1:
            lista_palavras = set_lista_palavras()
            iniciar_jogo(lista_palavras, True)
        elif opcao == 2:
            lista_palavras = set_lista_palavras()
            iniciar_jogo(lista_palavras, False)


# Protege o código de execução de terceiros
if __name__ == "__main__":
    main()

# Optamos por não utilizar a função definida como "printa_falso_acerto" por duas principais razões:
# A função não é usual no jogo da forca e nos pareceu pouco razoável com o usuário
# O texto da função é limitante: "Bom... errado você não está. Mas essa letra já foi escolhida anteriormente e você perdeu essa tentativa :D". Dizer que o usuário não está errado orienta a função para letras que pertencem à palavra, mas já foram inseridas.
# Assim, sua implementação tornaria necessária a criação de uma segunda função para letras que não pertencem à palavra, mas já foram tentadas, ou não haveria concordância com o texto. A criação de duas funções diferentes, sendo uma do módulo gráfico e uma do módulo lógico, nos pareceu uma implementação ruim.
