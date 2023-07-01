n, s = int(input()), input()
res = None
for i in range(n - 1):
    if s[i] != s[i + 1]:
        res = s[i : i + 2]
        break
print("YES" if res else "NO")
if res:
    print(res)
