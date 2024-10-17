# https://onlinejudge.org/external/114/11417.pdf

from math import gcd

while 1:
    inp = int(input())
    if inp == 0: exit()
    G = 0
    for i in range(1,inp):
        for j in range(i+1, inp+1):
            G += gcd(i,j)
    print(G)