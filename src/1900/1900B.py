t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    b_c, a_c, a_b = abs(b - c), abs(a - c), abs(a - b)
    res = [
        int(b_c & 1 == 0 and a + min(b, c) > 0),
        int(a_c & 1 == 0 and b + min(a, c) > 0),
        int(a_b & 1 == 0 and c + min(a, b) > 0),
    ]
    print(*res)
