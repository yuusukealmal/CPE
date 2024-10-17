# https://onlinejudge.org/external/100/10008.pdf

dict = {}
for i in range(int(input())):
    s = input()
    for j in s:
        if 97 <= ord(j) <= 122 or 65 <= ord(j) <= 90:
            if j.upper() in dict:
                dict[j.upper()] += 1
            else:
                dict[j.upper()] = 1
for k,v in sorted(dict.items(), key=lambda x: (x[1], -ord(x[0])), reverse=True):
    print(k,v)