t = int(input())
for _ in range(t):
    input()
    a = [int(i) for i in input().split()]
    avg = sum(a) / len(a)
    print("YES" if any(i == avg for i in a) else "NO")
