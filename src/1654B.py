t = int(input())
for _ in range(t):
    s = input()
    p = {c: i for i, c in enumerate(s)}
    res = s[min(p.values()) :]
    print(res)
