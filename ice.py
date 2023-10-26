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
