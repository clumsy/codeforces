t = int(input())
for _ in range(t):
    n = int(input())
    letters = {}
    total = 0
    for _ in range(n):
        s = input()
        total += len(s)
        for c in s:
            letters[c] = letters.get(c, 0) + 1
    res = "NO"
    if total % n == 0 and all(v % n == 0 for _, v in letters.items()):
        res = "YES"
    print(res)
