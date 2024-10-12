# https://onlinejudge.org/external/100/10071.pdf

while 1:
    try:
        inp = input()
    except EOFError:
        exit()
    v, t = inp.split(" ")[0], inp.split(" ")[1]
    print(int(v)*int(t)*2)
