<<<<<<< HEAD
def check(s, i, p, x):
    # check if s[i:i+p] can be valid block of size p if it's allowed to use only x '#'s before position i
    return (
            i + p <= len(s) and
            s[:i].count('#') <= x and
=======
def check(s, i, p, x, y):
    # check if s[i:i+p] can be valid block of size p 
    # if it's allowed to use only x '#'s before position i and 
    # y '#'s after position i + p
    return (
            i + p <= len(s) and
            s[:i].count('#') <= x and
            s[i+p:].count('#') <= y and
>>>>>>> 9e310cf (2023 day-12)
            all(s[i] in '#?' for i in range(i, i + p)) and
            (i == 0 or s[i - 1] in '.?') and
            (i + p == len(s) or s[i + p] in '.?')
    )


def get_variants(s, p):
    S, P = len(s), len(p)
<<<<<<< HEAD
=======
    # dp[k][i] - number of ways to place first k + 1 patterns with last pattern ending at position i
>>>>>>> 9e310cf (2023 day-12)
    dp = [[0] * S for _ in range(P)]
    for k in range(P):
        for i in range(S):
            pos = i - p[k] + 1
<<<<<<< HEAD
            if pos >= 0 and check(s, pos, p[k], sum(p[:k])):
                dp[k][i] = (dp[k][i - 1] if i else 0) + 1 if not k else 1 + dp[k-1][pos-2] if pos - 2 >= 0 else 0
    print(' '.join(c.rjust(4, ' ') for c in s))
    for row in dp:
        print(' '.join(str(x).rjust(4, ' ') for x in row))
    print(sum(dp[-1]))

#
# with open('input.txt') as f:
#     total = 0
#     for line in f.readlines():
#         s, p2 = line.strip().split()
#         *v, = map(int, p2.split(','))
#         for si in get_variants(s):
#             total += check(si, v)
#     print(total)


get_variants('??????', [1, 1])
=======
            if pos >= 0 and check(s, pos, p[k], sum(p[:k]), sum(p[k+1:])):
                if k == 0:
                    dp[k][i] = 1
                else:
                    for j in range(pos - 2, -1, -1):
                        dp[k][i] += dp[k - 1][j]
                        if s[j] == '#':
                            break
    return sum(dp[-1])


with open('input.txt') as f:
    total = 0
    for line in f.readlines():
        s, p2 = line.strip().split()
        *p, = map(int, p2.split(','))
        total += get_variants(s, p)
    print(total)
>>>>>>> 9e310cf (2023 day-12)
