t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    m, c = n // 2, 0
    if n & 1 == 1:
        c -= 1
    while m < n and s[m] == s[n // 2]:
        c += 2
        m += 1
    print(c)
