N, X, Y = map(int, input().split())

def red(N):
  if N >= 2:
    return red(N-1) + X * blue(N)
  else:
    return 0

def blue(N):
  if N >= 2:
    return red(N-1) + Y * blue(N-1)
  else:
    return 1

print(red(N))


# if N == 1:
#   print(0)
# else:
#   red = [0 for _ in range(N+1)]
#   red[1] = 0
#   red[2] = X*Y + red[1]

#   blue = [0 for _ in range(N+1)]
#   blue[1] = 0
#   blue[2] = X*Y

#   for i in range(3, N+1):
#     blue[i] = X * Y**(i-1)
#     for j in range(2,i):
#       print(j)
#       if j == i-1:
#         blue[i] += 2 * red[j]
#       else:
#         blue[i] += red[j] 
#     red[i] = blue[i] + red[i-1]


#   print(blue[N])