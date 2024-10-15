# https://onlinejudge.org/external/110/11063.pdfB2-Sequence

s, index = "Case #{}: It is {}a B2-Sequence.", 1
while 1:
    try:
        nums, inp, res, flag = input(), input().split(" "), [], 1
        for i in range(len(inp)):
            for j in inp[0:i]:
                r = int(inp[i])+int(j)
                if r not in res: 
                    res.append(r)
                elif r in res:
                    print(s.format(index, "not "))
                    flag, index = 0, index+1
            if not flag: break
        else:
            print(s.format(index, ""))
            index+=1
        print()
        input()
    except EOFError:
        exit()