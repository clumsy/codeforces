t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    if min(a) == max(a):
        res = "No"
    else:
        ma = a.index(max(a))
        res = "Yes\n" + " ".join(["1"] * ma + ["2"] + ["1"] * (n - 1 - ma))
    print(res)
