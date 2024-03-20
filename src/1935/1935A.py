t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    if s <= s[::-1]:
        res = s
    else:
        res = s[::-1] + s
    print(res)
