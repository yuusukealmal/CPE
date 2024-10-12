# https://zerojudge.tw/ShowProblem?problemid=c039

while 1:
    try:
        inp = input()
    except EOFError:
        exit()

    first, second = int(inp.split(" ")[0]), int(inp.split(" ")[1])
    print(first, second, end=" ")
    if second < first: first, second = second, first
    def calc(n, s):
        if n == 1:
            return s + 1
        if n%2 == 0:
            s += 1
            return calc(int(n/2), s)
        else:
            s += 1
            return calc(3*n+1, s)

    ls  = []
    for i in range(first, second+1):
        s = 0
        ls.append(calc(i, s))
    print(max(ls))