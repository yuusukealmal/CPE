# https://onlinejudge.org/external/100/10041.pdf
# hint 找中位數

def get_house(housesg):
    n = len(houses)
    if n % 2 == 1:
        return houses[n // 2]
    else:
        return houses[n // 2 - 1]

for i in range(int(input())):
    houses = [int(i) for i in input().split(" ")]
    nei = houses[0]
    s = 0
    houses.pop(0)
    houses.sort()
    house = get_house(houses)
    for i in houses:
        s += abs(int(i)-house)
    print(s)
    