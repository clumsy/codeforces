t = int(input())
for _ in range(t):
    a, b, k = (int(i) for i in input().split())
    res = a * ((k + 1) // 2) - b * (k // 2)
    print(res)
