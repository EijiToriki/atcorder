N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

q1_max_k = min(N-A, N-B)
q1_min_k = max(1-A, 1-B)

q2_max_k = min(N-A, B-1)
q2_min_k = max(1-A, B-N)

ans_list = []
for i in range(P,Q+1):
  ans_part = ''
  for j in range(R, S+1):
    output_flag = True
    if A+q1_min_k <= i <= A+q1_max_k:
      if B+q1_min_k <= j <= B+q1_max_k and j == B+q1_min_k+i-A-q1_min_k:
        ans_part += '#'
        output_flag = False

    if output_flag:
      if A+q2_min_k <= i <= A+q2_max_k:
        if B-q2_max_k <= j <= B-q2_min_k and j == B-q2_min_k-i+A+q2_min_k:
          ans_part += '#'
          output_flag = False
    
    if output_flag:
      ans_part += '.'
  ans_list.append(ans_part)

print('\n'.join(ans_list))