from collections import defaultdict

N = int(input())
election_box = defaultdict(int)

for _ in range(N):
  s = input()
  election_box[s] += 1

ans_name = ''
max_vote = 0
for key, value in election_box.items():
  if value > max_vote:
    max_vote = value
    ans_name = key
  
print(ans_name)