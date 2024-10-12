# https://onlinejudge.org/external/101/10190.pdf

while 1:
    try:
        inp = input()
    except EOFError:
        exit()
    first, div = int(inp.split(" ")[0]), int(inp.split(" ")[1])
    if div == 1:
        print("Boring!")
        continue
    ls = []
    ls.append(first)

    while first // div != 0:
        first //= div
        ls.append(first)

    def calc(ls):
        for i in range(0, len(ls)):
            if ls[i] % div != 0 and ls[i] != 1:
                return False
        return True

    if calc(ls):
        print(*ls)
    else:
        print("Boring!")