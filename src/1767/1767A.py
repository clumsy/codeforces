t = int(input())
for _ in range(t):
    input()
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    res = (
        "NO"
        if len(set([a[0], b[0], c[0]])) == len(set([a[1], b[1], c[1]])) == 2
        else "YES"
    )
    print(res)
