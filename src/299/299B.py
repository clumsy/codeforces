n, k = (int(i) for i in input().split())
s = input()
ma = 0
for i, c in enumerate(s):
    if i > ma:
        break
    ma = i + k if c == "." else ma
res = "YES" if ma >= n - 1 else "NO"
print(res)
