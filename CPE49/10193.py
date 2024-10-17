# https://onlinejudge.org/external/101/10193.pdf

from math import gcd

def convert(a):
    a = a[::-1]
    s = 0
    for i in range(0, len(a)):
        s += int(a[i])*(2**i)
    return s

index = 1
for i in range(0, int(input())):
    a, b = input(), input()
    dec_a, dec_b = convert(a), convert(b)
    if gcd(dec_a, dec_b) != 1:
        print("Pair #{}: All you need is love!".format(index))
    else:
        print("Pair #{}: Love is not all you need!".format(index))
    index += 1