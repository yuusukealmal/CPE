# https://zerojudge.tw/ShowProblem?problemid=e561

while 1:
    try:
        for test in range(int(input())):
            time = 0
            cnt = int(input())
            train = [int(i) for i in input().split()]
            for i in range(0, len(train)):
                for j in range(0, len(train)-1):
                    if train[j] > train[j+1]:
                        train[j], train[j+1] = train[j+1], train[j]
                        time += 1
            print("Optimal train swapping takes {} swaps.".format(time))
    except EOFError:
        exit()
