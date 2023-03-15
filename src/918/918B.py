n, m = (int(i) for i in input().split())
mapping = {}
for _ in range(n):
    name, ip = input().split()
    mapping[ip] = name
for _ in range(m):
    s = input()
    ip = s[s.index(" ") + 1 : s.index(";")]
    res = f"{s} #{mapping[ip]}"
    print(res)
