# https://onlinejudge.org/external/102/10235.pdf

from math import sqrt

def judege(num):
    for i in range(2, int(num)):
        if num%i==0:
            return "not prime"
    if num == int(str(num)[::-1]):return "prime"
    num = int(str(num)[::-1])
    for j in range(2, num):
        if num%j==0:
            return "prime"
    return "emirp"

while 1:
    try:
        inp = int(input())
        print("{} is {}".format(str(inp), judege(inp)))
    except EOFError:
        exit()