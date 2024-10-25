t = int(input())
for _ in range(t):
    s = input()
    res = "YES" if len(s) & 1 == 0 and s[0] != ")" and s[-1] != "(" else "NO"
    print(res)
