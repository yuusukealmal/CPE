# https://onlinejudge.org/external/106/10642.pdf

def calc(x0, y0, x1, y1, t):
    while x0 != x1 or y0 != y1:
        if y0 == 0:
            y0 = x0 +1
            x0 = 0
        else:
            x0 += 1
            y0 -= 1
        t += 1
    return t

for i in range(int(input())):
    x0, y0, x1, y1 = map(int, input().split())
    t = calc(x0, y0, x1, y1, 0)
    print("Case {}: {}".format(i+1, t))