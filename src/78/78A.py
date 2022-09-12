res = [sum(1 for c in input() if c in "aeiou") for _ in range(3)] == [5, 7, 5]
print("YES" if res else "NO")
