# https://zerojudge.tw/ShowProblem?problemid=a134

fib = [1,2]
while fib[-1]< 1e9:
    fib.append(fib[-1]+fib[-2])
def calc(n, r):
    for i in fib[::-1]:
        if n>=i:
            r += "1"
            n -= i
        else:
            r += "0"
    return r

for i in range(0, 1):
    res = int(calc(inp:=int(input()), ""))
    print("{} = {} (fib)".format(inp, res))