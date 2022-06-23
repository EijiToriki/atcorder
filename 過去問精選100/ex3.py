## 全探索
S = input()

acgt_row_length = 0
max_acgt_row_length = 0

setACGT = {'A','C','G','T'}

for ch in S:
  if ch in setACGT:
    acgt_row_length += 1
  else:
    if acgt_row_length > max_acgt_row_length:
      max_acgt_row_length = acgt_row_length
      acgt_row_length = 0

if acgt_row_length > max_acgt_row_length:
  max_acgt_row_length = acgt_row_length

print(max_acgt_row_length)

