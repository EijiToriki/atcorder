N, M = map(int, input().split())
setA = []
for _ in range(M):
    C = int(input())
    setC = set(list(map(int, input().split())))
    setA.append(setC)

ans = 0
for i in range(2 ** M):
    check = []
    for j in range(M):
        if ((i >> j) & 1):
            check.append(setA[j])
    check_set = set()
    for one_set in check:
        check_set = check_set | one_set
    if len(check_set) == N:
        ans += 1

print(ans)
