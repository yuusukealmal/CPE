# https://onlinejudge.org/external/100/10050.pdf

ts_cnt = int(input())
for i in range(ts_cnt):
    cdays, counter, bruh, C = int(input()), int(input()), 0, []
    for i in range(counter):
        C.append(int(input()))
    for j in range(1, cdays+1):
        if j%7 == 0 or j%7 == 6: continue
        for k in C:
            if j%k == 0:
                bruh += 1
                break
    print(bruh)