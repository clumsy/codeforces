s = input()
n = len(s)
res = sum(s[i] != s[n - 1 - i] for i in range(n // 2))
res = "YES" if res == 1 or (res == 0 and n & 1 == 1) else "NO"
print(res)
