def check_all_schedule(schedule_list, day):
  for schedule in schedule_list:
    if schedule[day] == 'x':
      return False
  return True


N, D = map(int, input().split())
schedule_list = []
for _ in range(N):
  Si = input()
  schedule_list.append(Si)

together_length = 0
buf_length = 0
for i in range(D):
  if check_all_schedule(schedule_list, i):
    buf_length += 1
  else:
    together_length = max(buf_length, together_length)
    buf_length = 0

together_length = max(buf_length, together_length)

print(together_length)

