t = input()
f, s = input().split()
m = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}
for i in range(6, 10):
    m[str(i)] = i
res = (
    "YES"
    if f[-1] == t and s[-1] != t
    else "NO"
    if s[-1] == t and f[-1] != t
    else "YES"
    if f[-1] == s[-1] and m[f[:-1]] > m[s[:-1]]
    else "NO"
)
print(res)
