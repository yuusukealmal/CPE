# https://onlinejudge.org/external/113/11332.pdf

def f(num):
    return sum([int(i) for i in str(num)])

while 1:
    inp  = int(input())
    if inp == 0: exit()
    while inp >= 10:
        inp = f(inp)
    print(inp)