from collections import deque

S = input()

alpha_box = deque()
rm_num_que = deque()

ans_flag = True

for i in range(len(S)):
  if S[i] == "(":
    rm_num_que.append(0)
  elif S[i] == ")":
    rm_num = rm_num_que.pop()
    for j in range(rm_num):
      alpha_box.pop()
  else:
    try:
      rm_num_que[len(rm_num_que)-1] += 1
      if S[i] in alpha_box:
        ans_flag = False
        break
      else:
        alpha_box.append(S[i])
    except:
      if S[i] in alpha_box:
        ans_flag = False
        break
      else:
        alpha_box.append(S[i])

if ans_flag:
  print('Yes')
else:
  print('No')

