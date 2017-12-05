import math

# ------------------ subprogramas -------------------- #

# Obs.: a variável arquivo armazena o nome do arquivo a ser lido.
# Fórmula para calcular o centróide:
# Suponha que existam vários pontos (x,y).
# O centróide é um ponto (x,y) tal que:
# o seu valor de x é a soma dos valores de x de todos os pontos
# dividida pela quantidade de pontos, e
# o seu valor de y é a soma dos valores de y de todos os pontos
# dividida pela quantidade de pontos.

# centroide = (somaX / quantPontos, somaY / quantPontos)
# Sempre que há um problema relacionado a contar elementos,
# somar valores, e obter a média dos valores,
# devemos ter variáveis iniciadas com 0 antes que elas sejam
# usadas.

def centroideDosPontos(arquivo):

    quantPontos = 0
    somaX = 0
    somaY = 0

    # abre o arquivo no modo de leitura
    # with open(arquivo) as arq --> "r" é o modo padrão
    with open(arquivo, "r") as entrada:

        # Lê a primeira linha do arquivo para saber se ele está
        # vazio ou não
        linha = entrada.readline()

        # enquanto linha != "" (string vazia), ainda há pontos
        # para ler no arquivo
        while linha != "":
            # transforma a string em uma lista de valores x, y
            linha = linha.split()
            # linha[0] é o valor x do ponto
            # linha[1] é o valor y do ponto
            # somaX += int(linha[0]). O operador += é um atalho
            # para a operação da linha de baixo.
            somaX = somaX + float(linha[0])
            somaY = somaY + float(linha[1])

            # aumenta a quantidade de pontos, se mais uma linha
            # foi lida com sucesso.
            quantPontos += 1

            # Lê mais uma linha para saber se continua no loop
            # while ou não.
            linha = entrada.readline()

        # fora do while, dentro do with open
        centroide = (somaX / quantPontos, somaY / quantPontos)
        print("Centroide: x = %.2f, y = %.2f" % (centroide[0],
                                                 centroide[1]))
        print()
    # fora do with open
    return centroide


def pontosNaCircunferencia(arquivo, centroide, raio):



    with open(arquivo) as entrada:
        #
        linha = entrada.readline()

        while linha != "":
            ponto = linha.split()
            ponto[0] = float(ponto[0])
            ponto[1] = float(ponto[1])

            distancia = math.sqrt((ponto[0] - centroide[0])**2
                                   + (ponto[1] - centroide[1])**2)

            # verifica se o ponto está dentro da cirfunferência
            # se o sinal fosse <=, poderia haver casos em que
            # o ponto estaria na "borda" da circunferência,
            # que é quando distancia é igual ao raio.
            if distancia < raio:
                print("x = %.2f, y = %.2f" % (ponto[0], ponto[1]))

            linha = entrada.readline()

    print()
    # fora do with open. Fim da função
    return None






# ------------------ programa principal -------------- #

# Ler o nome do arquivo conforme especificado no exemplo de
# entrada da questão.
nomeArquivo = input()

centroide = centroideDosPontos(nomeArquivo)


raio = float(input())

while raio != -1.0:
    print("Pontos na circunferência de raio %.2f" % raio)
    pontosNaCircunferencia(nomeArquivo, centroide, raio)
    print()

    raio = float(input())