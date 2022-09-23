t = int(input())
for _ in range(t):
    n = int(input())
    # m = n, when adding from left to right we end up with arithmetic sum
    res = (i + 1 for i in range(n))
    print(n)
    print(*res)
