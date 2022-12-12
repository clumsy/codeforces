n, k = (int(i) for i in input().split())
s = input()
g, t, res = s.index("G"), s.rindex("T"), "NO"
g, t = min(g, t), max(g, t)
s = set(s[g : t + 1 : k])
res = "YES" if "G" in s and "T" in s and "#" not in s else "NO"
print(res)
