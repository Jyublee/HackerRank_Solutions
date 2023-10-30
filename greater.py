t = int(input())

for z in range(t):
    w = list(input())
    l = len(w)
    
    i = l - 1
    while i > 0 and w[i-1] >= w[i]:
        i-=1
    
    if i<=0:
        print ("no answer")
        continue
    
    j = l - 1
    while w[j] <= w[i-1]:
        j-=1
    
    w[i-1],w[j] = w[j],w[i-1]
    
    print ("".join(w[:i]+w[i:][::-1]))
        
