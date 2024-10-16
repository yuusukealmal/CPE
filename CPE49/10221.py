# https://onlinejudge.org/external/102/10221.pdf

# hint: 弧長=半徑*弧度 弦距=半2*徑*sin(弧度/2)  
import math
while 1:
    try:
        earth = 6440
        inp = input()
        s, d, count = inp.split()
        s, d = int(s), int(d)
        if count == "min": d = d/60
        rad = d * math.pi / 180
        long = (earth+s) * rad
        distance = 2 * (earth+s) * math.sin(rad/2)
        print("{:.6f} {:.6f}".format(long, distance))
    except EOFError:
        exit()