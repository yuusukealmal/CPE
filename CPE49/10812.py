# https://onlinejudge.org/external/108/10812.pdf

lines = input()
for i in range(int(lines)):
    inp = input()
    s, d = int(inp.split(" ")[0]) , int(inp.split(" ")[1])
    if (s%2 != d%2):
        print("impossible")
    else:
        a, b = int((s+d)/2), int((s-d)/2)
        if a < 0 or b < 0:
            print("impossible")
        else:
            print(f"{max(a,b)} {min(a,b)}")