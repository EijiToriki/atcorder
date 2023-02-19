from collections import defaultdict

def factorization(n):
    arr = defaultdict(int)
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            # arr.append([i, cnt])
            arr[i] = cnt

    if temp!=1:
        # arr.append([temp, 1])
        arr[temp] = 1

    if arr==[]:
        # arr.append([n, 1])
        arr[n] = 1

    return arr

K = int(input())

factor = factorization(K)
factor = dict(factor)


ans = 0
for k, v in factor.items():
  f_min = k
  kakeru_kazu = 1
  ex = 1
  while True:
    if ex >= v:
      break
    kakeru_kazu += 1
    f_min = kakeru_kazu * k
    ex += factorization(f_min)[k]
  ans = max(ans, f_min)

print(ans)


