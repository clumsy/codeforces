t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = b - a
    print(res)
