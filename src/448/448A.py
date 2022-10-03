a = sum(int(i) for i in input().split())
b = sum(int(i) for i in input().split())
n = int(input())
n = n - (a + 4) // 5 - (b + 9) // 10
res = "YES" if n >= 0 else "NO"
print(res)
