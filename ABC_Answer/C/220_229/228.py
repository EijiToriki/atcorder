N, K = map(int, input().split())

score_list = []
for _ in range(N):
  score1, score2, score3 = map(int, input().split())
  score_list.append(score1+score2+score3)

sorted_score_list = sorted(score_list, reverse=True)
base_score = sorted_score_list[K-1]

for score in score_list:
  if score + 300 >= base_score:
    print('Yes')
  else:
    print('No')