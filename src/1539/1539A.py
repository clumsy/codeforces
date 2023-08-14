k = int(input())
for _ in range(k):
    n, x, t = (int(i) for i in input().split())

    # 0123456789
    # 0....0....
    # ..1....1..
    # ....2....2
    # ......3....3
    # ........4....4

    d = t // x
    res = d * (n - d) + (d - 1) * d // 2 if n > d else n * (n - 1) // 2
    print(res)
