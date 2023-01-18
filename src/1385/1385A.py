t = int(input())
for _ in range(t):
    x, y, z = sorted(int(i) for i in input().split())
    # max has to show up in two pairs
    if y == z:
        print("YES")
        # x always work as a and b
        print(x, x, z)
    else:
        print("NO")
