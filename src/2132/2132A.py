t = int(input())
for _ in range(t):
    n, a = int(input()), input()
    m, b = int(input()), input()
    c = input()
    res = (
        "".join(bi for bi, ci in zip(b, c) if ci == "V")[::-1]
        + a
        + "".join(bi for bi, ci in zip(b, c) if ci == "D")
    )
    print(res)
