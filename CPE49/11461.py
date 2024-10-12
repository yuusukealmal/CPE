# https://onlinejudge.org/external/114/11461.pdf

from math import sqrt

while 1:
    try:
        inp = input()
    except EOFError:
        exit()
    a = int(inp.split(" ")[0])
    b = int(inp.split(" ")[1])

    if a==0 and b==0: break
    sum = 0
    for i in range(a, b+1):
        if sqrt(i) == int(sqrt(i)):
            sum += 1
    print(sum)