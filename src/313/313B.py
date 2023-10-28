s = input()
n = len(s)
m = int(input())
a = [0] * n
for i, c in enumerate(s):
    a[i] = (a[i - 1] if i > 0 else 0) + (s[i] == s[i + 1] if i < n - 1 else 0)
for _ in range(m):
    l, r = (int(i) for i in input().split())
    res = a[r - 2] - (a[l - 2] if l > 1 else 0)
    print(res)
