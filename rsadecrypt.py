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

def isPrime(n):
    if n < 2:
        return False

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return False

    return True

w = 1
p = int(0)
q = int(0)

for x in range(n):
    x = int(x+2087378595)
    if isPrime(x):
        k = int(n/x)
        if isPrime(k):
            j = int(x * k)
            if n == j:
                p = int(x)
                q = int(k)
                print("P = ", q)
                print("Q = ", q)
                break

qq = int((p-1)*(q-1))
print("QQ = ", qq)
d = int(0)
for y in range(qq):
    y  = int(y+489242836476650830)
    h = int(y*e%qq)
    if(h == 1):
        print("D = ", y)
        d = y
        break

print(d)
a = 3273204705651769058**d
print(a)
b = a%n
print(b)
# print((3273204705651769058**d)%n)
# print((646988929665855640**d)%n)
# print((414039851588460319**d)%n)
# print((1564884230541949829**d)%n)
# print((2061518062454276150**d)%n)
# print((531123879758565307**d)%n)
# print((577351741551993872**d)%n)
# print((2354366801187868444**d)%n)
# print((531123879758565307**d)%n)
# print((1045758354504410760**d)%n)
# print((114322492855077014**d)%n)
# print((2087794601428009825**d)%n)
# print((3233175618851774368**d)%n)
# print((531123879758565307**d)%n)
# print((2877578967909742608**d)%n)
# print((1445428592792218022**d)%n)


print("Banana")