t = int(input())
for _ in range(t):
    s = input()
    n, ones = len(s), s.count("1")
    res = "DA" if min(ones, n - ones) & 1 == 1 else "NET"
    print(res)
