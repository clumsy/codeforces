t = int(input())
for _ in range(t):
    # 0101010
    # 0101001 1
    # 0100110 2
    # 0011001 3
    # 0000110 4
    # 0000001 5
    n, s = int(input()), input()
    i = res = 0
    while i < n:
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        res += res & 1 != int(s[i]) if i < n - 1 else 0
        i += 1
    print(res)
