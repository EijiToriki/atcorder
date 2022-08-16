H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

b_point = -1
index_list = []
for i in range(b_point+1, len(A)):
  for h2 in range(H2):
    cnt = 0
    index_list_ele = []
    for w2 in range(W2):      
      if B[h2][w2] in A[i]:
        cnt += 1
        index_list_ele.append(A[i].index(B[h2][w2]))
    if cnt == len(B[h2]):
      index_list.append(index_list_ele)
  
if H2 == 1:
  if len(index_list) == 1:
    print('Yes')
  else:
    print('No')
else:
  if len(index_list) == H2:
    flag = True
    check = index_list[0]
    for i in range(1, len(index_list)):
      if check != index_list[i]:
        flag = False
        break
    if flag:
      print('Yes')
    else:
      print('No')
  else:
    print('No')