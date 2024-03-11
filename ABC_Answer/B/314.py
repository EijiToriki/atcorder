from collections import defaultdict

N = int(input())

kake_dict = defaultdict(set)
for i in range(N):
  kake_cnt = int(input())
  kake_dict[i+1] = set(map(int, input().split()))
X = int(input())

hit_person = defaultdict(int)
for person, kake_nums in kake_dict.items():
  if X in kake_nums:
    hit_person[person] = len(kake_nums)

if(len(hit_person) == 0):
  print(0)
  exit()

ans = []
min_kake_num = min(hit_person.values())
for person in hit_person.keys():
  if hit_person[person] == min_kake_num:
    ans.append(person)

ans = sorted(ans)
print(len(ans))
print(*ans)

