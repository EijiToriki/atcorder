N, L, R = map(int, input().split())
A = list(map(int, input().split()))

l_loss_plus_list = []
loss = 0
for i in range(N):
  loss += L - A[i]
  if loss >= 0:
    l_loss_plus_list.append(i)


r_loss_plus_list = []
loss = 0
for i in range(N):  
  loss += R - A[-(i+1)]
  if loss >= 0:
    r_loss_plus_list.append(N-i-1)

print(l_loss_plus_list)
print(r_loss_plus_list)
