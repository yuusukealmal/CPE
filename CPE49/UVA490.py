# https://zerojudge.tw/ShowProblem?problemid=c045

ls = []
while 1:
    try:
        ls.append(input())
    except EOFError:
        break
ls.reverse()
for i in range(len(max(ls, key=len))):
    for j in range(len(ls)):
        try:
            print(ls[j][i], end="")
        except:
            print(" ", end="")
    print()