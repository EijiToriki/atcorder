N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = []
tmp = []
i = 1
while i <= N:
    if i in A:
        tmp.append(i)
    else:
        if len(tmp) > 0:
            tmp.append(i)
            tmp = sorted(tmp, reverse=True)
            for a in tmp:
                ans.append(a)
            tmp = []
        else:
            ans.append(i)
    i += 1

print(*ans)

        


