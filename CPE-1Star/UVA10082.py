# https://zerojudge.tw/ShowProblem?problemid=c054


key =  " `1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./ "

while 1:
    try:
        inp = input()
        print("".join(key[key.index(i) - 1] for i in inp))
    except EOFError:
        exit()