# https://onlinejudge.org/external/120/12019.pdf

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dooms = [
    [1,10],
    [2,21],
    [3,7],
    [4,4],
    [5,9],
    [6,6],
    [7,11],
    [8,8],
    [9,5],
    [10,10],
    [11,7],
    [12,12]
]

def calc(div):
    if div<0:
        index = abs(div)%7
        print(week[7-index if index != 0 else 0])
    else:
        print(week[div%7])

lines = input()
for i in range(int(lines)):
    inp = input()
    month = int(inp.split(" ")[0])
    day = int(inp.split(" ")[1])
    dooms_date = dooms[month-1][1]
    div = day - dooms_date
    calc(div)