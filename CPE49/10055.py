# https://onlinejudge.org/external/100/10055.pdf

while 1:
    try:
        inp = input().split(" ")
    except EOFError:
        exit()
    a = int(inp[0])
    b = int(inp[1])
    print(abs(a-b))