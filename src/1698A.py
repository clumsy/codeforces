t = int(input())
for _ in range(t):
    input()
    # any element works, everything else cancels out
    x = next(int(i) for i in input().split())
    print(x)
