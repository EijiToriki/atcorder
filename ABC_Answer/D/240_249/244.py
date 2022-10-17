s1, s2, s3 = input().split()
t1, t2, t3 = input().split()

S = [s1, s2, s3]
T = [t1, t2, t3]

cnt = 0
for i in range(len(S)):
    if S[i] == T[i]:
        cnt += 1

if cnt == 3 or cnt == 0:
    print('Yes')
else:
    print('No')