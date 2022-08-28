t = int(input())
for _ in range(t):
    n = int(input())
    print(2)
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        j = i
        while j <= n:
            print(j, end=" ")
            j *= 2
    print()
