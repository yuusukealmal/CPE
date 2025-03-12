# https://zerojudge.tw/ShowProblem?problemid=e553

num = [0, 1, 5, 2, 8, 3, 9, 2, 8, 7, 7, 8, 4, 7, 3, 8, 4, 1, 5, 4, 4]

def mod(s):
    res = 0
    for c in s:
        res = (res * 10 + int(c)) % 20
    return res

def cnt(n):
    r = mod(n)
    M = int(n) if len(n)<2 else int(n[-2:])
    diff = M - r
    while diff < 0:
        diff += 100
    c = (diff // 20) % 5
    s = num[r]
    return (4 * c + s) % 10

while 1:
    inp = input().strip()
    if inp == "0": break
    print(cnt(inp))