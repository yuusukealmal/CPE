# https://onlinejudge.org/external/100/10038.pdf

while 1:
    try:
        inp = input()
    except EOFError:
        exit()
    ls = inp.split(" ")
    ls.pop(0)
    r = [int(i)+1 for i in range(len(ls)-1)]
    for i in range(0, len(ls)-1):
        diff = abs(int(ls[i])-int(ls[i+1]))
        if 1 <= diff <= len(ls)-1:
            try:
                r.remove(diff)
            except:
                pass
        else:
            print("Not jolly")
            break
    else:
        print("Jolly") if len(r) == 0 else print("Not jolly")
