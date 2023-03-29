def diff(s1, s2):
    limit = min(len(s1), len(s2))

    for i in range(limit):
        if s1[i] != s2[i]:
            return i
    return limit


N = int(input())
S = []
for i in range(N):
    S.append((input(), i+1))
S.sort()

result = [0] * (N+1)
result[S[0][1]] = diff(S[0][0], S[1][0])
for i in range(N-1):
    result[S[i][1]] = max(
        diff(S[i-1][0], S[i][0]),
        diff(S[i][0], S[i+1][0])
    )
result[S[N-1][1]] = diff(S[N-2][0], S[N-1][0])

for i in range(1, N+1):
    print(result[i])
