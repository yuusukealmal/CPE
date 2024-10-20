# https://onlinejudge.org/external/100/10093.pdf

l = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

while 1:
    try:
        inp = input()
        m = l.find(max([i for i in inp if i in l]))
        s = sum([l.find(i) for i in inp if i in l])
        f = 0
        while m <= 62:
            if m <= 1: 
                print(2)
                f = 1
                break
            if s % (m - 1) == 0: 
                print(m)
                f = 1
                break
            m += 1
        if f == 0:
            print("such number is impossible!")
    except EOFError:
        exit()
