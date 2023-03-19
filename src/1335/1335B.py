t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    s = ["a"]
    for i in range(1, a):
        b -= 1
        s.append(chr(ord(s[i - 1]) + 1) if b > 0 else s[i - 1])
    for i in range(a, n):
        s.append(s[i - a])
    res = "".join(s)
    print(res)
