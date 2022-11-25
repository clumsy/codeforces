t = int(input())
res = [i for i in range(101)]
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    if any(i < 0 for i in a):
        print("NO")
    else:
        print("YES")
        print(len(res))
        print(*res)
