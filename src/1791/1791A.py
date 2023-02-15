t = int(input())
s = set("codeforces")
for _ in range(t):
    c = input()
    res = "YES" if c in s else "NO"
    print(res)
