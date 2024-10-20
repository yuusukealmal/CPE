# https://onlinejudge.org/external/102/10226.pdf

for i in range(test:=int(input())+1):
    dic = {}
    t = 0
    while True:
        try:
            inp = input().strip()
            if inp == "":
                break
            if inp in dic:
                dic[inp] += 1
            else:
                dic[inp] = 1
            t += 1
        except EOFError:
            break

    for k, v in sorted(dic.items()):
        print(f"{k} {v / t * 100:.4f}")
    if dic != {} or i != test-1:
        print()