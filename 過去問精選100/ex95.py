A, B, K = map(int, input().split())

t_cookie = A - K
rest_query_num = 0

if t_cookie < 0:
  rest_query_num = abs(t_cookie)
  t_cookie = 0

a_cookie = B - rest_query_num

if a_cookie < 0:
  a_cookie = 0

print(*(t_cookie,a_cookie))