t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = 1 if a > 1 else a + b
    print(res)
