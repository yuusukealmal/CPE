# https://onlinejudge.org/external/104/10409.pdf

def roll(dice, way):
    if way == "north":
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif way == "south":
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    elif way == "east":
        dice[0], dice[5], dice[2], dice[4] = dice[4], dice[0], dice[5], dice[2]
    elif way == "west":
        dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]
    return dice

while 1:
    dice = [1,2,6,5,3,4]
    times = int(input())
    if times == 0: break
    for i in range(times):
        dice = roll(dice, input())
    print(dice[0])