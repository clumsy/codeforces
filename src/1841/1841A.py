t = int(input())
for _ in range(t):
    n = int(input())
    # [1 1 n - 2]
    res = "Alice" if n >= 5 else "Bob"
    print(res)
