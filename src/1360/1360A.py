t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = max(2 * min(a, b), max(a, b)) ** 2
    print(res)
