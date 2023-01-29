t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res, rem = divmod(abs(a - b), 5)
    res += (rem + 1) // 2
    print(res)
