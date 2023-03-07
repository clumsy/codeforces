t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    if n & 1 == 1:
        res = 1 if sum(int(i) & 1 == 1 for i in s[::2]) else 2
    else:
        res = 2 if sum(int(i) & 1 == 0 for i in s[1::2]) else 1
    print(res)
