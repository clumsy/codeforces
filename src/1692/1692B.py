t = int(input())
for _ in range(t):
    n = int(input())
    a = {int(i) for i in input().split()}
    dupes = n - len(a)
    print(n - dupes - (dupes & 1))
