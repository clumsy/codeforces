t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = min(b, c // 2)
    res = (min(a, (b - res) // 2) + res) * 3
    print(res)
