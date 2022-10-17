n,x,y,z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total_list = []
for a,b in zip(A,B):
  total_list.append(a+b)

student_list = [i for i in range(n)]
pass_list = []

math_sort_idx = [i[0]+1 for i in sorted(enumerate(A), key=lambda x:x[1], reverse=True)]
eng_sort_idx = [i[0]+1 for i in sorted(enumerate(B), key=lambda x:x[1], reverse=True)]
total_sort_idx = [i[0]+1 for i in sorted(enumerate(total_list), key=lambda x:x[1], reverse=True)]

for i in range(x):
  pass_list.append(math_sort_idx[i])

cnt = 0
for i in range(n):
  if cnt == y:
    break
  if eng_sort_idx[i] not in pass_list:
    pass_list.append(eng_sort_idx[i])
    cnt += 1
  
cnt = 0
for i in range(n):
  if cnt == z:
    break
  if total_sort_idx[i] not in pass_list:
    pass_list.append(total_sort_idx[i])
    cnt += 1

student_list = sorted(pass_list)

for student in student_list:
  print(student)


