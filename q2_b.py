

def mdc(a, b):
    print("a =", a, "; b =", b)
    if b > 0:
        return mdc(b, a % b)
    else:
        return a

print(mdc(200, 100))
