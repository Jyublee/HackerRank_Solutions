def similar(string, T):  
    T.append(len(string))                                                          # default the zero index value for the z-array
    l = r = 0
    for i in range(1, len(string)):                                                # traverse the whole string to build the rest of the z-array
        k = 0
        if i < r:                                                                  # to check if the index we are checking is in the z-block 
            k = min(r-i, T[i-l])                                                   # to facilitate the condition where the value can exceed the block size
        while i+k<len(string) and string[i+k] == string[k]:                        # manually reading/updating z value in array
            k += 1
        T.append(k)
        if i+k > r:                                                                 # to form/update to a new z block
            l = i
            r = i+k

N = int(input())
for i in range(N):
    curr = input()
    count = 0
    T = []
    similar(curr, T)
    for j in range(len(T)):
        count += T[j]
    print(count)
