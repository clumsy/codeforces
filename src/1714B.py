t = int(input())
for _ in range(t):
    input()
    a = [int(i) for i in input().split()]
    uniq, res = set(), 0
    for i in range(len(a) - 1, -1, -1):
        if a[i] in uniq:
            res = i + 1
            break
        uniq.add(a[i])
    print(res)
