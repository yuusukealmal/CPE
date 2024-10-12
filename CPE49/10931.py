# https://onlinejudge.org/external/109/10931.pdf

out = "The parity of {} is {} (mod 2)."
while 1:
    inp = input()
    if inp == "0": break
    b = bin(int(inp))
    print(out.format(b.split("0b")[1], b.count("1")))