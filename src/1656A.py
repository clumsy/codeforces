t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    min_i, min_a, max_i, max_a = 0, 10**9 + 1, 0, 0
    for i, a_i in enumerate(a):
        if a_i < min_a:
            min_i, min_a = i, a_i
        if a_i > max_a:
            max_i, max_a = i, a_i
    print(min(min_i, max_i) + 1, max(min_i, max_i) + 1)
