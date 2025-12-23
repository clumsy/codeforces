t = int(input())
for _ in range(t):
    a, b, n = (int(i) for i in input().split())
    res = 2 if a / n < b < a else 1
    print(res)
