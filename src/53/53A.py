s, n = input(), int(input())
res = min((v for _ in range(n) if (v := input()).startswith(s)), default=s)
print(res)
