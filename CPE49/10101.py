# https://onlinejudge.org/external/101/10101.pdf

index = 1

def calc(n, res):
    if n >= 10000000:
        res += calc(n//10000000, res) + " kuti"
        n %= 10000000
    if n >= 100000:
        res += " " + str(n//100000) + " lakh"
        n %= 100000
    if n >= 1000:
        res += " " + str(n//1000) + " hajar"
        n %= 1000
    if n >= 100:
        res += " " + str(n//100) + " shata"
        n %= 100
    if n >= 1:
        res += " " + str(n)
    return res

while 1:
    try:
        inp = int(input())
        if inp == 0:
            print("   {}.0".format(index))
        else:
            res = ""
            print("{:>4}.{}".format(index, calc(inp, res)))
        index += 1
    except EOFError:
        exit()