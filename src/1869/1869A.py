t = int(input())
for _ in range(t):
    n, a = int(input()), input()
    if n & 1 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, n - 1)
        print(1, n - 1)
        print(n - 1, n)
        print(n - 1, n)
