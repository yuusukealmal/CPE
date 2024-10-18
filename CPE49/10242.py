# https://onlinejudge.org/external/102/10242.pdf

while 1:
    try:
        spl = input().split()
        pts = []
        for i in range(0,len(spl),2):
            pts.append([float(spl[i]),float(spl[i+1])])
        for i in pts:
            if pts.count(i) == 2:
                tmp = i
                break
        pts.remove(tmp)
        pts.remove(tmp)
        x, y = 0 ,0
        for j in pts:
            x += j[0]
            y += j[1]
        print("{:.4f} {:.4f}".format(x-tmp[0],y-tmp[1]))
    except EOFError:
        exit()