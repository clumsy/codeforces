t = int(input())
for _ in range(t):
    n = int(input())
    res = "Kosuke" if (n + 1) & 1 == 0 else "Sakurako"
    print(res)
