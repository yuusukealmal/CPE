# https://onlinejudge.org/external/113/11349.pdf

for i in range(1, int(input())+1):
    size = input()
    ls = []
    for j in range(0, int(size.split()[-1])):
        for k in input().split():
            ls.append(int(k))
    if any(ls[i] < 0 for i in range(1, len(ls))):
        print("Test #{}: Non-symmetric.".format(i))
        continue
    cp = ls.copy()
    if ls == cp[::-1]:
        print("Test #{}: Symmetric.".format(i))
    else:
        print("Test #{}: Non-symmetric.".format(i))