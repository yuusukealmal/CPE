# https://onlinejudge.org/external/109/10908.pdf

def calc(ls, x, y, t):
    char = ls[x][y]
    while True:
        if x-t < 0 or x+t >= len(ls) or y-t < 0 or y+t >= len(ls[0]):
            return 2*t-1
        
        for i in range(-t, t+1):
            if ls[x-t][y+i] != char or ls[x+t][y+i] != char or ls[x+i][y-t] != char or ls[x+i][y+t] != char:
                return 2*t-1
        
        t += 1
for i in range(int(input())):
    ls = []
    M, N, Q = map(int, input().split())
    print(M, N, Q)
    for j in range(M):
            ls.append([k for k in input()])
    for a in range(Q):
        x, y = map(int, input().split())
        print(calc(ls, x, y, 1))