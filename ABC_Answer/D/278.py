N = int(input())
A = list(map(int, input().split()))
Q = int(input())

deal_set = set()
remember = -1
query1_flag = False
for _ in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    deal_set = set()
    query1_flag = True
    remember = query[1]
  elif query[0] == 2:
    if query1_flag:
      if query[1]-1 not in deal_set:
        A[query[1]-1] = remember + query[2]
        deal_set.add(query[1]-1)
      else:
        A[query[1]-1] += query[2]
    else:
      A[query[1]-1] += query[2]
  elif query[0] == 3:
    if query1_flag:
      if query[1]-1 in deal_set:
        print(A[query[1]-1])
      else:
        print(remember)
    else:
      print(A[query[1]-1])