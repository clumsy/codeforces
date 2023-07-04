n = int(input())
ax, ay = (int(i) for i in input().split())
bx, by = (int(i) for i in input().split())
cx, cy = (int(i) for i in input().split())
res = "YES" if (bx < ax) == (cx < ax) and (by < ay) == (cy < ay) else "NO"
print(res)
