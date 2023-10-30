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
## 2.Bigger is Greater

  - [Problem](https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/greater.py) (navigate to the Solution file)
  - Explanation:
```python
n=int(input())
for a in range(n):
    s = input()
    s = list(s[::-1])
    done = 0
    for i in range(1,len(s)):
        if s[i-1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    print("".join(s[::-1]))
                    break
            break
    else:
        print("no answer")

```
The program begins by reading an integer that represents the number of test cases to be processed.

For each test case, it reads a string s.

It reverses the string and converts it into a list of characters. This reversed string will be manipulated to find the next greater permutation.

The done variable is used to track whether a greater permutation has been found.

It then iterates through the reversed string, starting from the second-to-last character (i ranging from 1 to len(s) - 1).

It checks if the current character is greater than the next character. This is a crucial condition for finding the next greater permutation.

If the condition is met, it searches for the smallest character to the right of the current character (s[j] > s[i]).

It swaps the found characters and sorts the substring to the right of i in ascending order.

The program prints the result, which is the next greater permutation in the original string format, and breaks out of the loop.

If no answer is found within the loop (meaning the string is already in the lexicographically greatest order), it prints "no answer."
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

if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().split()))

        result = icecreamParlor(money, cost)

        print(*result)
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
## 9. Mansa and the Stones

  - [Problem](https://www.hackerrank.com/challenges/manasa-and-stones/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](https://github.com/Jyublee/HackerRank_Solutions/blob/main/mansa.py) (navigate to the Solution file)
  - Explanation:
```python
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
    
```
The stones function takes three parameters: n (the number of stones), a (the cost to add 'a'), and b (the cost to add 'b').

It starts by checking whether a is greater than b. If so, it swaps the values to ensure that a is smaller than or equal to b.

It then checks if a and b are the same. If they are, it means that there's only one possible final value for all stones, and it calculates and prints that value.

If a and b are different, it calculates the starting value (start), ending value (end), and the difference (difference) between consecutive values.

It then enters a loop that generates and prints possible final values for the stones within the specified range, using the difference to increment the values.

In the main code, it first reads the number of test cases.

For each test case, it reads the values for n, a, and b.

It then calls the stones function for each test case to calculate and print the possible final values for the stones. The result represents a series of possible final values for the given set of stones.
****
## 10. Grid Search

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
