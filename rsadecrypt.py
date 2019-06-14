#!/usr/bin/python
# n = p . q
#p = ?
#q = ?
#Ke = (n,e)
#Kd= (n,d)
#c=m^e mod n

#qq = (p.1)(q.1) = z
#d.e mod(qq) = 1
from math import sqrt; from itertools import count, islice
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

def createPhrase(array):
    phrase = ""
    for l in array:
        phrase = phrase + chr(l)
    print(phrase)

def decryptArray(d, n):
    arrayDecrypt = []

    for c in msgArray:
        arrayDecrypt.append(
            pow(c, d, n)
        )
    return arrayDecrypt

def modInverse(e,qq):
	g,x,y = eqq(e,qq)
	if g != 1:
		return None
	else:
		return x%qq

def eqq(e, qq):
	if e == 0:
		return (qq, 0, 1)
	else:
		g, y, x = eqq(qq % e, e)
		return (g, x - (qq // e) * y, y)

w = 1
p = int(0)
q = int(0)
x = int(sqrt(n))
if((x & 1) == 0):
    x = x-1
x = int(x)
while True:
    if(n%x == 0):
        p = x
        q = n/x
        print("Q:",q)
        print("P:",p)
        break
    x = x+2

qq = int((p-1)*(q-1))
print("QQ:", qq)

d = modInverse(e, qq)

print("D:", d)

msgDecrypt = decryptArray(d, n)
createPhrase(msgDecrypt)
