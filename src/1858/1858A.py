t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "First" if a + (c + 1) // 2 > b + c // 2 else "Second"
    print(res)
