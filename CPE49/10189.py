# https://onlinejudge.org/external/101/10189.pdf

index = 1
first = False
while 1:
    size = input()
    if size == "0 0": break
    x ,y = int(size.split(" ")[0]) , int(size.split(" ")[1])
    if first==False: first = True
    else: print()
    ls = []

    def calc(ls, j, k):
        t = 0
        dire = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i in dire:
            try:
                nj, nk = j+i[0], k+i[1]
                if nj>=0  and nk>=0:
                    if ls[j+i[0]][k+i[1]] == "*": t += 1
            except:
                pass
        return t

    for i in range(x):
        ls.append([i for i in input()])
    for j in range(x):
        for k in range(y):
            if ls[j][k] != "*":
                ls[j][k] = calc(ls, j, k)
    print("Field #{}:".format(index))
    for i in ls:
        print(*i, sep="")
    index += 1