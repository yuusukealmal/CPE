# https://onlinejudge.org/external/102/10252.pdf

while 1:
    try:
        inp1 = input()
        inp2 = input()
    except EOFError:
        exit()
    res = ""
    for i in "abcdefghijklmnopqrstuvwxyz":
        res += i * min(inp1.count(i), inp2.count(i))
    print(res)