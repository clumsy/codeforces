t = int(input())
for _ in range(t):
    _, s = input(), input()
    res = s in {"0", "1", "01", "10"}
    print("YES" if res else "NO")
