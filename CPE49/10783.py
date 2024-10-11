lines = input()
for i in range(int(lines)):
    min, max = int(input()), int(input())
    if min%2 == 0: min = min+1
    sum = 0 
    for j in range(min, max+1, 2):
        if j%2 != 0: sum += j
            
    print(f"Case {i+1}: {sum}")