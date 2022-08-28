t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    k %= 4
    if k == 0:
        print("NO")  # we don't have enough numbers divisible by 4 to match the rest
    else:
        print("YES")
        if k == 1 or k == 3:
            for i in range(1, n + 1, 2):
                print(f"{i} {i + 1}")  # b is always divisible by 4
        else:  # k == 2
            for i in range(1, n + 1, 2):
                if (i + 1) % 4 == 0:
                    print(f"{i} {i + 1}")  # b is divisible by 4
                else:
                    print(f"{i + 1} {i}")  # a is divisible by 4 (even a, plus k == 2)
