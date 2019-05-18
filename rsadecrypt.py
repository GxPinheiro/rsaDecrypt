#!/usr/bin/python

n = 3386871005523622783
e = 65537

# n = p . q
#p = ?
#q = ?
#Ke = (n,e)
#Kd= (n,d)
#c=m^e mod n

#qq = (p.1)(q.1) = z
#d.e mod(qq) = 1

w = 1

for x in xrange(n):
    x = x+2
    if x == 0:
        print(x)
        break
    k = n-x
    if k == x:
        break
    else:
        f = k % x
        if f == 0:
            print(x, k)
    
print("Banan")