R, B = map(int, input().split())
x, y = map(int, input().split())

left = 0
right = 10**32

while right-left > 1:
  mid = (left + right) // 2

  sum = 0
  if R-mid >= 0 and B-mid >= 0:
    sum = (R-mid)//(x-1) + (B-mid)//(y-1)
  
  if sum >= mid:
    left = mid
  else:
    right = mid

print(left)