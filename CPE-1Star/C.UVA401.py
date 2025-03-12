# https://zerojudge.tw/ShowProblem?problemid=e543

while 1:
    try:
        rev_map = {
            "A":"A",
            "E":"3",
            "H":"H",
            "I":"I",
            "J":"L",
            "L":"J",
            "M":"M",
            "O":"O",
            "S":"2",
            "T":"T",
            "U":"U",
            "V":"V",
            "W":"W",
            "X":"X",
            "Y":"Y",
            "Z":"5",
            "1":"1",
            "2":"S",
            "3":"E",
            "5":"Z",
            "8":"8"
        }
        pal = True
        inp = input()
        for i in range(len(inp)):
            try:
                pal = rev_map.get(inp[i]) == inp[-1-i]
            except:
                pal = inp[i] == inp[-1-i]
            if pal ==False:
                break

        if (inp == inp[::-1] and pal): print(f"{inp} -- is a mirrored palindrome.\n\n")
        elif (pal): print(f"{inp} -- is a mirrored string.\n\n")
        elif (inp == inp[::-1]): print(f"{inp} -- is a regular palindrome.\n\n")
        else: print(f"{inp} -- is not a palindrome.\n\n")
    except EOFError:
        exit()