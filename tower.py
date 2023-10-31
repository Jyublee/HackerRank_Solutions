T = int(input())
for t in range(T):
    n, m = [int(x) for x in input().strip().split()]
    if m == 1: 
        print(2)
    else:
        if n % 2 == 1:
            print(1)
        else:
            print(2)
