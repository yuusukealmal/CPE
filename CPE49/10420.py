# https://onlinejudge.org/external/104/10420.pdf

dict = {}
for i in range(int(input())):
    country = input().split()[0]
    if country in dict:
        dict[country] += 1
    else:
        dict[country] = 1
for k, v in sorted(dict.items(), key=lambda x: x[0]):
    print(k, v)
