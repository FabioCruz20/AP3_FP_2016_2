
# analisa o padrão da lista x e retorna True,
# se o padrão é válido, ou False, caso contrario.
def analisarPadrao(x):
    # imprimindo a lista x em cada chamada apenas para teste
    print(x)

    # Se o tamanho da lista é 0, ela esta vazia. Esta situação só acontece
    # quando o padrão se mostra válido para cada par de valor da lista.
    if len(x) == 0:
        return True

    # Se o tamanho da lista x não é 0, ainda há valores para verificar se
    # seguem o padrão (por isso o uso do elif). Se o par formado pelo
    # primeiro e último valores da sub-lista atual corresponde ao padrão,
    # verificamos se a condição é válida para a sub-lista obtida pela
    # exclusão do primeiro e do último elementos.

    # A sintaxe para obter essa lista é x[1: len(x) - 1], onde o valor
    # da posição len(x) - 1 não é incluído na lista do fatiamento.
    elif x[len(x) - 1] == 2 * x[0] % 10:
        analisarPadrao(x[1:len(x)-1])

    # Este caso corresponde ao fato de que os valores não correspondem
    # ao padrão.
    else:
        return False

    # Este caso 
    return True


# --------------------- programa principal ------------------- #


valores = input("Digite números separados por espaço em branco: ").split()

# converte os valores lidos para inteiro
for i in range(len(valores)):
    valores[i] = int(valores[i])


# [1,3,4,8,6,2]
print(analisarPadrao([1,4,4,8,6,2]))
