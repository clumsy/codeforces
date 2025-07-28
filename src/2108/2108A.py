t = int(input())
for _ in range(t):
    n = int(input())
    res = sum(abs(i + 1 - (n - i)) for i in range(n)) // 2 + 1
    print(res)
