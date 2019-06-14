
n = 3386871005523622783
e = 65537
msgArray = [
    3273204705651769058,
    646988929665855640,
    414039851588460319,
    1564884230541949829,
    2061518062454276150,
    531123879758565307,
    577351741551993872,
    2354366801187868444,
    531123879758565307,
    1045758354504410760,
    114322492855077014,
    2087794601428009825,
    3233175618851774368,
    531123879758565307,
    2877578967909742608,
    1445428592792218022
]

def montaFrase(ascArray):
    fraseArray = []

    for letra in ascArray:
        fraseArray.append(
            chr(letra)
        )
    return fraseArray

def decriptarMsg(d, n):
    arrayDecriptado = []

    for c in msgArray:
        arrayDecriptado.append(
            pow(c, d, n)
        )
    return arrayDecriptado

def moduloInverso(e, qq):
    u1, u2, u3 = 1, 0, e
    v1, v2, v3 = 0, 1, qq

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 -q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % qq

def isPrimeNumber(x):
    if (x==3)or(x==2):
        return True
    elif ((((x+1)%6 ==0) or ((x-1)%6 ==0)) and (x>1)):
        return True
    else:
        return False


p = int(n ** 0.5)

if p % 2 != 1:
    p = p + 1

while (True):
    if isPrimeNumber(p):
        q = n/p
        if isPrimeNumber(q):
            if p*q == n:
                break

    p = p + 2

qq = (p -1) * (q -1)

d = moduloInverso(e, qq)

mensagemDecriptada = decriptarMsg(d, n)

print montaFrase(mensagemDecriptada)