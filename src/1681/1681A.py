t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    _, b = input(), (int(i) for i in input().split())
    max_a, max_b = max(a), max(b)
    print("Alice" if max_a >= max_b else "Bob")
    print("Bob" if max_b >= max_a else "Alice")
