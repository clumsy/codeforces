t = int(input())
for _ in range(t):
    s = input()
    d = 0 if s[-1] == "B" else -42
    for c in s:
        d += 1 if c == "A" else -1
        if d < 0:
            break
    print("YES" if d >= 0 else "NO")
