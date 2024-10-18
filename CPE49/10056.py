# https://onlinejudge.org/external/100/10056.pdf

for _ in range(int(input())):
    N, p, i = input().split()
    N = int(N)
    p = float(p)
    i = int(i)
    
    if p ==0: 
        print("0.0000")
        continue
    win = (p * ((1 - p) ** (i - 1)))/(1 - (1 - p) ** N)
    print("{:.4f}".format(win))
