t = int(input())
for _ in range(t):
    c, r = input()
    res = [c + i for i in "12345678" if i != r] + [i + r for i in "abcdefgh" if i != c]
    print(*res, sep="\n")
