# https://zerojudge.tw/ShowProblem?problemid=c082

sizex, sizey = input().split()

lost = []
def move(x, y, face, i):
    directions = ["N", "E", "S", "W"]
    idx = directions.index(face)
    if i == "L": 
        face = directions[(idx - 1) % 4]
    elif i == "R":
        face = directions[(idx + 1) % 4]
    elif i == "F":
        lx, ly = x, y
        if (x, y, face) in lost:
            return (x, y, face)
        if face == "N":
            y += 1
        elif face == "S":
            y -= 1
        elif face == "E":
            x += 1
        elif face == "W":
            x -= 1
        if x<0 or y<0 or x>int(sizex) or y>int(sizey):
            lost.append((lx, ly, face))
            return ("LOST", lx, ly, face)
    return (x, y, face)

while 1:
    try:
        x, y, face = input().split()
        x, y  = int(x), int(y)
        for i in input():
            result = move(x, y, face, i)
            
            if result[0] == "LOST":
                print(f"{result[1]} {result[2]} {result[3]} LOST")
                break
            else:
                x, y, face = result
        else:
            print("{} {} {}".format(x, y, face))
    except EOFError:
        exit()