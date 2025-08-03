t = int(input())
for _ in range(t):
    n = int(input())
    res = "Alice" if n % 4 != 0 else "Bob"
    print(res)
