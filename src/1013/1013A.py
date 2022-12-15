n = int(input())
x = sum(int(i) for i in input().split())
y = sum(int(i) for i in input().split())
res = "YES" if x >= y else "NO"
print(res)
