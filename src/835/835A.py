s, v1, v2, t1, t2 = (int(i) for i in input().split())
diff = (2 * t1 + s * v1) - (2 * t2 + s * v2)
res = "First" if diff < 0 else "Second" if diff > 0 else "Friendship"
print(res)
