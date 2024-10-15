# https://onlinejudge.org/external/109/10922.pdf

def calc(n):
    return sum(int(i) for i in str(n))

while 1:
    num = int(input())
    if num == 0: break
    if num%9 != 0: 
        print("{} is not a multiple of 9.".format(num))
        continue
    if num == 9:
        print("9 is a multiple of 9 and has 9-degree 1.")
        continue
    tmp, cnt = num, 0
    while tmp%9 == 0:
        if tmp == 9:
            break
        tmp = calc(tmp)
        cnt += 1
    print("{} is a multiple of 9 and has 9-degree {}.".format(num, cnt))