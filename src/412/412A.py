n, k = (int(i) for i in input().split())
s = input()
m = min(k - 1, n - k)
right = m < k - 1
for _ in range(m):
    print("RIGHT" if right else "LEFT")
if right:
    s = reversed(s)
right = not right
for c in s:
    print(f"PRINT {c}")
    if n > 1:
        print("RIGHT" if right else "LEFT")
    n -= 1
