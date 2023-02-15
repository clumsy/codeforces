t = int(input())
for _ in range(t):
    n, h = int(input()), (int(i) for i in input().split())
    ones = sum(i == 1 for i in h)
    res = (ones + 1) // 2 + (n - ones)
    print(res)
