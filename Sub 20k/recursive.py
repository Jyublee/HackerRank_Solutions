def sumOfDigits(num):
    num = str(num)
    length = len(num)
    sum = 0
    
    for i in range(length):
        sum += int(num[i])
        
    return sum

def superDigit(num):
    if len(str(num)) == 1:
        return num
    return superDigit(sumOfDigits(num))

temp = input().split()
n = int(temp[0])
k = int(temp[1])
num = sumOfDigits(n) * k

if len(str(num)) == 1:
    print(num)
else:
    answer = superDigit(num)
    print(answer)
