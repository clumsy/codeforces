n, s = int(input()), sorted(int(i) for i in input().split())
res = 0
for i in range(n // 2):
    res += (s[i] + s[n - i - 1]) ** 2
print(res)
