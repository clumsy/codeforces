t = int(input())
for _ in range(t):
    a, b = (abs(int(i)) for i in input().split())
    res = 2 * min(a, b) + max(0, (2 * (max(a, b) - min(a, b)) - 1))
    print(res)
