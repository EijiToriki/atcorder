def judge(H, M):
  changeH = H[0] + M[0]
  changeM = H[1] + M[1]
  
  if 0 <= int(changeH) <= 23 and 0 <= int(changeM) <= 59:
    return True
  else:
    return False


H, M = input().split()
H = H.zfill(2)
M = M.zfill(2)

while True:
  if judge(H, M):
    break
  else:
    if M == '59':
      M = '00'
      if H == '23':
        H = '00'
      else:
        H = str(int(H) + 1).zfill(2)
    else:
      M = str(int(M) + 1).zfill(2)

print(H, M)
