# https://onlinejudge.org/external/110/11005.pdf

l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(tests:=int(input())):
    print("Case {}:".format(i+1))
    price = []
    for j in range(4):
        for _ in input().split():
            price.append(int(_))
    for ts in range(int(input())):
        txt = int(input())
        r = []
        small = l.find(max([i for i in str(txt) if i in l]))
        small = 2 if small <= 1 else small
        for _ in range(small, 37):
            sum = 0
            current = txt  
            while current > 0:
                digit = current % _
                sum += price[digit]
                current//= _ 
            r.append(sum)
        res = min(r)
        out = "Cheapest base(s) for number {}: ".format(str(txt))
        for _ in range(0, len(r)):
            if r[_] == res: 
                out += "{} ".format(_+small)
        print(out[:-1])
    if i != tests-1:
        print()
