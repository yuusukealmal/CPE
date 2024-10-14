# https://onlinejudge.org/external/101/10170.pdf

def calc(person, day):
    while day > 0:
        person += 1
        day -= person - 1
    return person - 1

while True:
    try:
        inp = input()
        person, day = map(int, inp.split())
        print(calc(person, day))
    except EOFError:
        break