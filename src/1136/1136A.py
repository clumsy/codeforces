n = int(input())
c = [(int(i) for i in input().split()) for _ in range(n)]
k = int(input())
res = sum(1 for _, r in c if k <= r)
print(res)
