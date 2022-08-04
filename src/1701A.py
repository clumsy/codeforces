t = int(input())
for _ in range(t):
    s = sum(int(i) for i in input().split()) + sum(int(i) for i in input().split())
    if s == 4:
        print(2)
    elif s > 0:
        print(1)
    else:
        print(0)
