
# Nesta função, o que eu fiz foi basicamente transformar a
# definição do enunciado em código python.

def mdc(a, b):
    if b > 0:
        return mdc(b, a % b)

    # O caso base é quando b == 0, que corresponde ao else
    else:
        return a


# ------------------ programa principal ------------------- #

# Lê dois números inteiros na mesma linha

a = int(input("Digite um numero inteiro: "))
b = int(input("Digite um numero inteiro: "))
result = mdc(a, b)

print("mdc(%d, %d) = %d" % (a, b, result) )

