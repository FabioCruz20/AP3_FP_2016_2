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
            ponto = linha.split()
            # linha[0] é o valor x do ponto
            # linha[1] é o valor y do ponto
            # somaX += int(linha[0]). O operador += é um atalho
            # para a operação da linha de baixo.
            somaX = somaX + float(ponto[0])
            somaY = somaY + float(ponto[1])

            # aumenta a quantidade de pontos, se mais uma linha
            # foi lida com sucesso.
            quantPontos += 1

            # Lê mais uma linha para saber se continua no loop
            # while ou não.
            linha = entrada.readline()

        # fora do while, dentro do with open
        centroide = (somaX / quantPontos, somaY / quantPontos)

        # Formatando saída do modo antigo. Perceba que as variáveis que vão
        # substituir os símbolos %.2f DEVEM ESTAR DENTRO DE PARÊNTESES.
        # %.2f: número float com 2 dígitos depois do ponto flutuante.
        # Se quisesse 5 dígitos depois do ponto, por exemplo, usaria %.5f.
        print("Centroide: x = %.2f, y = %.2f" % (centroide[0], centroide[1]))
        # linha vazia para formatação de saída de acordo com o enunciado
        print()
    # fora do with open
    return centroide # retorna a tupla que representa o centroide


def pontosNaCircunferencia(arquivo, centroide, raio):



    with open(arquivo) as entrada:
        # Lê a primeira linha para saber se o arquivo é vazio ou não
        linha = entrada.readline()

        # string vazia significa fim do arquivo
        while linha != "":

            # para cada ponto (x,y) calculamos a distância entre esse ponto e o centróide.
            # Se a distância entre esses dois pontos for menor que o raio, significa que
            # o ponto está dentro da circunferência.
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

            # Lê mais uma linha do arquivo para dar a possibilidade de sair do loop while,
            # ou processar mais essa linha.
            linha = entrada.readline()

    # print() apenas para manter o formato de saída igual ao do enunciado.
    print()
    # fora do with open. Fim da função
    return None


# ------------------ programa principal -------------- #

# Ler o nome do arquivo conforme especificado no exemplo de
# entrada da questão.
nomeArquivo = input()

centroide = centroideDosPontos(nomeArquivo)

# Depois que lemos o conteúdo do arquivo para gerar o centróide, devemos ler valores de raio
# para determinar quais pontos do nosso arquivo de entrada estariam dentro dessa circunferência.
raio = float(input())

while raio != -1.0:
    print("Pontos na circunferência de raio %.2f" % raio)
    pontosNaCircunferencia(nomeArquivo, centroide, raio)
    print()

    raio = float(input())