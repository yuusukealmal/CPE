# https://onlinejudge.org/external/102/10268.pdf

while 1:
    try:
        x = int(input())
        func = input().split()
        func.reverse()
        s = 0
        for i in range(0, len(func)):
            s += i * (int(func[i]) * int((x ** (i-1))))
        print(int(s))
    except EOFError:
        exit()