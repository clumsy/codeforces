t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = ["X"] + (["B"] * m)
    for i in range(0, n):
        mi, ma = sorted([a[i], m + 1 - a[i]])
        s[mi if s[mi] == "B" else ma] = "A"
    print("".join(s[1:]))
