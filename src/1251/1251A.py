t = int(input())
for _ in range(t):
    s = input()
    n, size, odd = len(s), 0, set()
    for i in range(n):
        size += 1
        if i + 1 >= n or s[i] != s[i + 1]:
            if size & 1 == 1:
                odd.add(s[i])
            size = 0
    res = "".join(sorted(odd))
    print(res)
