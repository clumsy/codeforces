n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(f"1 {int(y/x)}" if (y/x).is_integer() else "0 0")
