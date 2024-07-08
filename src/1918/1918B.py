t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    def order(i):
        return a[i] + b[i]

    ord = sorted(range(n), key=order)
    print(*(a[i] for i in ord))
    print(*(b[i] for i in ord))
