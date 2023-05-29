t = int(input())
for _ in range(t):
    n = int(input())
    res = "4" + "3" * (n - 1) if n > 1 else -1
    print(res)
