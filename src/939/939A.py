n, f = int(input()), [int(i) for i in input().split()]


def triangle(i):
    return i == f[f[f[i] - 1] - 1] - 1


res = "YES" if any(triangle(i) for i in range(n)) else "NO"
print(res)
