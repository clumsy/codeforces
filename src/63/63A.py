n = int(input())
priority = {
    "rat": 0,
    "woman": 1,
    "child": 1,
    "man": 2,
    "captain": 3,
}
crew = [input().split() for _ in range(n)]


def rank(i):
    return (priority[crew[i][1]], i)


order = sorted(range(n), key=rank)
res = (crew[i][0] for i in order)
print(*res, sep="\n")
