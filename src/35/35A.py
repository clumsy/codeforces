with open("input.txt") as f:
    res = int(f.readline())
    for _ in range(3):
        x, y = (int(i) for i in f.readline().split())
        if res == x:
            res = y
        elif res == y:
            res = x
with open("output.txt", "w") as f:
    print(res, file=f)
