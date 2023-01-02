f, s, t = (input() for _ in range(3))
m = {f[i]: s[i] for i in range(len(f))}
res = "".join(m[c.lower()].upper() if c.isupper() else m.get(c, c) for c in t)
print(res)
