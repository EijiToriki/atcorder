from collections import defaultdict

N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

color_dict = defaultdict(list)
for i in range(N):
    color_dict[C[i]].append((i+1, R[i]))

if T not in color_dict:
    T = C[0]

val = -1
ans = -1
for p_v in color_dict[T]:
    if val < p_v[1]:
        val = p_v[1]
        ans = p_v[0]
print(ans)