# https://onlinejudge.org/external/100/10062.pdf
# clue :https://ithelp.ithome.com.tw/articles/10218710

first = False
while 1:
    try:
        inp = input()
        if not first: first = True
        else: print()
        dic = {}
        for i in inp:
            if ord(i) in dic:
                dic[ord(i)] += 1
            else:
                dic[ord(i)] = 1
        for key, value in sorted(dic.items(), key= lambda x: (x[1], -x[0])):
            print(key, value)
    except EOFError:
        exit()