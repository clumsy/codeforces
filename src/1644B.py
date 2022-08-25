t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n, 0, -1):
        s = [i]
        for j in range(n, 0, -1):
            if i != j:
                s.append(j)
        print(*s)
