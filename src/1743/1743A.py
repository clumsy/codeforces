t = int(input())
for _ in range(t):
    n, _ = int(input()), input()
    # ways to pick a pair of used numbers
    res = (10 - n) * (10 - n - 1)
    # ways to place 2 groups of 2 items on 4 positions: 4!/(2!*(4 - 2)!*2)
    res *= 3
    print(res)
