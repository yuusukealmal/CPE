# https://onlinejudge.org/external/102/10222.pdf

while 1:
    try:
        inp = input()
    except EOFError:
        exit()
    dict = "1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    for i in inp:
        if i == " ": print(" ", end="")
        else: print(dict[dict.index(i.lower())-2], end="")
    print("")