t = int(input())
for _ in range(t):
    input()
    for d in input().split():
        d = int(d) + sum(1 if x == "D" else -1 for x in input().split()[1])
        print(d % 10, end=" ")
    print()
