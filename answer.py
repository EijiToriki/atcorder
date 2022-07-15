def is_kaibun(S, N):
  check_num = N // 2

  for i in range(check_num):
    if S[i] != S[N-i-1]:
      return False
  
  return True


S = input()
N = len(S)

a_back_cnt = 0
for i in range(N):
  if S[-i-1] == 'a':
    a_back_cnt += 1
  else:
    break

S = S[:N-a_back_cnt]
N = len(S)


a_front_cnt = 0
for i in range(N):
  if S[i] == 'a':
    a_front_cnt += 1
  else:
    break

S = S[a_front_cnt:]
N = len(S)

if a_front_cnt > a_back_cnt:
  print('No')
else:
  if is_kaibun(S, N):
    print('Yes')
  else:
    print('No')

