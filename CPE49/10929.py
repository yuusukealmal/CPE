# https://onlinejudge.org/external/109/10929.pdf

while 1:
    inp = int(input())
    if inp == 0: break
    print("{} is{} a multiple of 11.".format(inp, "" if inp % 11 == 0 else " not"))