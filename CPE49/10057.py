# https://onlinejudge.org/external/100/10057.pdf

while 1:
    try:
        a, b, c = 0, 0, 0
        inp = input()
        ls = []
        for i in range(int(inp)):
            ls.append(int(input()))
        ls.sort()
        if len(ls) % 2 == 0:
            c = ls[int(len(ls)//2)] - ls[int(len(ls)//2)-1]+1
            a1 = ls[int(len(ls)//2)-1]
            a2 = ls[int(len(ls)//2)]
        else:
            c = 1
            a1 = ls[int(len(ls)//2)]
            a2 = 0
        if a1==a2: b = ls.count(a1)
        else: b = ls.count(a1) + ls.count(a2)
        print("{} {} {}".format(a1, b, c))
    except EOFError:
        exit()