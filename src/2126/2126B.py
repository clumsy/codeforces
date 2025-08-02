t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = input()
    a = a.replace(" ", "").split("1")
    res = sum((len(c) + 1) // (k + 1) for c in a)
    print(res)
