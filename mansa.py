def stones(n, a, b):
    if a>b:             
        a,b=b,a
    if a==b:         
        print((n-1)*a)
        return
    start,end,difference=(n-1)*a,(n-1)*b,b-a
    for i in range(start,end+1,difference):
        print(i,end=" ")
    print()
 
for _ in range(int(input())):
    n,a,b=int(input()),int(input()),int(input())
    stones(n,a,b)
