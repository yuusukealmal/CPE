# https://onlinejudge.org/external/104/10415.pdf

fingers = {
    'c' : [2, 3, 4, 7, 8, 9, 10],
    'd' : [2, 3, 4, 7, 8, 9],
    'e' : [2, 3, 4, 7, 8],
    'f' : [2, 3, 4, 7],
    'g' : [2, 3, 4],
    'a' : [2, 3],
    'b' : [2],
    'C' : [3],
    'D' : [1, 2, 3, 4, 7, 8, 9],
    'E' : [1, 2, 3, 4, 7, 8],
    'F' : [1, 2, 3, 4, 7],
    'G' : [1, 2, 3, 4],
    'A' : [1, 2, 3],
    'B' : [1, 2],
}
for i in range(int(input())):
    res = {i:0 for i in range(1, 11)}
    last = []
    for note in input():
        current = fingers[note]
        for finger in current:
            if finger not in last:
                res[finger] += 1 
        last = current
    r = ""
    for v in res.values():
        r += str(v) + " "
    print(r[:-1])