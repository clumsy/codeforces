with open("input.txt", "r") as f:
    n, m = (int(i) for i in f.read().split())
mi = min(n, m)
res = "G" * max(0, m - mi) + "BG" * mi + "B" * max(0, n - mi)
with open("output.txt", "w") as f:
    print(res, file=f)
