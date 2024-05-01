t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    res = "Bob" if (a + b) & 1 == 0 else "Alice"
    print(res)
