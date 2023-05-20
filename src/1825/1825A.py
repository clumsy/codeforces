t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    res = -1 if all(s[0] == s[i] for i in range(1, n)) else n - 1
    print(res)
