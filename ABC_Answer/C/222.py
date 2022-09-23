from collections import defaultdict


N, M = map(int, input().split())
A = []
for _ in range(2*N):
    A.append(input())

score_dict = defaultdict(int)
for i in range(2*N):
    score_dict[i] += 1

for i in range(M):     # ラウンド
    score_dict = dict(sorted(score_dict.items()))
    score_dict = dict(sorted(score_dict.items(), key=lambda x:x[1], reverse=True))
    cnt = 1
    for k in score_dict.keys():
        if cnt % 2 == 0:
            if A[k][i] == 'G' and A[pre_k][i] == 'C':
                score_dict[k] += 1
            elif A[k][i] == 'C' and A[pre_k][i] == 'P':
                score_dict[k] += 1
            elif A[k][i] == 'P' and A[pre_k][i] == 'G':
                score_dict[k] += 1
            elif A[k][i] == 'G' and A[pre_k][i] == 'P':
                score_dict[pre_k] += 1
            elif A[k][i] == 'P' and A[pre_k][i] == 'C':
                score_dict[pre_k] += 1
            elif A[k][i] == 'C' and A[pre_k][i] == 'G':
                score_dict[pre_k] += 1
        else:
            pre_k = k
        cnt += 1

score_dict = dict(sorted(score_dict.items()))
score_dict = dict(sorted(score_dict.items(), key=lambda x:x[1], reverse=True))
for k in score_dict.keys():
    print(k+1)
