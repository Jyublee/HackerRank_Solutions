# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.

## 1.Time in Words
  - [Problem](https://www.hackerrank.com/challenges/the-time-in-words/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/timeconvert.py) (navigate to the Solution file)
  - Explanation:
```python
def timeInWords(h, m):
    numbers = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    if m == 0:
        return f"{numbers[h]} o' clock"
    
    if m == 15:
        return f"quarter past {numbers[h]}"
    
    if m == 30:
        return f"half past {numbers[h]}"
    
    if m == 45:
        return f"quarter to {numbers[h + 1]}"
    
    if m < 30:
        if m < 20:
            return f"{numbers[m]} {'minute' if m == 1 else 'minutes'} past {numbers[h]}"
        else:
            return f"twenty {numbers[m % 10]} {'minute' if m % 10 == 1 else 'minutes'} past {numbers[h]}"
    else:
        m = 60 - m
        if m < 20:
            return f"{numbers[m]} {'minute' if m == 1 else 'minutes'} to {numbers[h + 1]}"
        else:
            return f"twenty {numbers[m % 10]} {'minute' if m % 10 == 1 else 'minutes'} to {numbers[h + 1]}"
```
The numbers list contains words representing numbers from "zero" to "nineteen." These words are used to construct the textual time representation.

The function first checks if the minutes (m) are equal to 0. If so, it returns "o' clock," signifying that it's the exact hour with no minutes.

If the minutes are 15, it returns "quarter past [hour]," indicating a quarter past the specified hour.

When the minutes are 30, the function returns "half past [hour]," indicating that it's exactly half an hour past the specified hour.

If the minutes are 45, the function returns "quarter to [next hour]," signaling that it's a quarter to the next hour.

For minutes less than 30, the function further distinguishes between different minute descriptions. For instance, if the minutes are less than 20, it returns "[minutes] minute(s) past [hour]," providing a detailed minute count. For minutes between 20 and 29, it returns "twenty [minutes] minute(s) past [hour]" for a more concise representation.

For minutes greater than or equal to 30, the function adjusts the description for the time remaining until the next hour. It calculates the remaining minutes and, like in the previous case, provides detailed descriptions for minutes less than 20 and more concise descriptions for minutes between 20 and 29.
****
## 2.Lonely Integer

  - [Problem](https://www.hackerrank.com/challenges/lonely-integer/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/lonely.py) (navigate to the Solution file)
  - Explanation:
```python
def lonelyinteger(a):
    a = sorted(a)
    if len(a) < 3:
        return a[0]
    elif a[0] != a[1]:
        return a[0]
    else:
        return lonelyinteger(a[2:])

if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))

```
I have made an attempt to solve this recursively, 

First it sorts the input list a in ascending order.

If the length of the sorted list is less than 3, it means there is only one element in the list, so that element is returned as the lonely integer.

If the first and second elements of the sorted list are not equal, it means the first element is the lonely integer, and it is returned.

If the first and second elements are equal, the function makes a recursive call with the sorted list excluding the first two elements.

****

## 3.Climbing the Leaderboard

  - [Problem](https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/Leaderboard.py) (navigate to the Solution file)
  - Explanation:
```python
def climbingLeaderboard(scores, alice):
    scores = sorted(list(set(scores)))
    index = 0
    rank_list = []
    n = len(scores)
    for i in alice:
        while (n > index and i >= scores[index]):
            index += 1
        rank_list.append(n+1-index) 
    return rank_list
    
```
The function takes two lists as input: scores (the existing leaderboard scores) and alice (Alice's scores for which we want to find the ranks).

It starts by preparing the leaderboard scores. It removes duplicates by converting the scores list to a set and then sorts the unique scores in descending order. This way, it ensures that the leaderboard scores are unique and in descending order, making it easier to determine Alice's rank.

The index variable is initialized to 0 and will be used to keep track of the current position in the sorted leaderboard.

The rank_list is initialized as an empty list where Alice's ranks will be stored.

The variable n is set to the length of the sorted leaderboard scores. This represents the number of unique scores on the leaderboard.

The function then iterates through Alice's scores using a for loop.

For each of Alice's scores, it enters a while loop. This loop increments the index as long as the current leaderboard score is less than Alice's score and while there are still scores in the leaderboard to compare.

Once Alice's score is greater than or equal to the current leaderboard score or the end of the leaderboard is reached, the while loop stops.

The function calculates Alice's rank by subtracting the current index from n + 1 (the "+1" is added to handle the case where Alice's score is better than all scores on the leaderboard, so she would be ranked as 1).

Alice's rank is added to the rank_list for the current score.

After processing all of Alice's scores, the function returns the rank_list, which contains the ranks for each of her scores based on the existing leaderboard.
****

## 4. Icecream Parlor

  - [Problem](https://www.hackerrank.com/challenges/icecream-parlor/problem)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/ice.py) (navigate to the Solution file)
  - Explanation:
```python
def icecreamParlor(money, cost):
    cost_dict = {}
    
    for i, c in enumerate(cost, 1):
        if money - c in cost_dict:
            return [cost_dict[money - c], i]
        cost_dict[c] = i

```
The main code begins by reading an integer t representing the number of test cases.

For each test case, it reads the following information:

money: The amount of money the customer has.
n: The number of available ice cream flavors.
cost: A list containing the cost of each ice cream flavor.
It then calls the icecreamParlor function with the money and cost as parameters to find two ice cream flavors whose cost adds up to the available money.

The icecreamParlor function uses a cost_dict dictionary to store the costs of ice cream flavors along with their indices. It iterates through the cost list using enumerate.

For each flavor cost, it checks if the complement (money - cost) is already in the cost_dict. If it is, it means there's a pair of ice cream flavors whose cost adds up to the available money, so it returns their indices.

In the main code, the indices of the two selected ice cream flavors are printed for each test case.
****

## 5. Migratory Birds

  - [Problem](https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/migration.py) (navigate to the Solution file)
  - Explanation:
```python
def migratoryBirds(arr):
    count = [0] * 6
    for i in arr:
        count[i] += 1
    return count.index(max(count))
```
The function takes a list arr as a parameter, where each element represents the type of bird (an integer from 1 to 5).

It initializes a list count with six elements (from index 0 to 5). This is done to align the indexing with the bird type numbers. The count list will be used to store the number of occurrences for each bird type.

The function then iterates through the elements in the input list arr.

For each bird type i in arr, it increments the corresponding count in the count list. For example, if the bird type is 1, it increases count[1] by 1.

After counting the occurrences of each bird type, the function returns the index of the maximum value in the count list. This index corresponds to the ID of the most common bird type.

In the main code, it reads the number of birds, the list of bird types, and calls the migratoryBirds function to find the most common bird type.

****

## 6. Jumping on Clouds

  - [Problem](https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/jump.py) (navigate to the Solution file)
  - Explanation:
```python
def jumpingOnClouds(c, k):
    e=100
    energy=0
    i=0
    while(i!=len(c)):
        if(c[i]==1):
            energy=e-3
            e=energy
        else:
            energy=e-1
            e=energy
        i+=k
    return energy
    
```
The function takes two parameters: c, which is a list of clouds (0 for safe, 1 for thunderhead), and k, which is the jump distance.

It initializes the energy e to 100, a variable energy to track energy consumption, and a variable i to keep track of the current position in the clouds.

It enters a loop that continues until the character reaches the end of the clouds (i is not equal to the length of c).

Inside the loop, it checks the type of the current cloud. If it's a thunderhead (1), it subtracts 3 from the energy; if it's a safe cloud (0), it subtracts 1 from the energy.

After updating the energy level, it moves the character forward by k clouds by incrementing i.

The loop continues until the character has jumped through all the clouds.

Finally, the function returns the remaining energy level as the result.
****

## 7. Array Manipulation

  - [Problem](https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/arrayman.py) (navigate to the Solution file)
  - Explanation:
```python
def arrayManipulation(n, queries):
    arr = [0]*(n+1)
    max_value = 0
    total_sum = 0

    for query in queries:
        l = query[0]
        h = query[1]
        val = query[2]
        arr[l-1] = arr[l-1] + val
        arr[h] = arr[h]-val
    for value in arr:
        total_sum = total_sum + value
        max_value = max(max_value, total_sum)
    return max_value

    
```
The function takes two parameters: n, which represents the size of the array, and queries, which is a list of queries to be applied to the array.

It initializes an array arr of size n+1 with all elements initially set to 0. This array will be used to represent the changes at different positions in the original array.

It also initializes two variables, max_value to keep track of the maximum value encountered during the manipulations and total_sum to track the cumulative sum of the changes.

It then iterates through each query in the queries list.

For each query, it extracts the query parameters: l (left index), h (right index), and val (the value to be added within the range l to h).

It updates the arr by adding val at the l-1 position and subtracting val at the h position. This step efficiently represents the change within the specified range in the original array.

After processing all the queries, the function iterates through the arr and calculates the cumulative sum while updating the max_value if a larger value is encountered.

Finally, the function returns the max_value, which represents the maximum value in the manipulated array.
****

## 8. Sparse Arrays

  - [Problem](https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/sparse.py) (navigate to the Solution file)
  - Explanation:
```python
N = int(input())
numbers = list()
counts = list()
for i in range(0,N):
    numbers.append(input())
Q = int(input())
for i in range(0,Q):
    checkstring = input()
    count = 0
    for num in numbers:
        if num == checkstring:
            count = count + 1
    counts.append(count)
for count in counts:
    print(count)

    
```
It first reads the integer N, which represents the number of numbers you want to input into the list.

It initializes two empty lists: numbers to store the numbers and counts to store the counts for each query.

It enters a loop to input the numbers and appends them to the numbers list.

It then reads the integer Q, which represents the number of queries you want to perform.

It enters another loop to process each query:

It reads a string checkstring that you want to count within the numbers list.
It initializes a count variable to 0.
Within the query loop, it iterates through the numbers list and checks if each number is equal to the checkstring. If they match, it increments the count variable.

After counting the occurrences for the current query, it appends the count to the counts list.

Finally, it prints the counts for each query by iterating through the counts list.
****
## 9. Sherlock and the valid string

  - [Problem](https://www.hackerrank.com/challenges/sherlock-and-valid-string?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/sherlock.py) (navigate to the Solution file)
  - Explanation:
```python
set_list = list(s) 
freq = {} 
  for item in set_list: 
    if (item in freq): 
      freq[item] += 1
    else: 
      req[item] = 1
  freq_of_freq = list(freq.values())
  freq_of_freq_counts = set(freq_of_freq)
  if(len(freq_of_freq_counts)==1):
    return "YES"
  else:
    my_freq = {} 
    for item in freq_of_freq: 
      if (item in freq): 
        freq[item] += 1
      else: 
        freq[item] = 1
    theValues = list(freq.values())
    theKeys = list(freq.keys())
    if(len(theValues) == 2):
      if( (theKeys[1] - theKeys[0] <= 1) and (theValues[1] == 1)):
        return "YES"
      else:
        return "NO"
    else:
      return "NO"
```
To solve this we use the concept of a hash table.

First be break down the input into a dictonary with the respective charecters and their occurences as key value pairs.

Then we examine the resulting dict_values to see how many there are, if there is one then the output is Yes and if there is more than 2 then out put is no

If the number of values is 2 then there is still a possibility for yes 

Hence we check the case where the diffrence in the magnitude of the two values is 1 and give the result accordingly
****
## 10. Circular Array Roation

  - [Problem](https://www.hackerrank.com/challenges/circular-array-rotation/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/circulararray.py) (navigate to the Solution file)
  - Explanation:
```python
def circularArrayRotation(a, k, queries):
    L=[]
    x=k%len(a)
    for i in range(x):
        L.insert(0,a.pop())
    b=L+a
    result=[]
    for j in queries:
        result.append(b[j])
    return result
```
L is initialized as an empty list. This list will be used to store the elements that are "rotated" out of the original array a.

x is calculated as k modulo the length of the array a. This is done to handle cases where k is greater than the length of the array. The remainder of the division (k % len(a)) gives the effective number of positions by which the array should be rotated.

A loop runs from 0 to x - 1. In each iteration, it pops the last element from the array a using a.pop() and inserts it at the beginning of the list L. This effectively simulates a circular rotation by moving the last x elements to the front of the array a.

The rotated array is created by concatenating the list L (containing the elements that were rotated out) with the remaining elements of the original array a. This forms the array b, which represents the array after the circular rotation.

Another list named result is initialized to store the elements that correspond to the indices specified in the queries list.

A loop iterates through the elements in the queries list. For each index j in the queries list, it retrieves the element at index j from the rotated array b and appends it to the result list.

The result list, containing the elements from the rotated array corresponding to the specified indices, is returned as the final output of the function.
****
## 11.Bigger is Greater

  - [Problem](https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/greater.py) (navigate to the Solution file)
  - Explanation:
```python
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
  ```
 Here we are going to traverse the string from the last charecter in order to find the first one which greater than the previous one, since only then would be have a possible swap to make

 if our first loop is executed till i=0 that means there is no possible swap hence we return no answer

 in the other case now we have to determine which 2 elements to swap, for this we start traversing from the last charecter again in order to find one that is less than or equal to our first selected charecter w[i-1]

 then after finding a suitable one we swap it and then build the string as parts. the two parts would be w[:i] and the rest of the string in reverse.
****
## 12. Chocolates in a box 
  - [Problem](https://www.hackerrank.com/challenges/chocolate-in-box/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/choco.py) (navigate to the Solution file)
  - Explanation:
  ```python
def chocolateInBox(arr):
    xo = 0
    for x in arr:
        xo ^= x
    if xo == 0: 
        return 0
    c = 0
    for x in arr:
        if x ^ xo < x: 
            c += 1
    return c

  ```
Here we are going to use some lemmas from the Nim game inorder to complete this process 

We know that the ideal moves will leave a state of nim sum 0, that is when we xor all the chocolates if we get a non 0 then it is a winning position 

Hence first we xor all the array elements to check if the result is 0, if so then there is no way to win hence we print 0

Else we know we can win, now the question becomes who many ways can that be done, for this we will have to check will our final resultant xor value and compare the xor value of each element in our array to see if we have a choice to make an intermediate play state by using that array element

Finally we return the count 

***
