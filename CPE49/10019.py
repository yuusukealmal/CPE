# https://onlinejudge.org/external/100/10019.pdf

for i in range(int(input())):
    M = int(input())
    x1 = bin(M)[2:].count("1")
    x2 = bin(int(str(M),16))[2:].count("1")
    print(x1, x2)