t = int(input())
for _ in range(t):
    n = int(input())
    if n == 3:
        res = [-1]
    elif n & 1 == 1:
        res = [n // 2 - 1, -(n // 2)] * (n // 2) + [n // 2 - 1]
    else:
        res = [1, -1] * (n // 2)
    if res == [-1]:
        print("NO")
    else:
        print("YES")
        print(*res)
