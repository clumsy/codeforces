from collections import Counter

t = int(input())
for _ in range(t):
    s = input()
    c = Counter(s)
    res = (
        "=" if c["="] == len(s) else ">" if c["<"] == 0 else "<" if c[">"] == 0 else "?"
    )
    print(res)
