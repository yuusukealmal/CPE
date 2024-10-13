# # https://onlinejudge.org/external/100/10035.pdf

BASE = "{} carry operation{}."

def calc(a, b, c):
    if a + b + c >=10:
        return True
    else:
        return False

while 1:
    inp = input()
    if inp == "0 0": exit()
    first  = list(inp.split(" ")[0])
    second = list(inp.split(" ")[1])
    diff = abs(len(first) - len(second))
    
    if len(first) < len(second):
        first = ["0"] * diff + first
    elif len(first) > len(second):
        second = ["0"] * diff + second
    carry, tmp = 0, 0
    for i in range(-1, -max(len(first),len(second))-1, -1):
        tmp = calc(int(first[i]), int(second[i]), tmp)
        if tmp:
            carry += 1
    print(BASE.format("No" if carry==0 else carry, "s" if carry>1 else ""))