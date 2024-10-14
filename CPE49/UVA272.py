# https://zerojudge.tw/ShowProblem?problemid=c007


index = 1
while 1:
    try:
        inp = input()
    except EOFError:
        exit()
    res = ""
    for i in inp:
        if i == '"' and index == 1:
            print(index)
            res += "``"
            index *= -1
        elif i == '"' and index == -1:
            print(index)
            res += "''"
            index *= -1
        else:
            res += i
    print(res)