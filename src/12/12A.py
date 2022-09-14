m = [[c for c in input()] for _ in range(3)]
m_t = [r[::-1] for r in m[::-1]]
res = m == m_t
print("YES" if res else "NO")
