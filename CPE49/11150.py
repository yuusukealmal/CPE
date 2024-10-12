# https://onlinejudge.org/external/111/11150.pdf

def calc(bottle, s) -> int:
    change = bottle//3
    s += change
    left = bottle%3 + change
    if left>=3: 
        return calc(left, s)
    if left == 2: s += 1
    return s

while 1:
    sum = 0
    try:
        bottle = int(input())
    except EOFError:
        exit()
    print(calc(bottle, bottle))
