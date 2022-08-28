t = int(input())
for _ in range(t):
    s, c = input(), input()
    n = len(s)
    # any c position in s works if on odd position from both ends
    res = any(s[i] == c for i in range(n) if i & 1 == 0)
    print("YES" if res else "NO")
